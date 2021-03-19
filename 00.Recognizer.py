import speech_recognition as sr #sr ile bi kısaltmayla bunu al

r = sr.Recognizer() #sesleri tanımak için bi fonksiyon çağır, bu da geriye bi parametre döndürüyor bunu da r ile yakala

with sr.Microphone() as source   #daha sonra mikrofonumuzu dinlicez burdan gelenleri de source olrak alırız
    audio = r.listen(source) #sesi geriye döndürecek sonrası anlamlı bi metin oluşturcaz
    #r üzerinden listen deyip kaynağı source dinlemeye başlıyoruz
    voice = r.recognize_google(audio, language= 'en-EN', 'tr-TR', 'ru-RU') #anlamlı bi metni voice değişenine atarız
#...gogle diyerek audio altında ttuğumuz değer, tanımlanmaya çalış
    print(voice)


