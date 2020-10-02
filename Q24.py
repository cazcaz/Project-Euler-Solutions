#To work out which digit will be first, work out how many cycles of the remaining numbers have passed
#If you have n numbers then there will be (n-1)! permutations before the first digit changes
#To work out the remaining numbers, do the same with the n-1 remaining numbers

def factorial(x):
    if x== 0:
        return 1
    temp=1
    while x !=1:
        temp = temp * x
        x-=1
    return temp

numbers = [i for i in range(0,10)]
print(factorial(len(numbers)), "possible combinations of", numbers)
position = 1000000
combination = []
original_length=len(numbers)
remainder = position-1
for i in range(1,original_length):
    cycled = remainder//factorial(original_length-i)
    remainder = remainder%factorial(original_length-i)
    combination.append(numbers[cycled])
    numbers.remove(numbers[cycled])

print("The", str(position) + "th lexicographic permutation is", combination + numbers)

