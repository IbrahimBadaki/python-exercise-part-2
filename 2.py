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

#
from datetime import date
date1 = date(2024, 1, 1)
date2 = date(2024, 6, 15)
difference= date2 - date1
print(difference.days)
import datetime
today = datetime.datetime.today()
result = today + datetime.timedelta(days=10)
print(result)
import math
print(math.sqrt(64))
import math
print(round(math.pi, 4))
import math
print(math.ceil(7.3))
print(math.floor(7.3))
import math
print(math.pow(5, 3))
x  = min(4, 9, 1, 7, 3)
y = max(4, 9, 1, 7, 3)
print(x)
print(y)
import math
print(abs(-15))
import math
x = 6
print(math.factorial(x))
import json
data = {"name": "Alex", "age": 30}
x = json.dumps(data)
print(x)
import json
data = {"name": "Alex", "age": 30}
x = json.loads(data)
print(x["name"])
import json
data = [1, 2, 3, "four"]
json_string = json.dump(data)
print(json_string)
import json
nested_data = {
    "user":{"name" : "Alex", "job": "egineer"},
    "status": "active"
}
pretty_json = json.dumps(nested_data, indent=4)
print(pretty_json)
import json
data = {"name":"Alex", "age": 36}
with open("data.json", "w") as file:
    json.dump(data, file)
import json
data = {"name":"Alex", "age": 36}
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
    import re
    text = "Hello, World"
    match = re.serach(r"World", text)
    if match:
        print("Match found!")
    else:
        print("No match found.")
    import re
    text = "Room 42, Building 7"
    digits = re.findall(r"\d", text)
    print(digits)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               










