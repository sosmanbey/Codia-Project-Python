#faktöriyel bulma
def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
    print("Faktöriyel:",faktoriyel)
    
sayý=int(input("Sayýyý Giriniz:"))
factoriel(sayý)

factoriel(7)
factoriel(6)
factoriel(5)
