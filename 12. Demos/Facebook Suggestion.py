# Suggest a Maximum Common Friends on Facebook

"""
    a---b---c
    |       |
    |---d---|---e
        |
        f
"""
# To use data from a database
# to input the data file
txt = open("friendship.txt", "r")
text = txt.readlines()

# Datadaki bilgileri satır satır işliceksin ki bu yüzden for döngüsü kullanılmalı
for line in text    # text diye adlandırdığımız dosyadaki her hat (line) için anlamında. Textin içinde sürekli okuyacak
  # print(line.strip()) # satır satır dosyayı okur
  # Her numarayı ayrı ayrı işleyeceğimiz için bunları ayırmamız lazım
  dic = {}                  # Boş bir sözlük oluşturuldu
  line = line.strip()
  line = line.split("\t")   # bir satırdaki iki verinin arasındaki boşluk tab kadar olduğu için 
  # İkisini ayrı ayrı işlemek istiyoruz ve bunu da int'e dönüştürmek istiyoruz
  line[0]=int(line[0])
  line[1]=int(line[1])
  if not line[0] in dic:
    dic[line[0]]=[]               # Satır index numarası yardımıyla 236 numaralı kişi için boş bir liste oluşturduk
    dic[line[0]].append(line[1])  # 236'nın arkadaşlarını tek tek ekle, bu for döngüsüyle sürekli dönüyor
  else:
    dic[line[0]].append(line[1])
    
  if not line[1] in dic:
    dic[line[1]]=[]
    dic[line[1]].append(line[0])
  else:
    dic[line[1]].append(line[0])
    
print(dic)  # Mesela 
            # 236'nın arkadaş olduğu kişileri liste şeklinde bize gösterecek
            # 122 ile arkadaş olanları gösterir
    
ID = int(input("Enter an user ID to suggest new friends. ")) #  ID input olduğunda böylece bir arkadaş önerecek -- Kullanıcı adı gibi

if not ID in dic:                       # Eğer girdiğin ID sözlüğün yani facebook içinde yoksa bunu yazdır
  print("There is no such an user ID")

else:
  sozluk = {}               # Yeni bir sözlük oluşturduk
  for id in dic[ID]:
    dic[id].remove(ID)
    for each in dic[id]:
      if not each in sozluk:
        sozluk[each] = 1
      else:
        sozluk[each]+= 1    # Ortak arkadaş kaç defa var, Her bir ortak arkadaşta bu sayı for döngüsü yardımıyla arttı

# print(sozluk)             # Mesela, ID numarasını yazdıktan sonra 235 ile 6 tane ortak arkadaşı olduğu gözükür 
                            # Sözlük formatında key ve value şeklinde çıkar. Key = user ID, Value = Kaç tane ortak arkadaşı var

# Yazdırmadan önce Maximumu bulmak daha iyi.
  maximum=max(sozluk.values())
  print(maximum)              # Maximum ortak arkadaş sayısı 25 çıktı diyelim, kaç kişiyle 25 ortak arkadaşı varsa bunları bize önerecek
  for a, b in sozluk.item():
    if b == maximum:
      print(a)                # ID sayısı önerecek: En fazla maximum ortak arkdaş sayısı onda olduğu için bize önerdi
                              # 236ya önerebileceğimiz 1 kişi çıktı. Daha doğrusu maximumu seçersek
                              # Başka bir Id kullanıldığında bunun sonucu olarak başka ID numaralı kişileri önerecek

# Eğer hiç ortak arkadaşları yoksa, yazılan kod muhtemelen hata verecek
# Diğer bir durum ise, Bu kod daha temiz olabilirdi ya da daha optimize olabilirdi



