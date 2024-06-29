import math

x1 = int(input("bir sayı giriniz: "))
y1 = int(input("bir sayı giriniz: "))
x2 = int(input("bir sayı giriniz: "))
y2 = int(input("bir sayı giriniz: "))

euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Minimum Öklid Mesafesi: {euclidean_distance}")
