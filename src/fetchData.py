import requests
import json
import os
from datetime import datetime

def format_date(date):
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")

def fetch_USGS_observations(sensor_name, sensor_id, start_time, end_time):
    # Base URL of the API
    base_url = "https://labs.waterdata.usgs.gov/sta/v1.1/Datastreams"
    # Construct the URL with the sensor ID and filter parameters
    url = f"{base_url}('{sensor_id}')/Observations?$filter=phenomenonTime ge {start_time} and phenomenonTime le {end_time}"

    all_observations = []

    while url:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            all_observations.extend(data['value'])

            # Check if there is a next link
            url = data.get('@iot.nextLink')
        else:
            return f"Error: {response.status_code}, {response.text}"  # Return an error message

    return all_observations

def download_all_USGS_sensor_data(start_time, end_time):
    # Convert start_time and end_time to the required string format
    start_time_str = format_date(start_time)
    end_time_str = format_date(end_time)

    # Read the sensor data from the JSON file
    with open('config/sensorData.json') as file:
        sensor_data = json.load(file)

    # Create a folder name based on the start and end dates
    folder_name = f"data/raw/{start_time_str}_{end_time_str}/USGS_Data"

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Iterate over each sensor in the sensorNameToId dictionary
    for sensor_name, sensor_id in sensor_data['sensorNameToId'].items():
        print(f"Downloading data for sensor: {sensor_name}")

        # Fetch the observations for the current sensor
        observations = fetch_USGS_observations(sensor_name, sensor_id, start_time_str, end_time_str)

        if isinstance(observations, list):
            # Generate the output file name with the sensor name
            output_file = f"{folder_name}/{sensor_name}.json"

            # Write the observations to a new JSON file
            with open(output_file, 'w') as file:
                json.dump(observations, file, indent=4)

            print(f"Observations saved to {output_file}")
        else:
            print(observations)  # Print the error message

        print()  # Print a blank line for separation

if __name__ == "__main__":
    # Define the date range using datetime objects
    start_time = datetime(2024, 6, 2, 9, 0, 0)
    end_time = datetime(2024, 6, 9, 9, 0, 0)

    # Download data for all sensors
    download_all_USGS_sensor_data(start_time, end_time)