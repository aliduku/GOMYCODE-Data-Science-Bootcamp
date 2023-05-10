numbers = []
numbers.append(int(input("insert a number: ")))
numbers.append(int(input("insert a number: ")))
numbers.append(int(input("insert a number: ")))
conversion = lambda n: n*n*n
cubes = list(map(conversion, numbers))
result = list(zip(numbers, cubes))
print(numbers)
print(cubes)
print(result)