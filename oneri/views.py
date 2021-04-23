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
    current_user = request.user
    id=current_user.id
    db_connection_str = 'mysql+pymysql://root:1234@127.0.0.1/django_db'
    db_connection = create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM yardim_arsiv', con=db_connection)        #veritabanında arsiv tablosuna bağlanıyorum.
    select = df.loc[df['user_id']==id]             #kullanıcıların idlerini alıyorum burda.


    #print(select)

    a=' '
    vir=","
    for x in select.content:
        a = x + vir + a

    #print(a)

    metin = a.split(",")
    sozluk = dict.fromkeys(metin, 0)

    for z in metin:
        sozluk[z] += 1

    pd.DataFrame([sozluk])


    def computeTF(wordDict, bow):
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bowCount)
        return tfDict

    tfdeneme = computeTF(sozluk, metin)
    tf_df = pd.DataFrame([tfdeneme])
    tfidf=tf_df.idxmax(axis=1)    #tfidf içinde en yüksek değeri olan kelime bulunuyor.
    print(tf_df)

    print("en çok kullanılan kelime", tfidf)  #en çok bağış yaptığı kelimeyi basıyotum.


    iht = pd.read_sql('SELECT * FROM yardim_ihtiyac', con=db_connection)
    ihtiyaclistele=Ihtiyac.objects.all()

    abc=str(tfidf)
    ayrik=abc.split(" ")
    temp=ayrik[5]
    eleman=temp.split("\n")
    kelime=eleman[0]
    sayac=121
    gecici=list()
    for f in iht.content:
        sayac = sayac + 1
        ayirma=f.split(" ")
        for k in ayirma:
            if kelime in k:
                gecici.append(sayac)
                print(gecici)

    #gerekli=Ihtiyac.objects.filter(id=gecici)


    return render(request, 'oneri/veriokuma.html',{'ihtiyaclistele':ihtiyaclistele,'gecici':gecici})






