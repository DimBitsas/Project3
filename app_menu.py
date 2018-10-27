import sys
from task import Task
from task_search import tasks_search
MAIN_MENU_PROMPT = "WORK_LOG\nWhat would you like to do?\na) add new entry\n" \
                   "b) Search in existing entries\nc) Quit program\n"


def app_menu():
    """Application menu"""
    while True:
        prompt_res = input(MAIN_MENU_PROMPT).upper()
        if prompt_res == "A":
            Task()
        elif prompt_res == "B":
            tasks_search()
        elif prompt_res == "C":
            sys.exit()
        else:
            print("Error: Please provide a valid input: a,b or c\n")


if __name__ == '__main__':
    app_menu()
