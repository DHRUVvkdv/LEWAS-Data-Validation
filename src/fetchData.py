import requests
import json
import os

def fetch_USGS_observations(sensor_name, sensor_id, start_time, end_time):
    # Base URL of the API
    base_url = "https://labs.waterdata.usgs.gov/sta/v1.1/Datastreams"
    # Construct the URL with the sensor ID and filter parameters
    url = f"{base_url}('{sensor_id}')/Observations?$filter=phenomenonTime ge {start_time} and phenomenonTime le {end_time}"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON data from the response
    else:
        return f"Error: {response.status_code}, {response.text}"  # Return an error message

def download_all_USGS_sensor_data(start_time, end_time):
    # Read the sensor data from the JSON file
    with open('config/sensorData.json') as file:
        sensor_data = json.load(file)

    # Create a folder name based on the start and end dates
    folder_name = f"data/raw/{start_time}_{end_time}/USGS_Data"

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Iterate over each sensor in the sensorNameToId dictionary
    for sensor_name, sensor_id in sensor_data['sensorNameToId'].items():
        print(f"Downloading data for sensor: {sensor_name}")

        # Fetch the observations for the current sensor
        observations = fetch_USGS_observations(sensor_name, sensor_id, start_time, end_time)

        if isinstance(observations, dict):
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
    # Define the date range
    start_time = '2024-06-01T09:05:00Z'
    end_time = '2024-06-08T09:05:00Z'

    # Download data for all sensors
    download_all_USGS_sensor_data(start_time, end_time)