'''
x is having 1 lakh in his bank acnt, rate of
interest is 12% pa. in the 5 mnth,x is wdrwing
25k rs in order to buy a gift for jis loved_1
in the 9 month 10k is dep. in his acnt by his
2_loved one.end of financial year..hw much is
x having in his yr(march 31st)
note:simple interest.
'''

n=100000
z=((n)*1/100)*4
n=n-25000
print(n)
k=((n)*1/100)*4
n=n+10000
d=((n)*1/100)*4
print(n)
print(n+k+d+z)
def calculate(PA,roi,month):
    z=0
    while (month<=12):
        interest = 0.01*PA
        z=z+interest
        if (month == 4):
            PA = PA - 25000
        elif month == 8:
            PA = PA + 10000
        month+=1
        pa = PA
    return z,pa

    
PA= 100000
roi = 1
month=1
a,pa = calculate(PA,roi,month)
print(pa+a)
