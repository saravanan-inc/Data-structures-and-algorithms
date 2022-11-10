class Patterns:
    def Pattern1(n):
        for i in range(n):
            for j in range(n):
                print("* ", end="")
            print("")

    def Pattern2(n):
        for i in range(n+1):
            for j in range(i):
                print("* ", end="")
            print("")

    def Pattern3(n):
        for i in range(n+1):
            for j in range(n+1-i, 1, -1):
                print("* ", end="")
            print("")

    def Pattern4(n):
        for i in range(n+1):
            for j in range(1, i+1):
                print(j, end="")
            print("")

    def Pattern5(n):
        for i in range(2*n):
            col = i
            if i > n:
                col = n - (i-n)
            for j in range(col):
                print("* ", end="")
            print("")

    def Pattern6(n):
        for i in range(2*n):
            col = i
            if i > n:
                col = n - (i-n)

            for space in range(n-col):
                print("", end=" ")

            for j in range(1, col):
                print("* ", end="")
            print("")


p = Patterns
p.Pattern1(5)
p.Pattern2(5)
p.Pattern3(5)
p.Pattern4(5)
p.Pattern5(5)
p.Pattern6(5)
