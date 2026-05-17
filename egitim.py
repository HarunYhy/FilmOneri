import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("sentetik_film_verisi.csv")

X = df[["yas", "sure", "puan", "oncekiTur"]]
y = df["tavsiye"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

tahminler = model.predict(X_test)

accuracy = accuracy_score(y_test, tahminler)

# 10 veri test 
print("Test verisi tahminleri:")
print(tahminler[:10])

print("Gercek etiketler:")
print(list(y_test)[:10])

print("Accuracy:", accuracy)

joblib.dump(model, "filmOneri.pkl")

print("Model kaydedildi: ogrenci_model.pkl")