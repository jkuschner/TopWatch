import get_time

start_menu_options = ["Start a new activity", "End an activity", "Print the log", "Export the log to .csv", "Import the log from .csv","Clear the log","Open settings","Quit TopWatch"]

menu_prompt = "What would you like to do?"

startup_message = "Welcome to TopWatch!!!"

end_activity_prompt = "Which activity do you want to end?"

settings_menu_options = ["Change time format(24/12 hr)","Change timezone", "Change default file location","Back to main menu"]

timezones = {'Pacific':'US/Pacific', 'Mountain':'US/Mountain','Central':'US/Central','Eastern':'US/Eastern','Hawaii':'US/Hawaii','UTC':'UTC'}

timezone_options = ['Pacific','Mountain','Central','Eastern','Hawaii','UTC']

def get_timezone(tz):
  try:
    my_tz = timezones[tz]
    return my_tz
  except KeyError:
    print("Not a valid timezone")