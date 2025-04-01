while True:
    n = int(input())
    if n == 0:
        break
    elif (int(str(n)[::-1])) == n :
        print("yes")
    else : print("no")


