class Globals {

    // Pin mchbuild to stable version to avoid breaking changes
    static String mchbuildVersion = '0.8.0'
}
pipeline {
    agent {
        label 'redhat'
    }
    triggers {
        // Run the job daily at 3:30 UTC
        cron('TZ=UTC\n30 3 * * *')
    }
    environment {
        PATH = "$workspace/.venv-mchbuild/bin:$PATH"
        HTTP_PROXY = 'http://proxy.meteoswiss.ch:8080'
        HTTPS_PROXY = 'http://proxy.meteoswiss.ch:8080'
        NO_PROXY = '.meteoswiss.ch,localhost'
    }
    options {
        // New jobs should wait until older jobs are finished
        disableConcurrentBuilds()
        // Discard old builds
        buildDiscarder(logRotator(artifactDaysToKeepStr: '7',artifactNumToKeepStr: '1', daysToKeepStr: '45', numToKeepStr: '10'))
        // Timeout the pipeline build after 1 hour
        timeout(time: 1, unit: 'HOURS')
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    echo "---- INSTALL MCHBUILD ----"
                    sh """
                    python -m venv .venv-mchbuild
                    PIP_INDEX_URL=https://hub.meteoswiss.ch/nexus/repository/python-all/simple \
                    .venv-mchbuild/bin/pip install mchbuild==${Globals.mchbuildVersion}
                    """
                }
            }
        }
        stage('Test notebooks execution') {
            steps {
                script {
                    echo "---- TEST NOTEBOOKS EXECUTION ----"
                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        sh """
                        mchbuild test.notebooks_execution
                        """
                    }
                }
            }
        }
    }
    post {
        failure {
            echo 'Sending email'
            // Send email if the execution fails
            emailext(subject: "Notebooks OGD ${env.JOB_BASE_NAME}",
                attachLog: true,
                body: """
The pipeline which checks the execution of the notebooks failed:
${env.BUILD_URL}
                """,
                to: "nina.burgdorfer@meteoswiss.ch",
                recipientProviders: [requestor(), developers()]
            )
        }
        success {
            echo 'Build succeeded'
        }
        cleanup {
            deleteDir()
        }
    }
}


