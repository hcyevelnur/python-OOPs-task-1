import os
import sys

class tapaz:
    miqdari = "10 ədəd" 
    satilib = "40 ədəd"

    def __init__(self, name, tipi, ram, Prosessor, Yaddaş, color, kredit, videokart, kamerasi, battery, sale, ayliq):
        self.name = name
        self.tipi = tipi
        self.ram = ram
        self.Prosessor = Prosessor
        self.Yaddaş = Yaddaş
        self.color = color
        self.kredit = kredit
        self.videokart = videokart
        self.kamerasi = kamerasi
        self.battery = battery
        self.sale = sale
        self.ayliq = ayliq

    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("RAM: {}".format(self.ram))
        print("Prosessor: {}".format(self.Prosessor))
        print("Videokart: {}".format(self.videokart))
        print("Batarya: {}".format(self.battery))
        print("Ön kamera: {}".format(self.kamerasi))
        print(f"Kredit: {self.kredit}")
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        # print("Endirim: {}".format(self.e))
        print(f"Qiymət: {self.sale} AZN")




    def get_info(self):
        print(f"Hazırda stokda {self.name} markalı komputer mövcuddur.")

    def get_sale(self):
        if self.sale == 12:
            print(self.sale//12)
        elif self.sale == 24:
            print(self.sale//24)
        elif self.sale == 18:
            print(self.sale//18)

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 200} AZN")

asus = tapaz("Asus", "Notebook","4 GB", 'Intel Core I5',"512 GB SSD", 'Qara','Var', '6 GB', '18 MP', "6500 mAh", 2400, 12)
apple = tapaz("Apple", "Macbook","8 GB", 'M1',"518 GB SSD", 'Gray','Var', '4 GB', '12 MP', "9500 mAh", 3620, 12)
lenevo = tapaz("Lenovo", "Notebook","8 GB", 'Intel Core I7',"500 GB SSD", 'Qara','Var', '6 GB', '16 MP', "6500 mAh", 1800, 12)
toshiba = tapaz("Toshiba", "Notebook","2 GB", 'Intel Core I3',"300 GB HDD", 'Qara','Var', '2 GB', '8 MP', "2500 mAh", 820, 12)
dell = tapaz("Dell", "Notebook","4 GB", 'Intel Core I3',"300 GB HDD", 'Ağ','Var', '2 GB', '8 MP', "3500 mAh", 800, 12)


if (sys.argv[1] == "Notebook" and sys.argv[2] == "al"): 
    # a = input("Seç- ")
    apple.salam()
    apple.get_sale()
    apple.get_info()

# --- --- --- notebook classi bitdi --- --- ---




# --- --- --- Telefon class basladi --- --- ---

class tapaz:
    miqdari = "3"
    satilib = "12"

    def __init__(self, name, tipi, ram, Prosessor, Yaddaş, color, kredit, kamerasi, battery, sale, ayliq):
        self.name = name
        self.tipi = tipi
        self.ram = ram
        self.Prosessor = Prosessor
        self.Yaddaş = Yaddaş
        self.color = color
        self.kredit = kredit
        self.kamerasi = kamerasi
        self.battery = battery
        self.sale = sale
        self.ayliq = ayliq


    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("RAM: {}".format(self.ram))
        print("Prosessor: {}".format(self.Prosessor))
        print("Batarya: {}".format(self.battery))
        print("Əsas kamera: {}".format(self.kamerasi))
        print(f"Kredit: {self.kredit}")
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiymət: {self.sale} AZN")


    def get_info(self):
        print(f"Hazırda stokda {self.name} adli telefon mövcuddur. ")

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 200} AZN")

iphone = tapaz("Apple", "İphone","8 GB", 'A16',"1 TB", 'Purple', 'Var', '45 MP', "4500 mAh", 2500, 12)
samsung = tapaz("Samsung", "S23","8 GB", 'Snapdragon 8 Gen',"1 TB", 'Ağ', 'Var', '50 MP + 10MP + 12 MP', "3900 mAh", 2139, 12)
xiaomi = tapaz("Xiaomi", "12 Lite","8 GB", 'Qualcomm',"128 TB", 'Qara', 'Var', '108 MP', "4300 mAh", 899, 12)
nokia = tapaz("Nokia", "G21","4 GB", 'Unisoc',"128 GB", 'Göy', 'Var', '50 MP', "5050 mAh", 429, 12)
huawei = tapaz("Huawei", "Nova Y70","4 GB", 'Kirin',"128 GB", 'Kristal Göy', 'Var', '48 MP', "6000 mAh", 399, 12)

if (sys.argv[1] == "Telefon" and sys.argv[2] == "al"): 
    huawei.salam()
    huawei.get_sale()
    huawei.get_info()

# --- --- --- Telefon class bitdi --- --- ---


# --- --- --- Saat ve televizor class basladi --- --- ---


class tapaz:
    miqdari = "25"
    satilib = "120"

    def __init__(self, name, tipi, color, kredit, battery, sale):
        self.name = name
        self.tipi = tipi
        self.color = color
        self.kredit = kredit
        self.battery = battery
        self.sale = sale

    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("Batarya: {}".format(self.battery))
        print("Kredit: {}".format(self.kredit))
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiyməti: {self.sale} AZN")

    def get_info(self):
        print(f"Hazırda stokda {self.name} {self.tipi} mövcuddur. ")

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 50} AZN")

