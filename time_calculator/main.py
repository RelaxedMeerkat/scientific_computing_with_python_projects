from time_calculator import add_time

# Arguements:
# start: count from this time
# duration: add this amount of time
# weekday (optional): start from this weekday
result = add_time("11:59 PM", "24:05", "Tuesday")

print(result) # prints: "12:04 AM, Thursday (2 days later)"
