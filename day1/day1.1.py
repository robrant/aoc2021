
f = open("./day1_input.txt", "r")

counter = 0
records = [int(i) for i in f.readlines()]

for i in range(len(records)-1):
    this_val = records[i]
    next_val = records[i+1]
    diff = next_val - this_val
    if diff > 0:
        counter += 1

print(counter)    
    