import csv
import get_time
import strings

labels = ['Activity', 'Start', 'End', 'Time']

def add_activity(activity_list, activity):
    activity_list.append(activity)
    return activity_list

def make_activity(name, start, end):
    #if len(name) > 50:
    #  print("Name must be less than 50 chars.")
    #  return
    time = get_time.calc_time(start, end)
    my_act = {'Activity': name, 'Start': start, 'End': end, 'Time': time}
    return my_act

def print_log(log):
  if isinstance(log, list):
    print(f'| {labels[0]:50} | {labels[1]:8} | {labels[2]:8} | {labels[3]:8}')
    bars = "--------"
    longbars = "--------------------------------------------------"
    print(f'| {longbars} | {bars} | {bars} | {bars} |')
    for act in log:
      #print('| {0:50s} | {1:8s} | {2:8s} | {3:8s} |'.format(act['Activity'], act['Start'], act['End'], act['Time']))
      print(f'| {act["Activity"]:50.50} | {act["Start"]:8} | {act["End"]:8} | {act["Time"]:8} |')

def log_to_csv(log, filename=strings.default_outfile):
  try:
    with open(filename, 'w') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=labels)
      writer.writeheader()
      for acts in log:
        writer.writerow(acts)
      print(f"Log successfully written to {filename}.\n")
  except IOError:
    print("I/O error")
