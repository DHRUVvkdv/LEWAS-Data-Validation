# LEWAS Water Quality Data Verification

## Project Overview

The **LEWAS Water Quality Data Verification** project aims to compare water quality data obtained from two external sources with the data available on the LEWAS (Learning Enhanced Watershed Assessment System) website. This comparison will help verify the accuracy and consistency of the data provided by our monitoring system.

## Objectives

1. **Data Collection**: Download water quality data from two external sources.
2. **Data Comparison**: Compare the external data with the data from the LEWAS website.
3. **Verification**: Validate the accuracy and consistency of the LEWAS water quality data.

## External Data Sources

1. **USGS Water Data API**

- The last ten days data is available via USGS API.

## Project Structure

The project is organized as follows:

- `data/`: Directory intended for storing downloaded data files. (**Note**: Not uploaded to the repository)
- `config/`: Directory for containing the configuration files.
- `requirements.txt`: Dependencies needed for the project.
- `README.md`: Project documentation (this file).
- `src/`: Directory containing the source files to run the code.

## Why No Data Folder Uploaded?

The `data/` folder is not uploaded to this repository due to the following reasons:

1. **Data Privacy**: Some of the data may contain sensitive or proprietary information that should not be publicly shared.
2. **Size Constraints**: The data files can be large, and including them in the repository would make it unwieldy.
3. **Dynamic Data**: The data is frequently updated, and maintaining a static version in the repository could lead to inconsistencies.

### How to Obtain the Data

To obtain the necessary data, follow these steps:

1. **Download Data**: Use the script provided in the `src/` directory to download data from the external sources.

   - `fetchData.py`: Script to download data from the USGS Water Data API.

2. **Store Data**: Save the downloaded data in the `data/raw/` directory.

### Example Usage

To download data from the USGS Water Data API, run the following command:

```sh
python3 src/fetchData.py
python3 src/fetchData.py --start-date 2024-06-02 --start-time 09:00:00 --end-date 2024-06-09 --end-time 09:00:00
```

## Errors Encountered

~~Data Error:\*\*

Data for the following parameters are available until June 5th only when the starting date is June 2nd:

- Air temperature - 3 calls to get all data
- Discharge - 3 calls to get all data
- Gage Height - 3 calls to get all data
- Precipitation - 3 calls to get all data

The following parameters seem to have correct data, but verification with more data is recommended:

- ph level
- Dissolved Oxygen
- Specific Conductance
- Turbidity
- Water Temperature~~

**Date Error:**

- Convert user input to Coordinated Universal Time (UTC) before making the API request.
- Convert the data received from the API to Eastern Standard Time (EST) format for display.
