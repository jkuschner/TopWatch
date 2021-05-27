import get_time

start_menu_options = ["Start a new activity", "End an activity", "Print the log", "Export the log to .csv", "Import the log from .csv","Quit TopWatch"]

start_menu_prompt = "What would you like to do?"

startup_message = "Welcome to TopWatch!!!"

end_activity_prompt = "Which activity do you want to end?"

default_file = get_time.get_date(extension=".csv",directory="logs/")