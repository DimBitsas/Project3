import csv
import re
from dates_handler import get_user_date
from log_csv import filename

SEARCH_PROMPT = "\nDo you want to search by: \na) Exact Date\nb) " \
                "Exact Time Spent\nc) Exact Search\nd) Regex Pattern\ne) Return to menu\n\n"
TRY_AGAIN_PROMPT = "Please provide a valid input\nTry again!!\n\n"
TIME_SPENT_PROMPT = "Time Spent (minutes)"
STRING_PROMPT = "Enter the string"
REGEX_PROMPT = "Enter regex pattern"

results_list = []


def show_search_results():
    """Show to the user the search results in a appropriate format"""
    if len(results_list) == 0:
        print("None task found!!\n")
        return
    for i in results_list:
        print("\n")
        print("Date:       ", i['Date'])
        print("Title:      ", i['Name'])
        print("Time Spent: ", i['Time'])
        print("Notes:      ", i['Notes'])
        print("\nResult    ", results_list.index(i)+1, "of", len(results_list), "\n")
        user_input = input("Enter R for search menu\nEnter any other key for next task\n").upper()
        if user_input == 'R':
            return


def search_csv(key, value):
    """Search csv for value, append results list"""
    try:
        with open(filename, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if row[key] == value:
                    results_list.append(row)
    except FileNotFoundError:
        print("\nError: File " + filename + " not found\nPlease create an entry first\n")
    except IOError:
        print("\nError opening file: " + filename)


def search_regex_csv(key, pattern):
    """Search csv for value, append results list"""
    try:
        with open(filename, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            for row in csv_reader:
                if re.search(r'%s' % pattern, row[key]):
                    results_list.append(row)
    except FileNotFoundError:
        print("\nError: File "+filename+" not found\nPlease create an entry first\n")
    except IOError:
        print("\nError opening file: " + filename)


def date_search():
    """Search tasks in the csv based on date input"""
    date = get_user_date()
    search_csv('Date', str(date))


def time_search():
    """Search tasks in the csv based on minutes input"""
    minutes = input(TIME_SPENT_PROMPT)
    search_csv('Time', minutes)


def string_search():
    """Search tasks in the csv based on string input"""
    string = input(STRING_PROMPT)
    search_csv('Name', string)
    search_csv('Notes', string)


def regex_search():
    """Search tasks in the csv based on regex pattern input"""
    pattern = input(REGEX_PROMPT)
    search_regex_csv('Name', pattern)
    search_regex_csv('Notes', pattern)


def tasks_search():
    """Provide/Choose search type
       Show search results
    """
    while True:
        results_list.clear()
        user_input = input(SEARCH_PROMPT).upper()
        if user_input == 'E':
            return
        elif user_input == 'A':
            date_search()
        elif user_input == 'B':
            time_search()
        elif user_input == 'C':
            string_search()
        elif user_input == 'D':
            regex_search()
        else:
            print(TRY_AGAIN_PROMPT)
        show_search_results()

