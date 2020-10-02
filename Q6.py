naturals = [i for i in range(1,101)]
squares = [i**2 for i in range(1,101)]
sum_naturals = sum(naturals)
sum_squares = sum(squares)
print(abs(sum_squares - sum_naturals**2))