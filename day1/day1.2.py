
f = open("/Users/rich/Projects/aoc2021/day1/day1_input.txt", "r")

counter = 0
records = [int(i) for i in f.readlines()]

# Note: stop the iteration 3 from the end to account for the i+4
for i in range(len(records)-3):
    this_val = sum(records[i:i+3])
    next_val = sum(records[i+1:i+4])
    diff = next_val - this_val
    if diff > 0:
        counter += 1

print(counter)