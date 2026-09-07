operator = str(input('Pilih operator penambahan, pengurangan, perkalian, atau pembagian: '))
nomor1 = int(input("Masukkan angka pertama: "))
nomor2 = int(input("Masukkan angka kedua: "))


if operator == 'penambahan':
  res = nomor1 + nomor2
elif operator == 'pengurangan':
  res = nomor1 - nomor2
elif operator == 'perkalian':
  res = nomor1 * nomor2
elif operator == 'pembagian':
  res = nomor1 / nomor2


print(f'{operator} dari {nomor1} dan {nomor2} adalah {res}')