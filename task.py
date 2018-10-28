from dates_handler import get_user_date
from csv_handler import write_csv
from task_time import task_minutes

TASK_NAME_PROMPT = "Title of the task: "
TASK_NOTES_PROMPT = "Notes (Optional, you can leave this empty): "
ENTRY_ADDED = "The entry has been add. Press enter to return to main menu\n"


class Task:
    def __init__(self):
        self.date = get_user_date()
        self.name = input(TASK_NAME_PROMPT)
        self.time = task_minutes()
        self.notes = input(TASK_NOTES_PROMPT)
        write_csv(self.date, self.name, self.time, self.notes)
        input(ENTRY_ADDED)


