from datetime import date

# data yang dimasukan pasti string
data =  input("masukan nama: ")
print('data = ', data, ',type = ', type(data))

# data yang dimasukan pasti string 
tempat =  input("masukan tempat: ")
print('data = ', tempat, ',type = ', type(tempat))

# tipe data date untuk memunculkan tanggal,bulan,tahun
tanggal_input = input("masukan tanggal lahir: (format: YYYY-MM-DD) ")
tahun,bulan,hari = map(int, tanggal_input.split('-'))
tanggal_lahir = date(tahun, bulan, hari) # membuat objek date langsung
print('data = ', tanggal_lahir, ',type = ', type(tanggal_lahir))

# data yang dimasukan pasti string 
alamat =  input("masukan alamat: ")
print('data = ', alamat, ',type = ', type(alamat))

# data yang dimasukan pasti string 
asal_sekolah =  input("masukan asal sekolah: ")
print('data = ', asal_sekolah, ',type = ', type(asal_sekolah))

# meminta input float dari user
jarak = float(input("masukan jarak rumah ke sekolah (km): "))

print(f"Jarak: {jarak} km")
print(f"Type: {type(jarak)}") # class 'float'

# data yang dimasukan pasti string 
pekerjaan_ayah =  input("masukan pekerjaan ayah: ")
print('data = ', pekerjaan_ayah, ',type = ', type(pekerjaan_ayah))

# jika kita ingin mengambil integer, maka
gaji_ebes = int(input("masukan gaji ebes: "))
print('data = ', gaji_ebes, ',type = ', type(gaji_ebes))

# data yang dimasukan pasti string 
pekerjaan_ibu =  input("masukan pekerjaan ibu: ")
print('data = ', pekerjaan_ibu, ',type = ', type(pekerjaan_ibu))

# jika kita ingin mengambil integer, maka
gaji_ibuk = int(input("masukan gaji ibuk: "))
print('data = ', gaji_ibuk, ',type = ', type(gaji_ibuk))