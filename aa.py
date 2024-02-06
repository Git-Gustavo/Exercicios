terminou = False
p = 0
i = 0
while not terminou:
    n = int(input("digite"))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

    print("p = ", p)
    print("I = ", i)
