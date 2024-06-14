# LEWAS Water Quality Data Verification

## Project Overview

The **LEWAS Water Quality Data Verification** project aims to compare water quality data obtained from two external sources with the data available on the LEWAS (Learning Enhanced Watershed Assessment System) website. This comparison will help verify the accuracy and consistency of the data provided by our monitoring system.

## Objectives

1. **Data Collection**: Download water quality data from two external sources.
2. **Data Comparison**: Compare the external data with the data from the LEWAS website.
3. **Verification**: Validate the accuracy and consistency of the LEWAS water quality data.

## Idea

The idea I have for the project is structured below:

- Download data from USGS Website.
  - Make a sensor.json having all the data stored on the USGS website - ✅
  - Figure out the API - ✅
  - Figure out way to download data. - ✅
  - Convert the user query to UTC Format - ✅
  - Convert the downloaded to EST Format - ✅
  - Make it run for the dates provided by the user - ✅
  - Doesn't work when dates are not good, have a error for this or handle this.
  - Make the script to downlaod data run whenver the date is provided or not.
- Download data from our APIs. (the server is down for LEWAS currently)
- Do some kind of ML stuff to complete missing parts of our Lab data (we have internet issues)
- Discuss with Yunus (PhD student) about how to use these results to verify our work.
- Make the script, service to compare both the data and show it on our website (OWLS).
- Once this is implemented, do this for the other parameters we have on the site. (potentially get data from other APIs)

## To Do:

- Make a function that checks if the data is already downloaded.
  - First is it a single file - should be easy
  - Second if its a different files like June 2 to June 6, 5 am to 5 am in one file and 6 June to 10 June in other file.
- Figure out how to delete the data once it gets downloaded
  - Can store just important stuff from the data.
- Make a script to delete the data.
- Have the code working without any date provided by the user
  - Figure out the last date the project was run and implement the
- Have the code working with any date provided by the user

  - check if the date is valid.
    - if older than 10 days then just give them the stored important stuff (figure this with the team)
    - othersise throw the error.
  - if valid run the command and store the data

  cahnge the time zone

  have archives - debugging purposes,

  downalods every day.

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
python3 src/fetchData.py --start-date 2024-06-02 --start-time 05:00:00 --end-date 2024-06-9 --end-time 05:00:00
python3 src/fetchData.py --start-date 2024-06-03 --start-time 05:00:00 --end-date 2024-06-10 --end-time 05:00:00
The time is 5am in EST which account to 9am to UTC (Daylight Savings ON - Jun 12)
```

## Errors Encountered

~~Data Error:\*\*

Data for the following parameters are available until June 5th only when the starting date is June 2nd:

- Air temperature - 3 calls to get all data - 5 min
- Discharge - 3 calls to get all data
- Gage Height - 3 calls to get all data
- Precipitation - 3 calls to get all data

The following parameters seem to have correct data, but verification with more data is recommended:

- ph level - 15 min
- Dissolved Oxygen
- Specific Conductance
- Turbidity
- Water Temperature~~

**Date Error:**

- Convert user input to Coordinated Universal Time (UTC) before making the API request.
- Convert the data received from the API to Eastern Standard Time (EST) format for display.
