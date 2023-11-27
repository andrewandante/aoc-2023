handle = open("input.txt", "r")
data = handle.read().splitlines()
print(data) 
handle.close()