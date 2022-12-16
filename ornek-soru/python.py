import math

def hesapla_hipotenus(a, b):
  return math.sqrt(a**2 + b**2)

# Örnek kullanım
hipotenus = hesapla_hipotenus(3, 4)
print(hipotenus)  # 5.0

hipotenus = (a**2 + b**2)**0.5
a = 3
b = 4
c = 0

while c**2 != a**2 + b**2:
  c += 0.001

print(c)  # 5.0
