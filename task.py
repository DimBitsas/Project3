import datetime
from log_csv import write_csv
TASK_DATE_PROMPT = "Date of the task\nPlease use DD/MM/YYYY: "
TASK_NAME_PROMPT = "\nTitle of the task: "
TASK_TIME_PROMPT = "\nTime spent (rounded minutes): "
TASK_NOTES_PROMPT = "\nNotes (Optional, you can leave this empty): "
ENTRY_ADDED = "\nThe entry has been add. Press enter to return to main menu\n"
MAIN_MENU_PROMPT = "Press enter to return to main menu\n"


class Task:
    def __init__(self):
        date_input = ""
        try:
            date_input = input(TASK_DATE_PROMPT)
            self.date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
        except ValueError:
            print("Error: {0}: does not seem to be a valid date\n".format(date_input))
            input(MAIN_MENU_PROMPT)
            return
        self.name = input(TASK_NAME_PROMPT)
        self.time = input(TASK_TIME_PROMPT)
        self.notes = input(TASK_NOTES_PROMPT)
        write_csv(self.date, self.name, self.time, self.notes)
        input(ENTRY_ADDED)


