from datetime import datetime, timedelta , timezone
import time

# current time

def current_datetime():
    now = datetime.now()

    print("Current Date & Time : ",now)
    print("Year: ", now.year)
    print("Month: ", now.month)
    print("Day: ", now.day)
    print("Hour: ",now.hour)
    print("Minute:", now.minute)
    print("Second:", now.second)
    
#current_datetime()


#Current Time in Seconds

def time_seconds():
    seconds = time.time()

    print("Second since 1 jan 1970", seconds)

#time_seconds()


# Date & Time Formatting

def format_datetime():

    now = datetime.now()

    print("DD-MM-YYYY: ", now.strftime("%d-%m-%y"))
    print("MM/DD/YYYY: ", now.strftime("%m/%d/%y"))
    print("12 - hours: ", now.strftime("%I : %M : %S : %p"))
    print("24 - hours: ", now.strftime("%H:%M:%S"))

#format_datetime()


# Number of Days Between two Dates

def date_diffrence():

    start_date = input("Enter start date (yyyy-mm-dd): ")
    end_date = input("Enter end date (yyyy-mm-dd):")

    date1 = datetime.strptime(start_date, "%Y-%m-%d")
    date2 = datetime.strptime(end_date, "%Y-%m-%d")

    days = abs((date2 - date1).days)
    print("Total day: ",days)

date_diffrence()

# UTC and Local time

def utc_local_time():
  utc_time = datetime.now(timezone.utc)
  local_time = datetime.now()

  print(utc_time)
  print(local_time)

utc_local_time()


















