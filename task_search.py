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


class Search:
    def search(self):
        raise NotImplementedError()

    @staticmethod
    def search_scv(key, value):
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

    @staticmethod
    def search_regex_csv(key, pattern):
        """Search csv for value, append results list"""
        try:
            with open(filename, newline='') as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=',')
                for row in csv_reader:
                    if re.search(r'%s' % pattern, row[key]):
                        results_list.append(row)
        except FileNotFoundError:
            print("\nError: File " + filename + " not found\nPlease create an entry first\n")
        except IOError:
            print("\nError opening file: " + filename)


class DateSearch(Search):
    def __init__(self):
        self.date = str(get_user_date())

    def search(self):
        Search.search_scv('Date', self.date)


class TimeSearch(Search):
    def __init__(self):
        while True:
            minutes = input(TIME_SPENT_PROMPT)
            if not minutes.isdigit():
                print("Error: Please provide a numeric value\n")
                continue
            self.minutes = minutes
            break

    def search(self):
        Search.search_scv('Time', self.minutes)


class StringSearch(Search):
    def __init__(self):
        self.string = input(STRING_PROMPT)

    def search(self):
        Search.search_scv('Name', self.string)
        Search.search_scv('Notes', self.string)


class RegexSearch(Search):
    def __init__(self):
        self.pattern = input(REGEX_PROMPT)

    def search(self):
        Search.search_regex_csv('Name', self.pattern)
        Search.search_regex_csv('Notes', self.pattern)


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
            DateSearch().search()
        elif user_input == 'B':
            TimeSearch().search()
        elif user_input == 'C':
            StringSearch().search()
        elif user_input == 'D':
            RegexSearch().search()
        else:
            print(TRY_AGAIN_PROMPT)
        show_search_results()
