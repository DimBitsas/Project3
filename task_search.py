import re
from dates_handler import get_user_date
from task_time import task_minutes
from csv_handler import csv_content
from csv_handler import NAME
from csv_handler import TIME
from csv_handler import NOTES
from csv_handler import DATE

SEARCH_PROMPT = "\nDo you want to search by: \na) Exact Date\nb) " \
                "Exact Time Spent\nc) Exact Search\nd) Regex Pattern\ne) Return to menu\n\n"
TRY_AGAIN_PROMPT = "Please provide a valid input\nTry again!!\n\n"
STRING_PROMPT = "Enter the string: "
REGEX_PROMPT = "Enter regex pattern: "

results_list = []


class Search:
    def search(self):
        raise NotImplementedError()

    @staticmethod
    def search_scv(key, value):
        """Search csv for value, append results list"""
        content = csv_content()
        for row in content:
            if row[key] == value:
                results_list.append(row)

    @staticmethod
    def search_string_scv(key, value):
        """Search csv for exact string value, append results list"""
        content = csv_content()
        for row in content:
            if value in row[key]:
                results_list.append(row)

    @staticmethod
    def search_regex_csv(key, pattern):
        """Search csv for regex pattern, append results list"""
        content = csv_content()
        for row in content:
            if re.search(r'%s' % pattern, row[key]):
                results_list.append(row)


class DateSearch(Search):
    def __init__(self):
        self.date = str(get_user_date())

    def search(self):
        """Search date"""
        Search.search_scv(DATE, self.date)


class TimeSearch(Search):
    def __init__(self):
        self.minutes = task_minutes()

    def search(self):
        """Search time"""
        Search.search_scv(TIME, self.minutes)


class StringSearch(Search):
    def __init__(self):
        self.string = input(STRING_PROMPT)

    def search(self):
        """Search exact string"""
        Search.search_string_scv(NAME, self.string)
        Search.search_string_scv(NOTES, self.string)


class RegexSearch(Search):
    def __init__(self):
        self.pattern = input(REGEX_PROMPT)

    def search(self):
        """Search regex pattern"""
        Search.search_regex_csv(NAME, self.pattern)
        Search.search_regex_csv(NOTES, self.pattern)


def show_search_results():
    """Show to the user the search results in a appropriate format"""
    if len(results_list) == 0:
        print("None task found!!\n")
        return
    for i in results_list:
        print("\n")
        print("Date:       ", i[DATE])
        print("Title:      ", i[NAME])
        print("Time Spent: ", i[TIME])
        print("Notes:      ", i[NOTES])
        print("\nResult    ", results_list.index(i)+1, "of", len(results_list), "\n")
        user_input = input("Enter R             --> Back to search menu\nEnter any other key --> Next task\n").upper()
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
