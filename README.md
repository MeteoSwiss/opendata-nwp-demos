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

- [**00_download_forecast_data.ipynb**](00_download_forecast_data.ipynb) - Download and read soil temperature forecast from the ICO
- [**01_retrieve_process_precip.ipynb**](01_retrieve_process_precip.ipynb) - Retrieve, process, and visualize deterministic precipitation forecasts from the ICON model.

## 🚀 Getting Started

### Install Dependencies

Clone the repository and install all required packages:
1. #### Ensure Python 3.11 is installed
    This project requires **Python 3.11**. You can check your current version with:
    ```bash
    python3 --version
    ```

2. #### Install Poetry 1.8.1
    Poetry is used to manage Python dependencies and environments. Install it using the official installer:
      ```bash
      curl -sSL https://install.python-poetry.org | python3 - --version 1.8.1
      ```
      Make sure poetry is available in your shell (you may need to restart your terminal or follow the post-install instructions shown after installation).

      Verify that Poetry is installed and check the version:
      ```bash
      poetry --version
      ```

3. #### Install Python dependencies using Poetry
    Make sure to be at the root of the project's folder.
    ```bash
    poetry install
    ```

4. #### Install the Jupyter kernel
    Activate the Poetry environment and register it as a Jupyter kernel so it can be used within notebooks:
    ```bash
    poetry shell
    python -m ipykernel install --user --name=notebooks-nwp-env --display-name "Python (notebooks-nwp-env)"
    ```

5. #### Open and run notebooks
    You can run the notebooks using **Visual Studio Code** or **JupyterLab** — whichever you prefer.

    **Option A: Using Visual Studio Code**

    Make sure you have the following VS Code extensions installed:

    - Python (by Microsoft)

    - Jupyter (by Microsoft)

    Once installed:

    1. Open the project folder in VS Code.

    2. Open a jupyter notebook file, for example 01_retrieve_process_precip.ipynb.

    3. When prompted (or from the top-right kernel picker), select the kernel: Python (notebooks-nwp-env)

    > 💡 If you don't see the environment, restart VS Code after running the kernel installation step.
    ---

    **Option B: Using JupyterLab**

    If you don't have VS Code or prefer using JupyterLab:
    1. Install JupyterLab using `pipx`:
        ```bash
        pipx install jupyterlab
        ```
        Don’t have `pipx` yet? Get it here: [https://pipx.pypa.io/stable/installation/](https://pipx.pypa.io/stable/installation/)
    2. Launch JupyterLab:
        ```bash
        jupyter lab
        ```
    3. Open your notebook and select the kernel **Python (notebooks-nwp-env)** from the kernel menu.


## 📚 Related Documentation

For more context on the available numerical weather forecast data and how it’s structured, see:

  🔗 [MeteoSwiss Forecast Data Documentation](https://opendatadocs.meteoswiss.ch/e-forecast-data/e2-e3-numerical-weather-forecasting-model)

## 💬 Feedbacks
Feel free to open issues to suggest improvements or contribute new examples!
