import log
import get_time
import strings
import csv

activities = [] # A list of dictionaries that represent each individual activity
curr_acts = []  # A list of pairs that contain activity names(1) and their start time(2) as strings that represent unfinished activities

timezone = strings.timezones['Pacific']
default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")

def getNumInput(prompt_message):
  while True:
    try:
      option = int(input(prompt_message))
      return option
    except ValueError:
      print("Input must be number.")
      continue

def printMenuOptions(options, menu_prompt):
  if not options:
    print("Error: no menu options\n")
    return
  else:
    print(menu_prompt)
    for i,option in enumerate(options):
      if isinstance(option, tuple):
        print(f"[ {i} ] {option[0]}")
      else:
        print(f"[ {i} ] {option}")
    print()

# Load a log from log.csv if available by default
try:
  print("Loading existing log data...")
  with open(default_file,'r') as data:
    for line in csv.DictReader(data):
      log.add_activity(activities,line)
    print("Successfully loaded log data\n")
except IOError:
  print("No log data to load\n")

    
print(strings.startup_message + "\n")

while True:
  printMenuOptions(strings.start_menu_options, strings.menu_prompt)

  start_opt = input("Choose a menu option: ")

  print()

  if start_opt == '0' or start_opt == 'start': # Start a new activity
    name = input("What are you going to do?(<50 chars): ")
    curr_acts.append((name, get_time.get_time(timezone)))
    print('Good Luck!\n')


  elif start_opt == '1' or start_opt == 'end': # End an activity
    if len(curr_acts) < 1:
      print("You can't end an activity without starting one first.\n")
    elif len(curr_acts) == 1:
      activities = log.add_activity(activities, log.make_activity(curr_acts[0][0],curr_acts[0][1],get_time.get_time(timezone)))
      print(f'Nice job finishing {curr_acts[0][0]}\n')
      del curr_acts[0]
    else:
      printMenuOptions(curr_acts, strings.end_activity_prompt)
        
      ending_option = getNumInput("Which one?: ")
      
      ending_name = curr_acts[ending_option][0]
      ending_start = curr_acts[ending_option][1]

      activities = log.add_activity(activities, log.make_activity(ending_name, ending_start, get_time.get_time(timezone)))
      print(f'Nice job finishing {curr_acts[ending_option][0]}\n')
      del curr_acts[ending_option]

      
    
  elif start_opt == '2' or start_opt == 'print': # Print the log
    log.print_log(activities)
  
  elif start_opt == '3' or start_opt == 'export': # Export to csv
    log.export_log(activities, default_file)

  elif start_opt == '4' or start_opt == 'import': # Import from csv
    log.import_log(activities, default_file)

  elif start_opt == '5' or start_opt == 'clear': # Clear the log
    log.clear(activities)

  elif start_opt == '6' or start_opt == 'settings': # Open Settings
    while True:
      printMenuOptions(strings.settings_menu_options, strings.menu_prompt)
      settings_opt = input("Choose a menu option: ")

      if settings_opt == '0':
        # Change time format
        print("Changed time format(not really)")

      elif settings_opt == '1': # Change timezone
        print(f"The current timezone is {timezone}.\n")
        while True:
          printMenuOptions(strings.timezone_options, "Which timezone do you want?")
          timezone_opt = input("Choose a menu option: ")

          if timezone_opt == '0' or timezone_opt == 'Pacific':
            timezone = strings.timezones['Pacific']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          elif timezone_opt == '1' or timezone_opt == 'Mountain':
            timezone = strings.timezones['Mountain']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          elif timezone_opt == '2' or timezone_opt == 'Central':
            timezone = strings.timezones['Central']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          elif timezone_opt == '3' or timezone_opt == 'Eastern':
            timezone = strings.timezones['Eastern']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          elif timezone_opt == '4' or timezone_opt == 'Hawaii':
            timezone = strings.timezones['Hawaii']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          elif timezone_opt == '5' or timezone_opt == 'UTC':
            timezone = strings.timezones['UTC']
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            break
          else:
            print("Not a valid option\n")
            continue

      
      elif settings_opt == '2':
        # Change default file location
        if default_file == get_time.get_date(timezone,extension=".csv",directory="logs/"):
          default_file = input("New default file location: ")
          print(f"Changed default file locaction to {default_file}\n")
        else:
          print(f"Default file location is currently {default_file}\n")
          confirm = input("Do you want to reset(Y) or change again(n)? [Y/n] ")
          if confirm == 'n':
            default_file = input("New default file location: ")
            print(f"Changed default file location to {default_file}\n")
          else:
            default_file = get_time.get_date(timezone,extension=".csv",directory="logs/")
            print(f"Reset default file location to {default_file}\n")

      elif settings_opt == '3': # go back to main menu
        break
  
  elif start_opt == '7' or start_opt == 'exit' or start_opt == 'quit': # Program Exit
    if len(curr_acts) > 0:
      print(f"Warning: You have {len(curr_acts)} unfinished activities which will be lost upon exiting.")
      confirm = input("Are you sure you want to quit? [Y/n] ")
      if confirm == 'n':
        print()
        continue
    
    if activities:
      confirm = input("Do you want to save the log data before exiting? [Y/n] ")
      if confirm != 'n':
        log.export_log(activities)

    print("Thanks for using TopWatch !!!\n")
    break

  else:
    print(f"{start_opt} is not a valid option.")
