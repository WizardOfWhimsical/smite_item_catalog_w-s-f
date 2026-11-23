import json

my_dict = {"message": "Hello World"}
print(json.dumps(my_dict))











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
# with open("data.json", "a") as file:
#     json.dump(data, file)

# # read
# with open("data.json", "r") as file:
#     data = json.load(file)

# # json.dump() — Formatted / readable JSON
# with open("data.json", "w") as file:
#     json.dump(data, file, indent=4)
