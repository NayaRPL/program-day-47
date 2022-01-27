def luas_persegi(sisi):
    return sisi*sisi
print("luas persegi dari sisi 4 :",luas_persegi(4))

def luas_persegi1(sisi):
    print(sisi*sisi)
luas_persegi1(4)

def luas_persegi(sisi):
    return sisi*sisi
luas_persegi_besar=luas_persegi(100)
luas_persegi_kecil=luas_persegi(50)
print("luas_persegi_besar:",luas_persegi_besar)
print("luas_persegi_kecil:",luas_persegi_kecil)
print("jumlah keseluruhan dari kedu persegi tersebut adalah:",luas_persegi_besar+luas_persegi_kecil)

def ciri_seseorang(nama,kulit,mata=2):
    print("namanya adalah",nama,"dan berkulit",kulit,"dan mempunyai",mata,"panca indra")
ciri_seseorang("naya","putih")

def ciri_seseorang(nama,kulit="sawo_matang",mata=2):
    print("namanya adalah",nama,"dan berkulit",kulit,"dan mempunyai",mata,"panca indra")
ciri_seseorang("naya",kulit="gelap")

def luas_segitiga(alas,tinggi):
    if alas != tinggi and alas < tinggi :
        return alas * tinggi / 2
    return False
ini_luas=luas_segitiga(11,10)
print(ini_luas)

def luas_segitiga(alas,tinggi):
    if alas != tinggi and alas < tinggi :
        return alas * tinggi / 2
    return False                    #ini sama dengan dari fungsi break di dalam prulangan for dan while
print("jumlah luas dari segitiga adalah",luas_segitiga(5,10))

kota="majene"  
def hello ():
    kota="mamuju"
    print(kota)
print("panggil fugsi hello ()")
hello()
print("panggil fungsi tdk langsung")
print(kota)


list=[1,2,3,4]
list.append(5)
print(list)

data=[1,2,3,4]
data1=int(input("masukkan data1:"))
for nilai in data:
    if data1==nilai:
        break
    print("data yang ada ",nilai)
else:
        print("data yang anda masukkan tidak terdapat dalam data list")
