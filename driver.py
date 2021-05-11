import log
import get_time
import strings

activities = [] # A list of dictionaries that represent each individual activity
curr_acts = []  # A list of pairs that contain activity names(1) and their start time(2) as strings
                #   that represent unfinished activities

def getMenuInput(prompt_message):
  while True:
    try:
      option = int(input(prompt_message))
      return option
    except ValueError:
      print("Input must be number.")
      continue

print("Welcome to ActivityLogger!!!")

while True:
  print(strings.start_menu + "\n")
  start_opt = getMenuInput("What's it gonna be bucko? ")

  """
  while True:
    try:
      option = int(input("What's it gonna be bucko? "))
      break
    except ValueError:
      print("Input must be a number.")
      continue
  """
  print('\n')

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
      print("Which activity do you want to end?\n")
      for i, act in enumerate(curr_acts):
        print(f"[ {i} ] {act[0]}")
        
      ending_option = getMenuInput("Which one?: ")
      
      ending_name = curr_acts[ending_option][0]
      ending_start = curr_acts[ending_option][1]

      activities = log.add_activity(activities, log.make_activity(ending_name, ending_start, get_time.get_time()))
      del curr_acts[ending_option]

      
    
  elif start_opt == 2: # Print the log
    log.print_log(activities)
  else:
    print(start_opt)
    print("Congrats, you're a retard.\n")
