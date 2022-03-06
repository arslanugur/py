# INFORMATION ABOUT UNDERLINES IN PYTHON (PYTHON ALT ÇİZGİLER HAKKINDA BİLGİLER)

# BAŞTAKİ TEK ALT ÇİZGİ: _var
Class Pubber:
  def __init__(self):
    self.name = 'String'
    self._age = 333 # Private Değişken
  # Py, Java gibi "private" ve "public" değişkenler arasında güçlü bir ayrım yapmaz.
  # Bu nedenle, bir değişkenin dahili kullanım için olduğunu belirtmek için, değişken adından önce tek bir alt çizgi (ön ek) kullanılır.
#


# SONDAKİ TEK ALT ÇİZGİ: var_
Class class: #SyntaxError: "invalid syntax"
Class class_ # No Problem
  # Değişken, fonksiyon veya sınıf adlarından sonra tek bir alt çizgi (son ek) eklerseniz kendi yazdığınız kelimelerin Py anahtar kelimeleriyle çakışmasını önler. 
#


# BAŞTAKİ İKİ ALT ÇİZGİ: __var
Class Pubber:
  def __init__(self):
    self.name = 'String'
    self._age = 333
    self.__adress = 'Mars'
  # Py'da subclass'larda isim çakışmalarını önlemek için çift alt çizgi öneki kullanılabilir.
#


# BAŞTAKİ VE SONDAKİ İKİ ALT ÇİZGİ: __var__
Class Pubber:
  def __init__(self):
  def __call__(self):
  # Hem başında hem de sonunda çift alt çizgi bulunan adlar, dilde özel kullanım için ayrılmıştır.
  # Bazen 'Special Methods' veya 'Magic Methods' olarak anılır.
  # Py'da nesne oluşturucular için __init__
  #       nesneleri çağırabilir hale getirmek için __call__ gibi 100'ye yakın yerleşik fonksiyon vardır.
#


# TEK ALT ÇİZGİ: _
for _ in range(5):  # for döngüsü
  # Bir değişkenin geçici veya önemsiz olduğunu belirtmek için ad olarak tek bir bağımsız alt çizgi kullanılır.
#




