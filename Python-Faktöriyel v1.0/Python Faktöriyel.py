#fakt�riyel bulma
def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
    print("Fakt�riyel:",faktoriyel)
    
say�=int(input("Say�y� Giriniz:"))
factoriel(say�)

factoriel(7)
factoriel(6)
factoriel(5)
