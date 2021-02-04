#module
import os
import marshal
#INI UNTUK MENGCLEAR
os.system("clear")

#INI UNTUK INPUT NAMA FILE
file = input("MASUKAN NAMA FILE NYA ~•> : ")

#Baca Isi File
baca = open(file, "r").read()

#compile file yg sudah di buat
com = compile(baca, "", "exec")

#compile file yg sudah di baca
encrypt = marshal.dumps(com)

#membuat file baru untuk hasil ecnrypt marshal
baru = open("enc"+str(file), "w")

#print kode marshal yg bisa di gunakan
baru.write("import marshal\n")
baru.write("exec(marshal.loads("+repr(encrypt)+"))")

#Jika Berhasil Ketikan
print(" [✓] FILE SUCCES ENCRYPT | file save as enc_"+str(file))

