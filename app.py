from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import sqlite3

def init_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            yas INTEGER,
            sure INTEGER,
            puan INTEGER,
            onceki_tur INTEGER,
            tavsiye TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

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
        

    input_data = pd.DataFrame([[yas, sure, puan, onceki_tur]], 
                              columns=["yas", "sure", "puan", "oncekiTur"])
    
    tahmin = model.predict(input_data)
    tavsiye = tahmin[0].capitalize()
    
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO predictions (yas, sure, puan, onceki_tur, tavsiye)
        VALUES (?, ?, ?, ?, ?)
    ''', (yas, sure, puan, onceki_tur, tavsiye))
    conn.commit()
    conn.close()
    
    return render_template("result.html", tavsiye=tavsiye)

@app.route("/history", methods=["GET"])
def history():
    conn = sqlite3.connect('history.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM predictions ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return render_template("history.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
