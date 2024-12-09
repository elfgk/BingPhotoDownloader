# Bing Görsel İndirme Uygulaması
Bu proje, kullanıcıların Bing üzerinden görseller indirmesine olanak sağlayan bir Python uygulamasıdır. Gradio arayüzü sayesinde kolayca kullanılabilir.

### Gereksinimler
Uygulamayı çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

gradio
bing-image-downloader


### Nasıl Çalışır?
Kullanıcı, indirmek istediği görsellerle ilgili anahtar kelimeyi girer.
İndirilmesini istediği görsel sayısını belirler.
Korumalı mod (yetişkin filtresi) ayarını yapar.
Uygulama, Bing üzerinden belirtilen sayıda görseli indirir ve indirme işlemini tamamlar.


### Kurulum ve Çalıştırma
Proje dosyalarını bilgisayarınıza indirin veya klonlayın.
Terminal veya komut satırında aşağıdaki komutla uygulamayı başlatın:
python app.py
Uygulama tarayıcınızda otomatik olarak açılacaktır. Alternatif olarak, terminalde paylaşılan bağlantıyı kullanabilirsiniz.

### Özellikler
Arama Anahtarı: Aramak istediğiniz kelimeyi yazabilirsiniz (örneğin, "cat", "dog").
Görsel Sayısı: İndirilecek görsel sayısını 1 ile 100 arasında ayarlayabilirsiniz.
Korumalı Mod: Yetişkin içerik filtresi için "True" (açık) veya "False" (kapalı) seçeneğini kullanabilirsiniz.
Gradio Arayüzü: Kullanıcı dostu  bir arayüz.


### Kullanım
Arama kutusuna anahtar kelimeyi yazın.
İndirmek istediğiniz görsel sayısını belirlemek için kaydırıcıyı kullanın.
Korumalı mod seçeneğini ayarlayın.
Uygulama görselleri indirdikten sonra, sonuç mesajını göreceksiniz. Görseller, çalıştırdığınız dizinde bir klasöre kaydedilecektir.


