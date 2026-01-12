# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, " + ", b, " = ", hasil)

# operasi kurang -
hasil = a - b
print(a, " - ", b, " = ", hasil)

# operasi kali *
hasil = a * b
print(a, " * ", b, " = ", hasil)

# operasi bagi /
hasil = a / b
print(a, " / ", b, " = ", hasil)

# operasi pangkat **
hasil = a ** b
print(a, " ** ", b, " = ", hasil)

# operasi modulus %
hasil = a % b
print(a, " % ", b, " = ", hasil)

# operasi floor division //
hasil = a // b
print(a, " // ", b, " = ", hasil)

# operasi operasi, operational percedence
''' 
prioritas operasi (urutan eksekusi)
1. ()
2. exponen **
3. perkalian dan teman-teman * / ** % //
4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4 

hasil = x ** y * (z + x) / y - y % x // z
print("hasil dari ", x, "**", y, "*(", z, "+", x, ")/", y, "-", y, "%", x, "//", z, "=", hasil)

hasil = x + y * z
print("hasil dari ", x, "+", y, "*", z, "=", hasil)
# kurang akan mengambil langkah paling pertama
hasil = (x + y) * z
print("hasil dari (", x, "+", y, ")*", z, "=", hasil)