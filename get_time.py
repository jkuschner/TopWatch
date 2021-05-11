from datetime import datetime
import pytz



def get_date_time():
  tz = pytz.timezone('US/Pacific')
  # dd/mm/YY H:M:S
  now = datetime.now(tz)
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  #print("date and time =", dt_string)

def get_time():
  tz = pytz.timezone('US/Pacific')
  # H:M:S
  now = datetime.now(tz)
  t_string = now.strftime("%H:%M:%S")
  #print("time =", t_string)
  return t_string

def calc_time(start, end):
  start_list = start.split(':')
  end_list = end.split(':')

  start_list = list(map(int, start_list))
  end_list = list(map(int, end_list))

  # convert each time into seconds
  start_seconds = 3600 * start_list[0] + 60 * start_list[1] + start_list[2]
  end_seconds = 3600 * end_list[0] + 60 * end_list[1] + end_list[2]

  # in case time rolled over the day
  if start_seconds > end_seconds:
    start_seconds = start_seconds - (3600 * 24)

  # take difference and convert back to H, M, S
  elapsed_seconds = end_seconds - start_seconds
  elapsed_list = []
  elapsed_list.append(int(elapsed_seconds / 3600))
  elapsed_seconds = elapsed_seconds - elapsed_list[0] * 3600
  elapsed_list.append(int(elapsed_seconds / 60))
  elapsed_seconds = elapsed_seconds - elapsed_list[1] * 60
  elapsed_list.append(elapsed_seconds)

  # format output string
  elapsed_list = list(map(str, elapsed_list))
  e_string = elapsed_list[0] + ':' + elapsed_list[1] + ':' + elapsed_list[2]
  #print(e_string)
  return e_string

