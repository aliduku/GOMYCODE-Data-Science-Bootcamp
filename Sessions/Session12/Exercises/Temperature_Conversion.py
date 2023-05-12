celsius = []
celsius.append(int(input("insert a temperature in Celsius: ")))
celsius.append(int(input("insert a temperature in Celsius: ")))
celsius.append(int(input("insert a temperature in Celsius: ")))
conversion = lambda c: (9/5)*c + 32
farenheit = list(map(conversion, celsius))
print(farenheit)