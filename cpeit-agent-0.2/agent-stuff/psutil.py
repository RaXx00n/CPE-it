import csv
import psutil

# Get a list of running processes
processes = []
for process in psutil.process_iter(['pid', 'name', 'exe']):
    try:
        processes.append({
            'pid': process.info['pid'],
            'name': process.info['name'],
            'path': process.info['exe']
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Write the list of processes to a CSV file
with open('software_inventory.csv', 'w', newline='') as csvfile:
    fieldnames = ['pid', 'name', 'path']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for process in processes:
        writer.writerow(process)
