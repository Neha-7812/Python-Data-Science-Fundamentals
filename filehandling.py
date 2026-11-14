file = open("demo.txt", "w")

file.write("Welcome to Python Programming")

file.close()

file = open("demo.txt", "r")

print(file.read())

file.close()