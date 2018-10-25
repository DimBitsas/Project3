import csv
import os

fieldnames = ['Name', 'Time', 'Notes', 'Date']
filename = 'work_log.csv'


def write_csv(date, name, time, notes):
    """Write a task in a csv file
       Add a header in case that it is missing (only once)
    """
    with open(filename, 'a', newline='') as csvfile:
        log_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if os.stat(filename).st_size == 0:
            log_writer.writeheader()
        log_writer.writerow({"Name": name, "Time": time, "Notes": notes, "Date": date})
