import os
import hashlib

seed = os.urandom(32) # 32 bayt boyutunda rastgelelik. Linux için /dev/random metodunu da kullanabilirsiniz.
hash = hashlib.sha256() # Bitcoin'in de kullandığı SHA-2'yi kullanıyoruz burada.
hash.update(seed) # seed değişkenini hash'e atadık.
hash = hash.hexdigest() # hash'i çalıştırıp hexadecimal (16'lı sayı sistemi) sayı çıktısı aldık.
print("seed:", hash)

# hash değerini kullanıcıyla paylaşabiliriz böylece kullanıcı numaranın gerçekten rastgele olup olmadığını doğrulayabilir.
# hash değişkeni orijinal seed'imizin SHA-256 ile şifrelenmiş halidir, kullanıcı ile paylaşmamız gereken değer de budur.
# Kullanıcının gerçek seed'i bulması imkansız çünkü hash'ı ters çevirmeleri gerekecek.

# Şimdi seed'i kullanarak rastgele sayılar üreteceğiz.
# Her bir oyun için tohuma sıfırdan başlayarak sayılan bir nonce değeri ekleyeceğiz. (nonce, kriptografik iletişimde sadece bir kez kullanılabilen rastgele bir sayıdır.)
# Ardından rastgele sayıları oluşturmak için farklı bir kriptografik karma işlevi kullanacağız.

nonce = 0 # 0'dan başlar ve her işlem için arttırılabilir.

while True:
    seedWithNonce = seed + nonce.to_bytes(32, byteorder="big") # seed'e nonce'u ekledik.
    numhash = hashlib.sha3_256(seedWithNonce).hexdigest() # Burada da Ethereum'un kullandığı SHA-3'ü kullanıyoruz.
    roll = int(numhash, 16) % 6 + 1 # hash'in hexadecimal çıktısını integer'a çeviriyoruz.
    # integer'a çevirdiğimiz değeri 6'ya mod alarak + 1 ekliyoruz ki 1 ile 6 arasında bir değer üretilsin.
    print("Zar atışı:", roll)
    os.system("pause >nul")
    nonce += 1