from datetime import date

tod = str(date.today())

tod = tod.split('-')
y = int(tod[0])
m = int(tod[1])
d = int(tod[2])
ud = int((input('Your birthday> ')))
um = int((input('Your birthmonth> ')))
uy = int((input('Your birthyear> ')))
a = y - uy
if um == m:
    if ud == d:
        print(f'Your are {a} years old and congrats today is your birthday.')
    elif ud < d:
        print(f'You are {a} years old.')
    elif ud > d:
        print(f'You are {a-1} years old')
else:
    if um < m:
        print(f'You are {a} years old.')
    elif um > m:
        print(f'You are {a -1} years old')
