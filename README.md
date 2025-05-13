<h1 align="center">OGD Model Data Access & Processing</h1>
<h3 align="center">Jupyter Notebook Examples Using MeteoSwiss NWP Data</h3>

<p align="center">
  <img src="images/logo_mch.png" alt="MCH Logo" width="130" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="images/logo_opendata.jpeg" alt="Open Data Logo" width="130" />
</p>

This repository provides Jupyter notebook examples for accessing and processing numerical weather prediction (NWP) model data from **MeteoSwiss**, released through Switzerland’s **Open Government Data (OGD)** initiative.

---

## 📓 Notebooks

- [**01_retrieve_process_precip.ipynb**](01_retrieve_process_precip.ipynb)- Retrieve and load precipitation forecasts as an Xarray object, then process, analyze, and visualize the data using Python tools.
- [**02_download_soil_temp.ipynb**](02_download_soil_temp.ipynb) — Download forecast files to disk for offline storage, external tools, or advanced manual processing.
- [**03_calculate_wind_speed.ipynb**](03_calculate_wind_speed.ipynb) — Retrieve wind component forecasts as Xarray objects and derive the horizontal wind speed using the Python library [meteodata-lab](https://meteoswiss.github.io/meteodata-lab/).

## 🚀 Getting Started

### Install Dependencies

Clone the repository and install all required packages. This project requires **Python 3.11** and [Poetry](https://python-poetry.org/docs/) to manage dependencies and environments.

1. #### Install Python dependencies using Poetry
    ```bash
    poetry install
    ```

2. #### Install the Jupyter kernel
    Activate the Poetry environment and register it as a Jupyter kernel so it can be used within notebooks:
    ```bash
    poetry run python -m ipykernel install --user --name=notebooks-nwp-env --display-name "Python (notebooks-nwp-env)"
    ```

### Open and Run Notebooks

You can run the notebooks using **Visual Studio Code** or **JupyterLab** — whichever you prefer.

#### Option A: Using Visual Studio Code

Make sure you have the following VS Code extensions installed:

- Python (by Microsoft)
- Jupyter (by Microsoft)

Once installed:

1. Open the project folder in VS Code.
2. Open a Jupyter notebook file, for example `01_retrieve_process_precip.ipynb`.
3. When prompted (or from the top-right kernel picker), select the kernel: **Python (notebooks-nwp-env)**.

> 💡 If you don't see the environment, restart VS Code after running the kernel installation step.

---

#### Option B: Using JupyterLab

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
