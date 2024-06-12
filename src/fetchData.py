import requests
import json
import os
from datetime import datetime
import argparse
import sys

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
    with open('config/sensor_data.json') as file:
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

def parse_arguments():
    if len(sys.argv) != 9:
        print("Error: Incorrect number of arguments.")
        print("Usage: python script_name.py <start_date> <start_time> <end_date> <end_time>")
        print("Example: python script_name.py 2024-06-02 09:00:00 2024-06-09 09:00:00")
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Download USGS sensor data.')
    parser.add_argument('--start-date', type=str, required=True,
                        help='Start date in the format YYYY-MM-DD')
    parser.add_argument('--start-time', type=str, default='00:00:00',
                        help='Start time in the format HH:MM:SS (default: 00:00:00)')
    parser.add_argument('--end-date', type=str, required=True,
                        help='End date in the format YYYY-MM-DD')
    parser.add_argument('--end-time', type=str, default='23:59:59',
                        help='End time in the format HH:MM:SS (default: 23:59:59)')
    return parser.parse_args()

def get_day_name(date):
    return date.strftime("%A")

def save_last_run_config(start_time, end_time):
    config_data = {
        "start_date": start_time.strftime("%Y-%m-%d"),
        "start_time": start_time.strftime("%H:%M:%S"),
        "end_date": end_time.strftime("%Y-%m-%d"),
        "end_time": end_time.strftime("%H:%M:%S")
    }

    # Write the configuration data to a JSON file
    with open('config/last_run.json', 'w') as file:
        json.dump(config_data, file, indent=4)

if __name__ == "__main__":
# Parse command-line arguments
    args = parse_arguments()

    # Create datetime objects from the provided arguments
    start_time = datetime.strptime(f"{args.start_date} {args.start_time}", "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(f"{args.end_date} {args.end_time}", "%Y-%m-%d %H:%M:%S")

    # Get the day names for start_time and end_time
    start_day = get_day_name(start_time)
    end_day = get_day_name(end_time)

    print(f"Start Day: {start_day}")
    print(f"End Day: {end_day}")

    # Download data for all sensors
    download_all_USGS_sensor_data(start_time, end_time)

    save_last_run_config(start_time, end_time)