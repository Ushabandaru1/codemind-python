def printRoman(num):
    n=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symb=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i=12
    while num:
        div=num//n[i]
        num%=n[i]
        while div:
            print(symb[i],end="")
            div-=1
        i-=1
num=int(input())
printRoman(num)