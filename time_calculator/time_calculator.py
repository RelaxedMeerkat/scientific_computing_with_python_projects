import re

weekdays_dict_str = {
  "monday" : 1,
  "tuesday" : 2,
  "wednesday" : 3,
  "thursday" : 4,
  "friday" : 5,
  "saturday" : 6,
  "sunday" : 7
}
weekdays_dict_int = {
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday",
  0: "Sunday"
}

def add_time(start, duration, day = None):

  new_time_int = parse(start + " " + duration)
  new_time_str, new_days_str, new_days_int = convert_time_to_string(new_time_int)

  if day == None:
    result = new_time_str + new_days_str
  else:
    weekday = get_new_weekday(day.lower(), new_days_int)
    result = new_time_str + ", " + weekday + new_days_str

  return result
# def end


def parse(input):
  start_hours = int(re.findall('([0-9]+):[0-9]+\s[AP]M', input)[0])
  start_minutes = int(re.findall('[0-9]+:([0-9]+)\s[AP]M', input)[0])
  day_period = re.findall('[0-9]+:[0-9]+\s([AP]M)', input)[0]
  time_start = start_hours * 60 + start_minutes
  if day_period == "PM":
    time_start += 720 # half day

  end_hours = int(re.findall('([0-9]+):[0-9]+', input)[1])
  end_minutes = int(re.findall('[0-9]+:([0-9]+)', input)[1])
  time_end = end_hours * 60 + end_minutes

  return time_start + time_end
#def end


def convert_time_to_string(input):
  new_days = input // 1440 # full day
  time_remaining = input - new_days * 1440 # full day
  
  new_hours = time_remaining // 60
  time_remaining -= new_hours * 60
  
  new_minutes = time_remaining
  
  if new_hours // 12 > 0:
    day_period = "PM"
    if new_hours != 12:
      new_hours -= 12
  else:
    day_period = "AM"
    if new_hours == 0:
      new_hours = 12

  time_str = str(new_hours) + ":" + str(new_minutes).zfill(2) + " " + day_period

  day_str = ""
  if new_days == 1:
    day_str = " (next day)"
  elif new_days > 1:
    day_str = " (" + str(new_days) + " days later)"

  return time_str, day_str, new_days
# def end


def get_new_weekday(starting_day, days_later):
  weekday_index = weekdays_dict_str[starting_day] + days_later

  weekday_index = weekday_index % 7
  
  return weekdays_dict_int[weekday_index]
# def end
