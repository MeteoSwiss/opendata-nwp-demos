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

You can run the notebooks in two ways:

- **Google Colab**: open a specific notebook directly in Colab.
- **RenkuLab**: launch the full project environment with all notebooks available.

    [![launch - renku](https://renkulab.io/renku-badge.svg)](https://renkulab.io/p/meteoswiss/opendata-nwp-demos/sessions/01KME52HC2FZ6ZHB30SSFG08PW/start)



| Notebook | Description | Open in Colab |
|---|---|---|
| [**01_retrieve_process_precip.ipynb**](01_retrieve_process_precip.ipynb) | Retrieve and load precipitation forecasts as an Xarray object, then process, analyze, and visualize the data using Python tools. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/01_retrieve_process_precip.ipynb) |
| [**02_download_soil_temp.ipynb**](02_download_soil_temp.ipynb) | Download forecast files to disk for offline storage, external tools, or advanced manual processing. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/02_download_soil_temp.ipynb) |
| [**03_calculate_wind_speed.ipynb**](03_calculate_wind_speed.ipynb) | Retrieve wind component forecasts as Xarray objects and derive the horizontal wind speed using [meteodata-lab](https://meteoswiss.github.io/meteodata-lab/). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/03_calculate_wind_speed.ipynb) |
| [**04_calculate_rel_humidity.ipynb**](04_calculate_rel_humidity.ipynb) | Retrieve specific humidity, temperature and pressure as Xarray objects and compute relative humidity. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/04_calculate_rel_humidity.ipynb) |
| [**05_interpolate_vertically.ipynb**](05_interpolate_vertically.ipynb) | Retrieve temperature forecasts and perform vertical interpolation from model levels to pressure levels or target altitude. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/05_interpolate_vertically.ipynb) |
| [**06_calculate_global_rad_flux.ipynb**](06_calculate_global_rad_flux.ipynb) | Retrieve radiation fluxes and compute the global radiation flux using [meteodata-lab](https://meteoswiss.github.io/meteodata-lab/). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/06_calculate_global_rad_flux.ipynb) |
| [**07_where_will_it_rain_next_24h.ipynb**](07_where_will_it_rain_next_24h.ipynb) | Visualize the probability of precipitation over Switzerland for the next 24 hours. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/07_where_will_it_rain_next_24h.ipynb) |
| [**08_where_will_the_sun_shine.ipynb**](08_where_will_the_sun_shine.ipynb) | Map the probability of experiencing over 6 hours of sunshine on the day after tomorrow. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/08_where_will_the_sun_shine.ipynb) |
| [**09_constant_parameters.ipynb**](09_constant_parameters.ipynb) | Retrieve constant model parameters and verify grid consistency with forecast parameters. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/09_constant_parameters.ipynb) |
| [**10_icon_ch2_pollen_forecast.ipynb**](10_icon_ch2_pollen_forecast.ipynb) | Retrieve, convert, and visualize ICON-CH2-EPS pollen forecasts. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/10_icon_ch2_pollen_forecast.ipynb) |
| [**11_analysis_data.ipynb**](11_analysis_data.ipynb) | Retrieve and visualize KENDA CH1 analysis data. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MeteoSwiss/opendata-nwp-demos/blob/main/11_analysis_data.ipynb) |
## 🚀 Getting Started

You can run the notebooks in three ways.

### Option 1: Open a single notebook in Google Colab

Use Google Colab if you want to open one notebook directly.

Click the **Open in Colab** badge next to the notebook in the table above, then run the notebook cells from top to bottom.

The first cell installs the required Python dependencies.

### Option 2: Run the full project in RenkuLab

Use RenkuLab if you want to start a project session with all notebooks available.

[![launch - renku](https://renkulab.io/renku-badge.svg)](https://renkulab.io/p/meteoswiss/opendata-nwp-demos/sessions/01KME52HC2FZ6ZHB30SSFG08PW/start)

1. Launch the RenkuLab session.
2. Navigate to the `opendata-nwp-demos` folder.
3. Open the notebook you would like to try.
4. Run the notebook cells from top to bottom.

The first cell installs the required Python dependencies.

### Option 3: Run locally

Clone the repository and install all required packages. This project requires **Python >=3.11,<3.13** and [Poetry](https://python-poetry.org/docs/) to manage dependencies and environments.

1. Install Python dependencies using Poetry:

    ```bash
    poetry install
    ```

2. Install the Jupyter kernel:

    ```bash
    poetry run python -m ipykernel install --user --name=notebooks-nwp-env --display-name "Python (notebooks-nwp-env)"
    ```

3. Open the notebook in VS Code or JupyterLab and select the kernel **Python (notebooks-nwp-env)**.

## 📚 Related Documentation

For more context on the available numerical weather forecast data and how it’s structured, see:

  🔗 [MeteoSwiss Forecast Data Documentation](https://opendatadocs.meteoswiss.ch/e-forecast-data/e2-e3-numerical-weather-forecasting-model)

## 💬 Feedbacks
Feel free to open issues to suggest improvements or contribute new examples!

## 🧑‍💻 Developers

When making a change:

1. Work on the notebook in `developer_notebooks/`.
2. Developer notebooks should use the `_clean` suffix, for example `09_notebook_clean.ipynb`.
3. Commit the developer notebook **without outputs**. This keeps PR review manageable and avoids noisy diffs from generated output.
4. Once the developer notebook has been reviewed, run it and save the corresponding notebook **with outputs** at the top level of the repository, without the `_clean` suffix. This is the version users will look at.
### RenkuLab image

The RenkuLab image was built from `pyproject.toml` to provide a compatible base environment. Since the notebooks install dependencies again in the first cell, the image does not need to be rebuilt after every dependency change.

If the supported Python version changes, rebuild the RenkuLab image so the session starts with the correct Python version. To do this, open the RenkuLab project and click **Rebuild**.

For more information about Renku at MeteoSwiss, see the [Renku documentation](https://meteoswiss.atlassian.net/wiki/spaces/MLOpsMCH/pages/346298461/Renku).
