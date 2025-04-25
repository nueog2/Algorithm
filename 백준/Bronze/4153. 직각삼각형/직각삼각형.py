while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    elif a*a == (b*b + c*c) or b*b == (a*a + c*c) or c*c == (b*b + a*a):
        print('right')
    else: print('wrong')