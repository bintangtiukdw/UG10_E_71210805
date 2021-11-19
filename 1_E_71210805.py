print("===== Kalkulator Akar dan Pangkat =====")
print("Pilihan menu : ")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")
Menu = float(input("\nMasukkan menu yang anda pilih : "))
if Menu >= 1 and Menu <= 3 :
    b = float(input("Masukkan bilangan yang ingin di pangkatkan : "))
else :
    print("Pilihan menu yang dimasukkan tidak sesuai!")
if Menu == 1:
    a = ("2 (Kuadrat)")
    c = 2
elif Menu == 2:
    a = ("3 (Kubik)")
    c = 3
else:
    a = ("akar kuadrat")
import math
if Menu == 1:
    Hasil = b**c
    print("Hasil dari pemangkatan bilangan %0.f" %b, "dengan", a, "adalah %0.f" %Hasil)
elif Menu == 2:
    Hasil = b**c
    print("Hasil dari pemangkatan bilangan %0.f" %b, "dengan", a, "adalah %0.f" %Hasil)
else:
    Hasil = math.sqrt(b)
    print("\nHasil", a, "dari bilangan %0.f" %b, "adalah", Hasil)



                      
