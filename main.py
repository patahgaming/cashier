import csv

hargas = []
barangs = []
harga = int
barang = str
total = 0
#fungsi tulis digunakan untung membuat list barang dan harga
def tulis():
    with open('barang.csv','+a' ,newline='') as file:
        tulis = csv.writer(file)
        barang = input("Masukan barang yang dijual: ")
        barang = barang.capitalize()
        harga = int(input("Masukan harga barang: "))
        tulis.writerow([barang,harga])


while 1:
    barang = input("Masukan nama barang(tekan Q untuk keluar): ")
    if barang.lower() =="q":
        break
    with open('barang.csv') as file:
        baca = csv.reader(file)
        ribet = []
        for baris in baca:
            ribet += [baris]
        barang = barang.capitalize()
        found = False

        for row in ribet:
            if barang in row:
                found = True
                target_row = row
                break

        if found:
            print(target_row)
            harga = target_row[1:2:]
            barang = target_row[0:1:]
            harga = int(harga[0])
            barang = str(barang[0])
            #print(barang)
            #print(harga)
            hargas.append(harga)
            barangs.append(barang)
            print(barangs)
            print(hargas)

        else:
            print("barang salah")
for harga in hargas:
    total += harga
JB = total
MEM = str(input("Apakah member?(Y/n):"))
MEM = MEM.lower()
if JB >= 100000.0:
    PeBY = "10%"
    JBB = JB-JB*10/100
elif JB >= 50000.0:
    PeBY = "5%"
    JBB = int(JB-JB*5/100)
else:
    PeBY = "Anda tidak mendapatkan Diskon"
    JBB = "Total belanja anda menjadi Rp"+str(int(JB))+",00"
if MEM == "y":
    if PeBY == "Anda tidak mendapatkan Diskon":
        PeBY = "2%"
        JBB = JB-JB*2/100
    else:
        PeBY = f"{PeBY} + 2%"
        JBB = JBB-JBB*2/100
if PeBY == "Anda tidak mendapatkan Diskon":
    print(PeBY)
    print("Total belanja anda menjadi Rp"+str((JBB))+",00")
else:
    print(f"Anda mendapatkan diskon sebesar {PeBY}")
    print("Total belanja anda menjadi Rp"+str((JBB))+",00")


                        ##############################
                        ######copywrite by NaNas######
                        #############XRPL#############