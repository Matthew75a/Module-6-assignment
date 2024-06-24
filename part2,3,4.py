from datetime import datetime, timedelta

#part2
now = datetime.now()
print("Current datetime:", now)

now_plus_day = now + timedelta(days=1)
print("After adding 1 day:", now_plus_day)

now_minus_60 = now - timedelta(seconds=60)
print("After subtracting 60 seconds:", now_minus_60)

now_plus_2yr = now.replace(year=now.year + 2)
print("After adding 2 years:", now_plus_2yr)

#part3
d = timedelta(days=100, hours=10, minutes=13)
print(d)
print("Days:", d.days, "Seconds:", d.seconds, "Microseconds:", d.microseconds)

#part4
def get_current_datetime():
    return datetime.now()

def feet_and_inches(feet, inches):
    current_datetime = get_current_datetime()
    print("Current DateTime:", current_datetime)
    print("Feet:", feet, "Inches:", inches)
    print('Type :- ', type(current_datetime))

feet_and_inches(5, 8)
