import csv
import get_time
import strings

labels = ['Activity', 'Start', 'End', 'Time']

def add_activity(activity_list, activity):
    activity_list.append(activity)
    return activity_list

def make_activity(name, start, end):
    time = get_time.calc_time(start, end)
    my_act = {'Activity': name, 'Start': start, 'End': end, 'Time': time}
    return my_act

def print_log(log):
  if log:
    if isinstance(log, list):
      print(f'| {labels[0]:50} | {labels[1]:8} | {labels[2]:8} | {labels[3]:8}')
      bars = "--------"
      longbars = "--------------------------------------------------"
      print(f'| {longbars} | {bars} | {bars} | {bars} |')
      for act in log:
        print(f'| {act["Activity"]:50.50} | {act["Start"]:8} | {act["End"]:8} | {act["Time"]:8} |')
      print()
  else:
    print("The log is empty.\n")

def log_to_csv(log, filename=strings.default_file):
  try:
    with open(filename, 'w') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=labels)
      writer.writeheader()
      for acts in log:
        writer.writerow(acts)
      print(f"Log successfully written to {filename}.\n")
  except IOError:
    print("I/O error")

def export_log(log, prompt="Filename?: "):
  outfile = input(prompt)
  if not outfile:
    outfile = strings.default_file
  
  log_to_csv(log, outfile)
  
def csv_to_log(log, filename=strings.default_file):
  try:
    with open(filename, 'r') as data:
      for line in csv.DictReader(data):
        add_activity(log, line)
      print(f"Log successfully loaded from {filename}.\n")
  except IOError:
    print("I/O error")

def import_log(log, prompt="Filename?: "):
  infile = input(prompt)
  if not infile:
    infile = strings.default_file
  csv_to_log(log, infile)

def clear(log):
  print(f"The log has {len(log)} items.")
  confirm = input("Are you sure you want to clear? [Y/n] ")
  if confirm != 'n':
    print("Log successfully cleared\n")
    return []
  else:
    print()
    return log



