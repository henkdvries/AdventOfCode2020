with open('data.txt', 'r') as reader:
    routemap = reader.read().splitlines().split()

print(routemap)
