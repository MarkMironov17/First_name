a = [i for i in range(1,1001)]
b = [i ** 3 for i in a]
c = sum([i // 7 for i in b])
print(c)

a = [i for i in range(1,1001)]
b = [i ** 3 for i in a]
b [:] = [i + 17 for i in b]
c = sum([i // 7 for i in b])
print(c)

