i=15           #burada i ye while döngüsünden daha küçük olacak bir değer atıyoruz li while sonsuz kere çalışsın ve durmadan cevap alabilelim
while i<20 :  #burada while döngüsü i 20 den küçük olduğu sürece içindeki fonksiyonları çalıştıracak içindeki işlemlerde i ye dokunmadığımız için sonsuz kere çalışacak
    a=input("lütfen 1. sayıyı giriniz  ")  #input ile kullanıcıdan ilk değeri alıyoruz kullanıcı ne istediğimizi anlasın diye parantez içinde belirtilir
    b=input("lütfen 2. sayıyı giriniz  ")   #input ile kullanıcıdan ikinci değeri alıyoruz kullanıcı ne istediğimizi anlasın diye parantez içinde belirtilir
    print("                              ")     #daha estetik ve güzel dursun diye bir satırı boşluk yazdırır
    print("Toplama İşlemi İçin 1 e Basınız ")   #kullanıcıyı hangi işlemlerin hangi değere denk geldiğini belirtir
    print("Çıkarma İşlemi İçin 2 e Basınız ")   #kullanıcıyı hangi işlemlerin hangi değere denk geldiğini belirtir
    print("Çarpma İşlemi İçin 3 e Basınız ")    #kullanıcıyı hangi işlemlerin hangi değere denk geldiğini belirtir
    print("Bölme İşlemi İçin 4 e Basınız ")     #kullanıcıyı hangi işlemlerin hangi değere denk geldiğini belirtir
    print("                              ")     #daha estetik ve güzel dursun diye bir satırı boşluk yazdırır

    c=input("lütfen yapmak istediğiniz işlemi seçiniz : ") # yukarıdaki bilgilendirmeden sonra alınacak değeri tutan değişken ve bunu yine belirten yorum

    if c=="1":                                   #alınan değer eğer 1 ise buradaki işlemleri yapar
        print("Cevap: " + str(float(a)+float(b)))    #yukarıda aldığı değerleri önce inte döüştürüp bunlarla işlem yapar daha sonra ekranda görünmesi için tekrardan string yapar
        print("      ")                          #daha estetik dursun diye bir satır boşluk bırakır
    elif c=="2":                                 #alınan değer eğer 2 ise buradaki işlemleri yapar
        print("Cevap: " + str(float(a)-float(b)))    #yukarıda aldığı değerleri önce inte döüştürüp bunlarla işlem yapar daha sonra ekranda görünmesi için tekrardan string yapar
        print("      ")                          #daha estetik dursun diye bir satır boşluk bırakır
    elif c=="3":                                 #alınan değer eğer 3 ise buradaki işlemleri yapar
        print("Cevap: " + str(float(a)*float(b)))    #yukarıda aldığı değerleri önce inte döüştürüp bunlarla işlem yapar daha sonra ekranda görünmesi için tekrardan string yapar
        print("      ")                          #daha estetik dursun diye bir satır boşluk bırakır
    elif c=="4":                                 #alınan değer eğer 4 ise buradaki işlemleri yapar
        print("Cevap: " + str(float(a)/float(b)))    #yukarıda aldığı değerleri önce inte döüştürüp bunlarla işlem yapar daha sonra ekranda görünmesi için tekrardan string yapar
        print("      ")                          #daha estetik dursun diye bir satır boşluk bırakır
    else:                                        #alınan değer eğer bunlar dışında başka birşeyse ise buradaki işlemleri yapar
        print("Hatalı işlem! Lütfen Sadece Yukarıda Yazılan Sayıyılardan Birini Tuşlayın Örneğin ") #bunlar dışında değer seçildiğinde neden çalışmadığını belirtip uyarmasını sağlar
        print("           ")                          #daha estetik dursun diye bir satır boşluk bırakır
    