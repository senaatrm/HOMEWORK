sayi=int(input("Sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")





sayi1=float(input("Birinci sayıyı girin:"))
sayi2=float(input("İkinci sayıyı girin:"))
print("Toplam:", sayi1+sayi2)
print("Fark:", sayi1-sayi2)
print("Çarpım:", sayi1*sayi2)
print("Bölüm:", sayi/sayi2)