a = ("Процент")
b = ("Процента")
c = ("Процентов")
n = [i for i in range(1,101)]
numbs = {11,12,13,14}
for n in range(100):
    n = n + 1
    if n in numbs:
        print(n, "процентов")
    elif n % 10 == 1:
        print(n, "процент")
    elif n % 10 > 1 and n % 10 <5:
        print(n, "процента")
    else:
        print(n, "процентов")