<h1 align="center">OGD Model Data Access & Processing</h1>
<h3 align="center">Jupyter Notebook Examples Using MeteoSwiss NWP Data</h3>

<p align="center">
  <img src="images/logo_mch.png" alt="MCH Logo" width="130" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="images/logo_opendata.jpeg" alt="Open Data Logo" width="130" />
</p>

This repository provides Jupyter notebook examples for accessing and processing numerical weather prediction (NWP) model data from **MeteoSwiss**, released through Switzerland’s **Open Government Data (OGD)** initiative.

---

## 📓 Example Notebooks

- [**01_retrieve_process_precip.ipynb**](01_retrieve_process_precip.ipynb) - Retrieve, process, and visualize ensemble precipitation forecasts from the ICON model.

## 🚀 Getting Started

### Install Dependencies

Clone the repository and install all required packages using:
 1. **Ensure Python 3.11 is installed**  
  This project requires **Python 3.11**. You can check your current version with:
    ```bash
    python3 --version
    ```
    If Python 3.11 is not installed, run the following script to install it with `pyenv`:
    ```bash
    bash install_python.sh
    ```

 2. **Install ecCodes using conda**
    > ⚠️ **Temporary Setup Notice**  
    > From **ecCodes 2.37.0** onwards, this step won't be needed as the Python wheel will include the binary automatically. This change is expected to take effect soon.


    ```bash
    bash install_eccodes.sh
    ```

 3. **Install Poetry**  
  Poetry is used to manage Python dependencies and environments. Install it using the official installer:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    Make sure poetry is available in your shell (you may need to restart your terminal or follow the post-install instructions shown after installation).

    Check the version to confirm it's installed:
    ```bash
    poetry --version
    ```

4. **Install Python dependencies using Poetry**
    ```bash
    poetry install
    ```

5. **Install the Jupyter kernel**  
    Activate the Poetry environment and register it as a Jupyter kernel so it can be used within notebooks:
    ```bash
    poetry shell
    poetry run python -m ipykernel install --user --name=notebooks-nwp-env --display-name "Python (notebooks-nwp-env)"
    ```

6. **Open and run notebooks**  
    You can run the notebooks using **Visual Studio Code** or **JupyterLab** — whichever you prefer.

    **Option A: Using Visual Studio Code**

    Make sure you have the following VS Code extensions installed:

    - Python

    - Jupyter (by Microsoft)

    Once installed:

    1. Open the project folder in VS Code.

    2. Open the .ipynb notebook file.

    3. When prompted (or from the top-right kernel picker), select the kernel: Python (notebooks-nwp-env)
    
    > 💡 If you don't see the environment, restart VS Code after running the kernel installation step.
    ---

    **Option B: Using JupyterLab**

    If you don't have VS Code or prefer using JupyterLab:

    1. Install JupyterLab inside the Poetry environment (if not already installed):
        ```bash
        poetry run pip install jupyterlab
        ```
    2. Launch JupyterLab:
        ```bash
        poetry run juypter lab
        ```
    3. Open your notebook and select the kernel **Python (notebooks-nwp-env)** from the kernel menu.


## 📚 Related Documentation

For more context on the available numerical weather forecast data and how it’s structured, see:

  🔗 [MeteoSwiss Forecast Data Documentation](https://github.com/MeteoSwiss/opendata-forecast-data/blob/main/README.md#2-numerical-weather-forecasting-model-data)

## 💬 Feedbacks
Feel free to open issues to suggest improvements or contribute new examples!

