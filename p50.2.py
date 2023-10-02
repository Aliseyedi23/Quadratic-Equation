def delta(a,b,c):
    delta=(b**2)-4*a*c
    return delta

def solve (a,b,c):
    d=delta(a, b, c)
    if d == 0 :
        x1=x2= -b/(2*a)
        return x1 , x2
    elif d < 0:
        return 'no root!!'
    else:
        x1=-b+(d**0.5)
        x2=-b-(d**0.5)
        return x1 , x2

Coefficient1 = float(input('enter ..a.. Coefficient :'))
Coefficient2 = float(input('enter ..b.. Coefficient :'))
Coefficient3 = float(input('enter ..c.. Coefficient :'))

if delta(Coefficient1, Coefficient2, Coefficient3) >=0:
    x1,x2 = solve(Coefficient1,Coefficient2,Coefficient3)
    print('root1 :',x1 ,'and','root2 :',x2)
else :
    message = solve(Coefficient1,Coefficient2,Coefficient3)
    print(message)


