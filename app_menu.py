import sys
from task import Task
MAIN_MENU_PROMPT = "WORK_LOG\nWhat would you like to do?\na) add new entry\n" \
                   "b) Search in existing entries\nc) Quit program\n"


def app_menu():
    while True:
        prompt_res = input(MAIN_MENU_PROMPT).upper()
        if prompt_res == "A":
            Task()
            continue;
        elif prompt_res == "B":
            print("BBBB")
            break;
        elif prompt_res == "C":
            print("CCCCC")
            sys.exit()
        else:
            print("Error: Please provide a valid input: a,b or c\n")


if __name__ == '__main__':
    app_menu()
