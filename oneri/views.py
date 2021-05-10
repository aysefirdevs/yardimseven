from django.shortcuts import render, redirect
from django.db import connection
from django.views.generic import ListView
from sqlalchemy import create_engine
import pymysql
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn
from re import search
# Create your views here.
from yardim.models import Ihtiyac


def veriokuma(request):
    current_user = request.user  #giriş yapan kullanıcı alınıyor.
    id=current_user.id           #giris yapan kullanici id si alıyoruz.
    db_connection_str = 'mysql+pymysql://root:1234@127.0.0.1/django_db'
    db_connection = create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM yardim_arsiv', con=db_connection)        #veritabanında arsiv tablosuna bağlanıyorum.
    select = df.loc[df['user_id']==id]             #arsiv tablosundan sadece giris yapmis kullanicinin verilerini çekiyorum.


    #print(select)

    a=' '
    vir=","
    for x in select.content:        #contentleri birleştirip virgül ile ayırıyorum.
        a = x + vir + a

    #print(a)

    metin = a.split(",")                    # virgül gorduğumuz her kelimeyi split ile ayırıyorum.
    sozluk = dict.fromkeys(metin, 0)        #virgülle ayırdığım kelimeleri sözlük haline getiriyorum.

    for z in metin:                         #metinde geçen kelimelerin kaç defa geçtiğini sayan döngü
        sozluk[z] += 1

    pd.DataFrame([sozluk])


    def computeTF(wordDict, bow):           #term fruquency algoritması kullanıldı.
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bowCount)
        return tfDict

    tfdeneme = computeTF(sozluk, metin)
    tf_df = pd.DataFrame([tfdeneme])
    tfidf=tf_df.idxmax(axis=1)    #tfidf içinde en yüksek değeri olan kelime bulunuyor.
    print(tf_df)

    print("en çok kullanılan kelime", tfidf)  #en çok bağış yaptığı kelimeyi terminale basıyorum.


    iht = pd.read_sql('SELECT * FROM yardim_ihtiyac', con=db_connection)    #anasayfadaki ihtiyaçlar listesini vt den çekiyorum.
    ihtiyaclistele=Ihtiyac.objects.all()        #html için gerekti görünmesi adına.

    abc=str(tfidf)      #en çok bağış yapılan kelimenin tf değerini stringe çevirdim.
    ayrik=abc.split(" ")
    temp=ayrik[5]
    eleman=temp.split("\n")
    kelime=eleman[0]
    sayac=121
    gecici=list()           #gecici adında bir liste oluşturdum.
    for f in iht.content:   #ihtiyac tablosundaki content kolonunu for döngüsüne aldım .
        sayac = sayac + 1
        ayirma=f.split(" ")     #içine girdiğim contentte boşluk gördükçe kelimeleri ayırdım.
        for k in ayirma:        #ayırdığım keliemeleri döngüye alarak tek tek bakıyorum.
            if kelime in k:     #kelime kullanıcın en çok bağış yaptığı ile ihtiyaç tablosundaki keliemelrden birini bulursa döngüye gir.
                gecici.append(sayac)        #sayacta tuttuğu idyi gönderiyor ve idyi gecici listesine atıyorum.
                print(gecici)

    #gerekli=Ihtiyac.objects.filter(id=gecici)

    return render(request, 'oneri/veriokuma.html',{'ihtiyaclistele':ihtiyaclistele,'gecici':gecici})






