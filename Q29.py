numbers = set()

for a in range(2,6):
    for b in range(2,6):
        numbers.add(a**b)

print(len(numbers))