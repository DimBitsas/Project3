import csv
from dates_handler import get_user_date
from log_csv import filename

SEARCH_PROMPT = "\nDo you want to search by: \na) Exact Date\nb) " \
                "Exact Time Spent\nc) Exact Search\nd) Regex Pattern\ne) Return to menu\n\n"
TRY_AGAIN = "Please provide a valid input\nTry again!!\n\n"
results_list = []


def show_search_results():
    """Show to the user the search results in a appropriate format"""
    print("\n")
    for i in results_list:
        print("Date:       ", i['Date'])
        print("Title:      ", i['Name'])
        print("Time Spent: ", i['Time'])
        print("Notes:      ", i['Notes'])
        print("Result      ", results_list.index(i)+1, "of", len(results_list), "\n")


def date_search():
    date = get_user_date()
    with open(filename, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_reader:
            if row['Date'] == str(date):
                results_list.append(row)

    show_search_results()





def time_search():
    print("time")


def string_search():
    print("string")


def regex_search():
    print("regex")


def tasks_search():
    while True:
        user_input = input(SEARCH_PROMPT).upper()
        if user_input == 'E':
            break
        elif user_input == 'A':
            date_search()
            break
        elif user_input == 'B':
            time_search()
            break
        elif user_input == 'C':
            string_search()
            break
        elif user_input == 'D':
            regex_search()
            break
        else:
            print(TRY_AGAIN)

