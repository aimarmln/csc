# TIPE DATA

this_is_integer = 10 # integer
this_is_float = 3.14 # float
this_is_string = "hello world" # string
this_is_boolean = True # boolean

# list []
# - seperti konsep array
# - dapat diubah isinya
# - data kesatu berada pada index 0 dan seterusnya
# - pengaksesan value: variable_name[index]
this_is_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# tuple ()
# - sama seperti list
# - tetapi isi value tidak dapat diubah
# - pengaksesan value: variable_name[index]
this_is_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# dictionary {}
# - kumpulan nilai yang terdiri dari key dan value
# - pengaksesan value: variable_name[key]
this_is_dictionary = {
    "name": "aimar",
    "age": 18
}

print(type(this_is_boolean)) # mengecek tipe data: type()


# OPERATOR

# operator aritmatika
# + = penjumlahan
# - = pengurangan
# * = perkalian 
# / = pembagian
# ** = pangkat
# % = modulus
a = 5 * 3
print(a)

# operator assignment
# = : x = y
# += : x += y => x = x + y
# -= : x -= y => x = x - y
# *= : x *= y => x = x * y
# /= : x /= => x = x / y
a += 5
print(a)

# operator perbandingan
# == : sama dengan
# != : tidak sama dengan
# > : lebih besar dari
# < : kurang dari
# >= : lebih besar sama dengan
# <= : kurang dari sama dengan
print(a < 10)

# operator logika
# and : dan
# or : atau
# not : kebalikan

print(not(5 > 7))