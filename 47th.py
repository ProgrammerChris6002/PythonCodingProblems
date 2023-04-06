nums = [1,2,3,4,5,6,7,8,9,10]

evens = filter(lambda x: x%2 == 0, nums)
squared = map(lambda x: x ** 2, evens)

print (list(squared))



# Another Solution


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2 == 0, li))
print (list(evenNumbers))