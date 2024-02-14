import time
import sys

class ATM:
    def __init__(self):
        self.bakiye = 1000

    def bakiye_sorgula(self):
        print("Bakiyeniz: {}TL dir.".format(self.bakiye))

    def para_cek(self):
        para_cekme = int(input("Lutfen cekmek istediginiz bakiyeyi giriniz: "))
        if para_cekme > self.bakiye or para_cekme < 0:
            print("Gecersiz islem. Lutfen tekrar deneyin.")
        else:
            self.bakiye -= para_cekme
            print("İslem basarili, bakiyeniz: {}TL".format(self.bakiye))

    def para_yatir(self):
        para_yatirma = int(input("Yatirmak istediginiz miktari giriniz: "))
        self.bakiye += para_yatirma
        print("İslem basarili, bakiyeniz: {}TL dir.".format(self.bakiye))

    def ana_menu(self):
        print("""
        ATM PROGRAMİNA HOSGELDİNİZ
        ***********************
        1)BAKIYE SORGULAMA 
        2)PARA CEKME
        3)PARA YATIRMA
        PROGRAMDAN CIKMAK ICIN Q TUSLAYIN
        ***********************
        """)

    def run(self):
        while True:
            self.ana_menu()
            islem = input("Lutfen isleminizi seciniz: ")

            if islem.lower() == "q":
                print("Programdan cikiliyor...")
                sys.exit()

            elif islem == "1":
                self.bakiye_sorgula()

            elif islem == "2":
                self.para_cek()

            elif islem == "3":
                self.para_yatir()

            else:
                print("Gecersiz islem. Lutfen tekrar deneyin.")

            time.sleep(1)

if __name__ == "__main__":
    atm = ATM()
    atm.run()