import log
import get_time
import strings
import csv

activities = [] # A list of dictionaries that represent each individual activity
curr_acts = []  # A list of pairs that contain activity names(1) and their start time(2) as strings that represent unfinished activities

def getMenuInput(prompt_message):
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
  with open(strings.default_file,'r') as data:
    for line in csv.DictReader(data):
      log.add_activity(activities,line)
    print("Successfully loaded log data\n")
except IOError:
  print("No log data to load\n")

    
print(strings.startup_message + "\n")

while True:
  printMenuOptions(strings.start_menu_options, strings.start_menu_prompt)

  start_opt = getMenuInput("Choose a menu option: ")

  print()

  if start_opt == 0: # Start a new activity
    name = input("What are you going to do?(<50 chars): ")
    curr_acts.append((name, get_time.get_time()))
    print('Good Luck!\n')


  elif start_opt == 1: # End an activity
    if len(curr_acts) < 1:
      print("You can't end an activity without starting one first.\n")
    elif len(curr_acts) == 1:
      activities = log.add_activity(activities, log.make_activity(curr_acts[0][0],curr_acts[0][1],get_time.get_time()))
      print(f'Nice job finishing {curr_acts[0][0]}\n')
      del curr_acts[0]
    else:
      printMenuOptions(curr_acts, strings.end_activity_prompt)
        
      ending_option = getMenuInput("Which one?: ")
      
      ending_name = curr_acts[ending_option][0]
      ending_start = curr_acts[ending_option][1]

      activities = log.add_activity(activities, log.make_activity(ending_name, ending_start, get_time.get_time()))
      print(f'Nice job finishing {curr_acts[ending_option][0]}\n')
      del curr_acts[ending_option]

      
    
  elif start_opt == 2: # Print the log
    if activities:
      log.print_log(activities)
      print()
    else:
      print("The log is empty.\n")
  
  elif start_opt == 3: # Export to csv
    outfile = input("Filename?: ")
    if not outfile:
      outfile = strings.default_file

    log.log_to_csv(activities, outfile)
    confirm = input("Do you want to clear the current log? [Y/n] ")
    if confirm != 'n':
      activities = []
      print("The log has been cleared\n")
    else:
      print()

  elif start_opt == 4: # Import from csv
    infile = input("Filename?: ")
    if not infile:
      infile = strings.default_file

    log.csv_to_log(activities, infile)
  
  elif start_opt == 5: # Program Exit
    if len(curr_acts) > 0:
      print(f"Warning: You have {len(curr_acts)} unfinished activities which will be lost upon exiting.")
      confirm = input("Are you sure you want to quit? [Y/n] ")
      if confirm == 'n':
        print()
        continue
    
    if activities:
      confirm = input("Do you want to save the log data before exiting? [Y/n] ")
      if confirm != 'n':
        outfile = input("Filename?: ")
        if not outfile:
          outfile = strings.default_file
        log.log_to_csv(activities, outfile)

    print("Thanks for using TopWatch !!!\n")
    break

  else:
    print(start_opt)
    print("Congrats, you're a retard.\n")
