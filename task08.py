# Bir so‘z bir necha marta qatnashgan bo‘lsa, birinchi indeksni toping Faqat birinchi topilgan joyni chiqarish.

text = input("Matnni kiriting: ")
word = input("Qidirilayotgan so'zni kiriting: ")

print("1-topilgan natija : " ,text.find(word))

print("oxirgi topilgan  natija: " ,text.rfind(word))

print("Nechi marta qatnashgan : ",text.count(word))
