from typing import Counter


nombre = input('ingrese su nombre')
Count=0
vocales =("a","e","i","o","u")

for item in nombre:
  if item in vocales:
    Count+=1
    print(f"{nombre} tiene {item} vocal")
  else:
    print("Intenta denuevo")


if Count>=3:
  print(nombre)
