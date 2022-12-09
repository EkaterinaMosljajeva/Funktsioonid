from math import * #* - kõik fuktsionid moodulist
#import math   math.function()

#print("Tere tulemast!") #info ekraanile väljundlause
#nimi=input("Mis sinu nimi on? ") #sisend lugemine jaoks input() ->str
#print() #tühi rida
#print(f"{nimi}, sul on väga ilus nimi!")
#print(nimi,", sul on väga ilus nimi!") #,->tühik
#print(nimi+", sul on väga ilus nimi!") #str+str
#vanus=int(input("Kui vana sa oled?")) #int(str)
#print(nimi,"sa oled",vanus,"aastat vana")
#vanus+=10
#print(nimi+", 10 aasta pärast sa oled "+str(vanus)+" aastat vana")

print()
print("Võrdse pindalaga ristkülik ja ring")
a=float(input("Anna laius: "))
b=float(input("Anna kõkgus: "))
S=a*b #-,+,*,/,**,//,%
P=2*a+2*b
d=round(sqrt(a**2+b**2),2) #ümardamine 2 numbrit koma pärast
r=sqrt(S/pi)
print(f"Pindala = {S}\nLäbimõõt = {P}\nDiagonaal = {d}")
print(f"Ringi raadius = {r}")