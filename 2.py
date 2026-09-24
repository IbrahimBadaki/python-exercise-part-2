#this shows the year, month, day, hour, minute, and microsecond.
import datetime
print(datetime.datetime.now())

#this shows the exact year, month, and day.
import datetime
print(datetime.datetime(2024, 9, 9))

#this shows day of month, number of month, full version of year.
import datetime
now = datetime.datetime.now()
result = now.strftime("%D-%m-%Y")
print(result)

#this shows full version of weekday.
import datetime
now = datetime.datetime(2023, 9,  5)
result = now.strftime("%A")
print(result)

#this shows the number of days between these dates.
from datetime import date
date1 = date(2024, 1, 1)
date2 = date(2024, 6, 15)
difference= date2 - date1
print(difference.days)

#this shows current date and time and represents 10 days.
import datetime
today = datetime.datetime.today()
result = today + datetime.timedelta(days=10)
print(result)

#used to find square root of 64
import math
print(math.sqrt(64))

"""this returns the value of PI(3.14)
and round it to 4 decimal points"""
import math
print(round(math.pi, 4))

#math.ceil  rounds a number upwards to nearest integer.
#math.floor rounds a number downwards to nearest integer
import math
print(math.ceil(7.3))
print(math.floor(7.3))

#it raises the value of 5 to power 3.
import math
print(math.pow(5, 3))

#it show the highest and lowest value in an iterable.
x  = min(4, 9, 1, 7, 3)
y = max(4, 9, 1, 7, 3)
print(x)
print(y)

#it returnsd the absolute value of the number.
import math
print(abs(-15))

#it shows the factorial of the number.
import math
x = 6
print(math.factorial(x))


#json.dumps() takes a dictionary into the formatted JSON strings.
import json
data = {"name": "Alex", "age": 30}
x = json.dumps(data)
print(x)

#json.loads expect the JSON string to convert back to python objects.
import json
data = {"name": "Alex", "age": 30}
x = json.loads(data)
print(x["name"])

"""json.dumps() requires two arguments;
1.to open the file pointer
2.to convert a string without using a file"""
import json
data = [1, 2, 3, "four"]
json_string = json.dump(data)
print(json_string)

#Passing the indent=4 into an argument to json.dumps()
import json
nested_data = {
    "user":{"name" : "Alex", "job": "egineer"},
    "status": "active"
}
pretty_json = json.dumps(nested_data, indent=4)
print(pretty_json)

#json.dumps() converts the Python dictionary and writes it directly into the file object.
import json
data = {"name":"Alex", "age": 36}
with open("data.json", "w") as file:
    json.dump(data, file)

#json.loads() reads and converts the json content back to dictionary.
import json
data = {"name":"Alex", "age": 36}
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
   
#regex search
    import re
    text = "Hello, World"
    match = re.search(r"World", text)
    if match:
        print("Match found!")
    else:
        print("No match found.")
    
#regex find digits
    import re
    text = "Room 42, Building 7"
    digits = re.findall(r"\d", text)
    print(digits)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               










