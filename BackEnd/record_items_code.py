import json

# my_dict = {"message": "Hello World"}
# print(json.dumps(my_dict))

fake_item = {
  "id": "uuid",
  "cost": "items_cost_is_int",
  "name": "Rage",
  "stats":{"strength": 30, "critical_hit": "20%"},
  "effect":{"type":"stack", "description":"5/god kill 1/assist or jungle boss. 1 stack = 2%% crit | 3 strength. At 10 stacks Rage evolves 15%% to crit and 35 to strength"}
}


file_path = "BackEnd/file.json"
# append
# this opens reads data to a varailable then new dict added to the end
# of the list so that we can write the data back to the file
try:
  with open(file_path, "r+") as file:
    current_data = json.load(file)
    print(current_data)
    current_data.append(fake_item)
    print(current_data)
    file.seek(0)
    file.truncate()
    json.dump(current_data, file, indent=4)
except Exception as e:
  print(e)
  print("Something went wrong with the save")


# with open("data.json", "a+") as file:
#     json.dump(item, file, indent=4)









# Flag  Action
# "w"   Write (creates or overwrites).
# "a"   Append (adds to existing content).
# "r"   Read

# Method           | Purpose
# json.dump()	   | Python object → JSON file
# json.dumps()	   | Python object → JSON string
# json.load()	   | JSON file → Python object
# json.loads()	   | JSON string → Python object
# file.write()	   | Write string to file
# file.writelines()| Write iterable of strings to file
# item_name = input("item name")

# stats = input("stats")
# while stats != "q":
#     stats = input(" additional stats")

# effects = input("what kind of effect").split()
# while effects != "q":
#     effects = input("what kind of effect").split()
# data = {"item_name": item_name, "stats": stats, "effects": effects}

# # if yes on previous promt trigger next step
# #
# # write
# with open("data.json", "w") as file:
#     json.dump(data, file)

# # append
# with open("data.json", "a+") as file:
#     json.dump(data, file, indent=4)

# # read
# with open("data.json", "r") as file:
#     data = json.load(file)

# # json.dump() — Formatted / readable JSON
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
