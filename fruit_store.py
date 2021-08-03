fruit=input().lower().strip()

#Product count
ac=fruit.count('a')
bc=fruit.count('b')
cc=fruit.count('c')
dc=fruit.count('d')

#logic section
if ac>=4 or cc>=6:
    rcc=cc//6
    rc=cc%6
    raa = ac//4
    ra=ac%4
    total =100*raa+ra*35+250*rcc+rc*50+bc*65+dc*85
    print("{:.2f}".format(total))
else:
    total = ac*35+bc*65+cc*50+dc*85
    print("{:.2f}".format(total))