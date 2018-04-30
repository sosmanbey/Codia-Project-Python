#girilen sayıya kadar olan asal sayılar
n=int(input("Bir sayı giriniz: "))
for i in range(2,n+1,1):
    s=0
    for j in range (1,i+1,1):
        if i%j==0:
            s=s+1
    if s==2:
        print(i)

input()
