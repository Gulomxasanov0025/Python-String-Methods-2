# Belgilarni qayerdan boshlab qidirishni aniqlang find() metodiga start pozitsiyasi bilan ishlash.  :) 

text = input("Matnni kiriting: ")
word = input("Qidirilayotgan so'zni kiriting: ")

start = int(input("Qayerda boshlab qidirilsin: " ))

index = text.find(word,start)

print(index)