Suhu = float(input("\nMasukkan suhu tubuh Anda : "))
if Suhu > 50 :
    print("Anda bukan Manusia :)")
elif Suhu < 32 :
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif Suhu > 37.5 and Suhu <= 50 :
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
else :
    print("Suhu Anda normal!")
