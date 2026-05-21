import numpy as np
import pandas as pd

def farkliTurOner():
    farkli_turler = [t for t in tum_turler if t != onceki_metin]
    if yas_egilimi in farkli_turler:
        onerilen = yas_egilimi
    else:
        onerilen = np.random.choice(farkli_turler)
    return onerilen


# kaynak veri kontrolü
try:
    df_orjinal = pd.read_csv("asilVeri.csv")
    print(":)")
except FileNotFoundError:
    print(
        "Hata: kaynak veri yok"
    )
    exit()

hedef_satir = 3000
np.random.seed(42)

sentetik_yas = np.random.randint(
    df_orjinal["yas"].min(), df_orjinal["yas"].max() + 1, hedef_satir
)
sentetik_sure = np.random.randint(
    df_orjinal["sure"].min(), df_orjinal["sure"].max() + 1, hedef_satir
)
sentetik_puan = np.random.randint(
    df_orjinal["puan"].min(), df_orjinal["puan"].max() + 1, hedef_satir
)

sentetik_onceki = np.random.choice([1, 2, 3], size=hedef_satir)

tur_map = {1: "aksiyon", 2: "dram", 3: "komedi"}
tum_turler = ["aksiyon", "dram", "komedi"]

sentetik_tavsiye = []


for i in range(hedef_satir):
    yas = sentetik_yas[i]
    sure = sentetik_sure[i]
    puan = sentetik_puan[i]
    onceki_metin = tur_map[sentetik_onceki[i]]

    # yaşa göre tavsiye
    if np.random.rand() < 0.1:
        yas_egilimi = np.random.choice(tum_turler)     
    elif yas < 26:
        yas_egilimi =  "aksiyon"
    elif 26 <= yas <= 40:
        yas_egilimi = "komedi"
    else: 
        yas_egilimi = "dram"

    #30-
    if sure < 30 :
        if puan > 5 :
                if np.random.rand() < 0.2:
                    onerilen = onceki_metin
                else:
                    onerilen = yas_egilimi
        else:
            onerilen = farkliTurOner() 

     #30+
    else:

        if puan < 5:
            onerilen = farkliTurOner()

        elif 5 <= puan < 8:
            if np.random.rand() < 0.6:
                onerilen = onceki_metin  
            else:
                onerilen = yas_egilimi
        else:
            onerilen = onceki_metin

    sentetik_tavsiye.append(onerilen)

df_sentetik = pd.DataFrame(
    {
        "yas": sentetik_yas,
        "sure": sentetik_sure,
        "puan": sentetik_puan,
        "oncekiTur": sentetik_onceki,
        "tavsiye": sentetik_tavsiye,
    }
)


df_nihai = pd.concat([df_orjinal, df_sentetik], ignore_index=True)

df_nihai.to_csv("sentetik_film_verisi.csv", index=False)

print(f"İşlem tamamlandı! Toplam satır sayısı: {len(df_nihai)}")
print("Yeni veri seti 'sentetik_film_verisi.csv' adıyla kaydedildi.")
