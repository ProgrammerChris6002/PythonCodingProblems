def cube_sum (num) :
    total = 0

    for i in range (num+1) :
        total += i ** 3

    
    return total



print (cube_sum (2))
print (cube_sum (3))
print (cube_sum (4))
print (cube_sum (5))
print (cube_sum (6))




# Alternative Solution



n = int (input ('Enter a number: '))
sum = (n * (n+1) / 2) ** 2
print ('Your sum of cubes are: ', sum)