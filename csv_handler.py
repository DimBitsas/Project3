import csv
import os

NAME = 'Name'
TIME = 'Time'
NOTES = 'Notes'
DATE = 'Date'
fieldnames = [NAME, TIME, NOTES, DATE]
filename = 'work_log.csv'


def write_csv(date, name, time, notes):
    """Write a task in a csv file
       Add a header in case that it is missing (only once)
    """
    try:
        with open(filename, 'a', newline='') as csvfile:
            log_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if os.stat(filename).st_size == 0:
                log_writer.writeheader()
            log_writer.writerow({NAME: name, TIME: time, NOTES: notes, DATE: date})
    except IOError:
        print("\nError opening file " + filename)


def csv_content():
    """Open csv file and return file content"""
    result = []
    try:
        with open(filename, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                result.append(row)
    except FileNotFoundError:
        print("\nError: File " + filename + " not found\nPlease create an entry first\n")
    except IOError:
        print("\nError opening file: " + filename)
    return result

