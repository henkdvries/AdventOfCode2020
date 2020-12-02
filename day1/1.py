with open('data.txt', 'r') as reader:
    ints = reader.readlines()

ints = [int(i) for i in ints] 
ints = sorted(ints)
quicksrc = set(ints)

for item in ints:
    mask = 2020-item
    if(mask in quicksrc):
        print(item)
        print(mask)
        print(mask*item)


