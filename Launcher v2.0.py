import PySimpleGUI as sg
from datetime import datetime
from threading import Timer
import time
from selenium import webdriver
import os


sg.theme('DarkAmber')   # Color
# All the stuff inside your window.
layout = [[sg.Text('Gerekli EBA Bilgilerini Gir.')],
          [sg.Text('EBABOT bu bilgileri kimse ile paylaşmaz.')],
          [sg.Text('Kimlik Numaranız', size=(13, 1)), sg.InputText()],
          [sg.Text('EBA Şifreniz', size =(13, 1)), sg.InputText()],
          [sg.Button('Başlat'), sg.Button('Geciktim'), sg.Button('İptal')]]
# Create the Window
window = sg.Window('EBABOT 2021 v1.0', layout)



# loop to get inputs
while True:
    event, values = window.read()
    tckn = values[0]
    sifre = values[1]
    if event == 'Başlat':
        # get date
        datetime.today()
        datetime(2012, 3, 23, 23, 24, 55, 173504)
        date = datetime.today().weekday()

        # // 0 = Pazartesi, 6 = Pazar //#

        # get time
        now = datetime.now()
        saat = now.strftime("%H:%M")

        print(saat, datetime.today(), date)

        print("EBABOT 2021")
        print("Başlatılıyor!")
        print("EBABOT Akşamöncesi sürümünü kullanıyorsunuz.")
        path = os.getcwd()
        profile = path + r"\dyrdas9x.EBA"
        print("Profil klasörü", profile, "adresinde bulundu.")
        print("Programdan tamamen çıkmak için CTRL + Pause/Break tuşuna basın.")
        if "00.00" < saat < "14:40":
            date += 1

        # ders öğlen mi akşam mı
        #if date == 1 or date == 3 or date == 5:
        #    print("Yarın ders öğlen lol")
        #    oglen = 1  # sabah
        #else:
        #    print("Yarın ders sabah lol")
        #    oglen = 0  # öğlen

        # DEFINITIOS
        oglen = 0
        fp = webdriver.FirefoxProfile(profile)
        driver = webdriver.Firefox(firefox_profile=fp)

        # giriş
        def giris():

            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            driver.find_element_by_id("tckn").send_keys(tckn)
            driver.find_element_by_id("password").send_keys(sifre)
            driver.find_element_by_class_name("nl-form-send-btn").click()

        # derse katılım
        def katil():

            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            time.sleep(2)
            driver.find_element_by_id("joinMeeting").click()
            time.sleep(2)
            driver.find_element_by_id("join").click()


        def ders():
            print("Derse giriş yapılıyor!")
            katil()
            time.sleep(1800)  # DERS UZUNLUĞU
            print("Ders Bitti! Beklemeye geçiliyor.")
            time.sleep(605)  # TENEFÜS UZUNLUĞU


        def okul():
            print("Giriş yapılıyor..")
            giris()
            print("Başarıyla Giriş Yapıldı!")
            ders_sayisi = 0
            while ders_sayisi < 9:
                ders()
                ders_sayisi += 1

            print("Daha fazla dersin yok")

        def tomorrow():
            if oglen == 1:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 1, hour=14, minute=50, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                print("Dersin başlamasına", sure / 3600, "saat kaldı!")
                t = Timer(sure, okul)
                t.start()
            else:

                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 1, hour=9, minute=30, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                print("Dersin başlamasına", sure / 3600, "saat kaldı!")
                t = Timer(sure, okul)
                t.start()


        def today():
            if oglen == 1:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 0, hour=14, minute=50, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                print("Dersin başlamasına", sure / 3600, "saat kaldı!")
                t = Timer(sure, okul)
                t.start()
            else:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 0, hour=9, minute=30, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                print("Dersin başlamasına", sure / 3600, "saat kaldı!")
                t = Timer(sure, okul)
                t.start()
        if "09:30" > saat > "00.00":
            today()
        else:
            tomorrow()
    if event == 'Geciktim':
        print("EBABOT 2021")
        print("Eğer ilerleyen derslerin otomatikleşmiyorsa bir sonraki dersin tam başlangıcında programı açmayı unutma")
        path = os.getcwd()
        profile = path + r"\dyrdas9x.EBA"
        print("Profil klasörü", profile, "adresinde bulundu.")
        print("Programdan tamamen çıkmak için CTRL + Pause/Break tuşuna basın.")
        fp = webdriver.FirefoxProfile(profile)
        driver = webdriver.Firefox(firefox_profile=fp)
        
        # giriş
        def giris():
            #   driver = webdriver.Firefox()
            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            driver.find_element_by_id("tckn").send_keys("15515365506")
            driver.find_element_by_id("password").send_keys("4185177em")
            driver.find_element_by_class_name("nl-form-send-btn").click()

        # derse katılım
        def katil():
            #  driver = webdriver.Firefox()
            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            time.sleep(2)
            driver.find_element_by_id("joinMeeting").click()  # TODO: CANLI DERSE KATILIM EKLE
            time.sleep(2)
            driver.find_element_by_id("join").click()


        def ders():
            print("Derse giriş yapılıyor!")
            katil()
            time.sleep(1800)  # DERS UZUNLUĞU
            print("Ders Bitti! Beklemeye geçiliyor.")
            time.sleep(605)  # TENEFÜS UZUNLUĞUg


        def okul():
            print("Giriş yapılıyor..")
            giris()
            print("Başarıyla Giriş Yapıldı!")
            ders_sayisi = 0
            while ders_sayisi < 9:
                ders()
                ders_sayisi += 1

            print("Daha fazla dersin yok")


        okul()
    if event == sg.WIN_CLOSED or event == 'İptal':  # if user closes window or clicks cancel
        window.close()
        break

window.close()
