a = float(input("\nMasukkan bilangan 1 : "))
b = float(input("Masukkan bilangan 2 : "))
c = float(input("Masukkan bilangan 3 : "))
if a <= b and b <= c :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %a, "%0.f" %b, "%0.f" %c)
elif c <= b and b <= a :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %c, "%0.f" %b, "%0.f" %a)
elif b <= a and a <= c :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %b, "%0.f" %a, "%0.f" %c)
elif b <= c and c <= a :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %b, "%0.f" %c, "%0.f" %a)
elif a <= c and c <= b :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %a, "%0.f" %c, "%0.f" %b)
elif c <= a and a <= b :
    print("\nUrutan bilangan dari yang terkecil adalah %0.f" %c, "%0.f" %a, "%0.f" %b)
