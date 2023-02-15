import os
import sys

class elanqoyy:
    def __init__(self):
        self.salam = []

    def eylansaxla(self):
        name = input("Marka: ")
        tipi = input("Növü: ")
        batarya = input("Batarya: ")
        color = input("Rəngi: ")
        kamera = input("Əsas Kamerası: ")
        ram = input("RAM: ")
        yaddas = input("Yaddaşı: ")
        prosessor = input("Prasessor: ")
        qiymet = input("Qiyməti: ")
        try:
         with open(input("Yaradılacaq not adını daxil et: "),"x") as file:
            file.write(f"Markası: {name}\nNövü: {tipi}\nBataryası: {batarya}\nRəngi: {color}\nKamerası: {kamera}\nRAM: {ram}\nYaddaşı: {yaddas}\nPrasessor: {prosessor}\nQiyməti: {qiymet}\n------------------------\n")

            print("Not yaradıldı")
            elanqoy2 = {"marka": name, "növü": tipi, "batarya": batarya, "rəngi": color, "kamera": kamera, "ram": ram, "yaddas": yaddas, "prosessor": prosessor, "qiymeti": qiymet,}
            self.salam.append(elanqoy2)
            print("Elanınız saxlanıldı!")
        except:
            print("Bu adlı not var!")
            print("Not adı eyni olduğu üçün elanınız saxlanılmadı!")  
if (sys.argv[1] == "elan" and sys.argv[2] == "yarat"):
    elan = elanqoyy()
    elan.eylansaxla()
elif sys.argv[1] == "elan" and sys.argv[2] == "sil":
    try:
        name = input("Silinəcək elan adını daxil et: ")
        os.remove(name)
        print(f"{name} Adli elan silindi!")
    except:
        print("Belə not yoxdur!")


