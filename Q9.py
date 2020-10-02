for i in range(1,1001):
    for j in range(1,1001):
        square = (i**2+j**2)**0.5
        if int(square) == square:
            if i+j+square == 1000:
                print(i*j*square)