# 🎬 Film Öneri Sistemi (Movie Recommendation System)

Bu proje, kullanıcının ruh haline, tercih ettiği türe veya izleme geçmişine göre makine öğrenmesi (Machine Learning) algoritmalarını kullanarak film önerilerinde bulunan web tabanlı bir Python/Flask uygulamasıdır.

---

## 📌 Proje Özellikleri

- **Makine Öğrenmesi Destekli Öneri Motoru:** `scikit-learn` ve `pandas` kütüphaneleri ile eğitilmiş model sayesinde kişiselleştirilmiş film önerileri.
- **Dinamik Veri Yönetimi:** Gerçek veriler (`asilVeri.csv`) ve sentetik veri üretim mekanizması (`sentetikVeriUret.py`) ile model eğitimi (`egitim.py`).
- **Kullanıcı Dostu Web Arayüzü:** HTML/CSS (`style.css`) ile modern, sade ve responsive bir tasarım.
- **İzleme / Öneri Geçmişi:** Kullanıcıların geçmiş arama ve önerilerini inceleyebileceği `history.html` sayfası.
- **Production-Ready Deployment:** Canlıya alınmaya hazır `gunicorn` ve `requirements.txt` yapılandırması.

---

## 📁 Proje Dizin Yapısı

```text
FilmOneri-main/
├── static/
│   └── style.css            # Web arayüzü stil dosyası
├── templates/
│   ├── index.html           # Ana sayfa (film/ruh hali seçim formu)
│   ├── result.html          # Öneri sonuçları ekranı
│   └── history.html         # Geçmiş öneriler ekranı
├── app.py                   # Flask web sunucusu ve ana uygulama mantığı
├── egitim.py                # Makine öğrenmesi modelinin eğitildiği betik
├── sentetikVeriUret.py      # Test ve geliştirme için sentetik veri üreten betik
├── asilVeri.csv             # Model eğitiminde kullanılan ana film veri seti
└── requirements.txt         # Gerekli Python kütüphaneleri