apple = tapaz("Apple", "Watch Ultra",'Ağ', 'Var',"542 mAh", 2199)
xiaomi = tapaz("Xiaomi", "Redmi Watch 2 Lite",'Qara', 'Var',"262 mAh", 130)
huawei = tapaz("Huawei", "Watch FİT 16",'Ağ', 'Var',"180 mAh", 159)


samsung = tapaz("Samsung", "Smart TV LED",'Qara', 'Var',"Tutumu yoxdur", 899)
xiaomi = tapaz("Xiaomi", "Smart TV LED",'Ağ', 'Var',"Tutumu yoxdur", 699)
lg = tapaz("LG", "Smart TV LED",'Qara', 'Var',"Tutumu yoxdur", 249)


if (sys.argv[1] == "Saat" and sys.argv[2] == "al"):
    huawei.salam()
    huawei.get_sale()
    huawei.get_info()

if (sys.argv[1] == "Televizor" and sys.argv[2] == "al"):
    samsung.salam()
    samsung.get_sale()
    samsung.get_info()


# --- --- --- Saat ve televizor class bitdi --- --- ---


# --- --- --- Kamera class basladi --- --- ---


class tapaz:
    miqdari = "12"
    satilib = "105"

    def __init__(self, name, tipi, color, kredit, battery, kamerasi, sale):
        self.name = name
        self.tipi = tipi
        self.color = color
        self.kredit = kredit
        self.battery = battery
        self.kamerasi = kamerasi
        self.sale = sale


    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("Batarya: {}".format(self.battery))
        print("Kredit: {}".format(self.kredit))
        print("Rəng: {}".format(self.color))
        print("Kamera: {}".format(self.kamerasi))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiymət: {self.sale} AZN")


    def get_info(self):
        print(f"Hazırda stokda {self.name} {self.tipi} mövcuddur. ")

    def get_sale (self):
        if self.sale > 200:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 109} AZN")

canon = tapaz("Canon", "EOS 850D",'Qara', 'Var',"890 mAh", "3840 x 2160 (4k UHD)", 1799)
sony = tapaz("Sony", "Alpha ILCE-7C",'Qara', 'Var',"994 mAh","3840 x 2160 (4k UHD)", 4499)
nikon = tapaz("Nikon", "D850 Body",'Qara', 'Var',"882 mAh","3840 x 2160 (4k UHD)", 6499)
leica = tapaz("Leica", "M10-R SL",'Qara', 'Var',"1290 mAh","7864 x 5200", 16739)



if (sys.argv[1] == "Kamera" and sys.argv[2] == "al"):
    sony.salam()
    sony.get_sale()
    sony.get_info()



# --- --- --- Kamera class bitdii --- --- ---
