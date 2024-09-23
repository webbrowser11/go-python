import csv
import requests
import time
from datetime import datetime
from io import StringIO

def check_task_completion(csv_url):
    # Fetch the CSV file from the URL
    response = requests.get(csv_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        csv_data = response.content.decode('utf-8')
        
        # Convert the CSV content into a file-like object
        csv_file = StringIO(csv_data)
        
        # Read the CSV content
        reader = csv.DictReader(csv_file)
        
        # Get the current date and time
        current_time = datetime.now()
        
        for row in reader:
            task = row['task']
            date_finished = row['datetobefinished']
            time_finished = row['timetobefinsihed']
            
            # Combine date and time for comparison
            finished_time_str = f"{date_finished} {time_finished}"
            finished_time = datetime.strptime(finished_time_str, "%m/%d/%y %I:%M")
            
            # Check if the task is finished based on the current time
            if finished_time <= current_time:
                print(f"The task '{task}' has been finished at {finished_time}.")
            else:
                print(f"The task '{task}' is not yet finished. go finish it.")
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")

# Usage
csv_url = 'https://webbrowser11.github.io/go-python/tasks/tasks.csv'  # Replace with your CSV URL
check_task_completion(csv_url)
time.sleep(30)
