from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("filmOneri.pkl")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    yas = int(request.form.get("yas"))
    sure = int(request.form.get("sure"))
    puan = int(request.form.get("puan"))
    onceki_tur = int(request.form.get("onceki_tur"))
    if yas < 18:
        hata_mesaji = "Maalesef 18 yaş altı için eğitilmiş verimiz bulunmamaktadır."
        return render_template("result.html", hata=hata_mesaji)
        
    # Modele gönderilecek veriyi DataFrame olarak hazırlıyoruz
    input_data = pd.DataFrame([[yas, sure, puan, onceki_tur]], 
                              columns=["yas", "sure", "puan", "oncekiTur"])
    
    tahmin = model.predict(input_data)
    tavsiye = tahmin[0].capitalize()
    
    return render_template("result.html", tavsiye=tavsiye)

if __name__ == "__main__":
    app.run(debug=True)
