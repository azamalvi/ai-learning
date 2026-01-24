import json

with open("sample.json", "r") as file:
    data = json.load(file)
    print(data.get("name"))

# print(json.dumps(data, indent=2))

with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("Goodbye!\n")

with open("sample.txt", "r")  as file:
    content = file.read()
    print(content)


data = {"name": "Azam", "role": "AI Engineer"}

with open("user.json", "w") as f:
    # it will convert python object to json string and write to file
    json.dump(data, f)

with open("user.json", "r") as f:
    loaded = json.load(f)

print(loaded)