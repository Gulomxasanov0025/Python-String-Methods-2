# Matnda ma’lum bir so‘zning boshlanish pozitsiyasini topish index() orqali Python so‘zi qayerdan boshlanganini topish.
text = input("Matnni kiriting: ")
word = input("Qidirilayotgan so'zni kiriting: ")

indeks = text.find(word)

if indeks != -1:
    print(f"\"{word}\" so'zi {indeks}-indekstdan boshlanadi.")
else:
    print("So‘z topilmadi.")