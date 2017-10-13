def dosyaoku():
    ac = open("test.txt","r")
    veri = ac.read()
    ac.close()
    return veri

def dosyayaz(veri):
    ac = open("test.txt","w")
    ac.write(veri)
    ac.close()
    print("Yazıldı")



sablon = input("Şablon adı : ")
ad = input("Adınız : ")
soyad = input("Soyadınız : ")
email = input("Email : ")
sifre = input("Şifre : ")

sonuc = dosyaoku().format(sablon,ad,soyad,email,sifre)

dosyayaz(sonuc)
