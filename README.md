# Proyek Analisis Data: Analisis Pola Penyewaan Sepeda (Bike Sharing Demand Analysis)

## Pendahuluan
Proyek ini bertujuan untuk menganalisis dataset penyewaan sepeda untuk memahami pola penggunaan dan faktor-faktor yang memengaruhinya. Analisis ini memberikan wawasan tentang bagaimana cuaca dan tipe pengguna (terdaftar atau kasual) memengaruhi jumlah penyewaan sepeda harian.

## Tujuan Proyek
* Menganalisis seberapa besar pengaruh cuaca terhadap jumlah sepeda yang disewa.
* Membandingkan pola penyewaan sepeda antara pengguna *registered* (terdaftar) dan *casual* (non-terdaftar) di hari kerja.

## Dataset
https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

### Penjelasan Dataset
* **`instant`**: Indeks catatan.
* **`dteday`**: Tanggal.
* **`season`**: Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin).
* **`yr`**: Tahun (0: 2011, 1: 2012).
* **`mnth`**: Bulan (1 sampai 12).
* **`hr`**: Jam (0 sampai 23) - *hanya di `hour.csv`*.
* **`holiday`**: Indikator hari libur atau bukan.
* **`weekday`**: Hari dalam seminggu.
* **`workingday`**: Indikator hari kerja (1 jika bukan akhir pekan atau hari libur, 0 jika sebaliknya).
* **`weathersit`**: Kondisi cuaca:
    * 1: Cerah, sedikit awan, sebagian berawan.
    * 2: Kabut + mendung, kabut + awan pecah, kabut + sedikit awan, kabut.
    * 3: Salju ringan, hujan ringan + badai petir + awan tersebar, hujan ringan + awan tersebar.
    * 4: Hujan lebat + es + badai petir + kabut, salju + kabut.
* **`temp`**: Suhu yang dinormalisasi dalam Celsius. Nilai turunan dari `(t-t_min)/(t_max-t_min)`, dengan `t_min=-8`, `t_max=+39` (hanya dalam skala per jam).
* **`atemp`**: Suhu perasaan yang dinormalisasi dalam Celsius. Nilai turunan dari `(t-t_min)/(t_max-t_min)`, dengan `t_min=-16`, `t_max=+50` (hanya dalam skala per jam).
* **`hum`**: Kelembaban yang dinormalisasi. Nilai dibagi dengan 100 (maksimum).
* **`windspeed`**: Kecepatan angin yang dinormalisasi. Nilai dibagi dengan 67 (maksimum).
* **`casual`**: Jumlah pengguna kasual.
* **`registered`**: Jumlah pengguna terdaftar.
* **`cnt`**: Total jumlah penyewaan sepeda (termasuk pengguna kasual dan terdaftar).

## Metodologi
Proyek ini mengikuti tahapan analisis data standar:
1.  **Pengumpulan Data (Gathering Data):** Memuat dataset `day.csv` dan `hour.csv` menggunakan Pandas.
2.  **Penilaian Data (Assessing Data):** Melakukan pemeriksaan awal pada struktur data, tipe data, dan keberadaan nilai hilang atau duplikasi. Tidak ditemukan masalah signifikan pada kedua dataset.
3.  **Pembersihan Data (Cleaning Data):** Tidak ada langkah pembersihan data yang spesifik diperlukan karena data sudah bersih dan tidak memiliki nilai kosong atau duplikasi.
4.  **Analisis Data Eksploratif (EDA):**
    * Menganalisis rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca (`weathersit`).
    * Menganalisis rata-rata jumlah penyewaan sepeda oleh pengguna *registered* dan *casual* berdasarkan hari kerja (`workingday`).
    * Menganalisis distribusi penyewaan sepeda berdasarkan musim (`season`).

## Dashboard Analisis Data Penyewaan Sepeda  

### Cara Menjalankan di Lokal  

1. **Clone repo ini**  
   ```bash
   git clone https://github.com/Jirrooo/Projek-Analisis-Data-Dicoding.git
   cd projek-analisis-data/dashboard
   ```

2. **Buat virtual environment (opsional, tapi disarankan)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan dashboard**  
   ```bash
   streamlit run dashboard.py
   ```

## Deploy ke Streamlit Cloud  

1. **Push kode ke GitHub**  
2. **Buka [Streamlit Cloud](https://share.streamlit.io/)**  
3. **Connect repo GitHub**  
4. **Tentukan file utama:** `dashboard/dashboard.py`  
5. **Tambahkan `requirements.txt` jika belum ada**  
6. **Deploy!**  

---

## Hasil dan Wawasan
### Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda
![Plot Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda](https://github.com/Jirrooo/Bike-Sharing-Demand-Analysis/blob/main/assets/plot%20pengaruh%20cuaca%20terhadap%20penyewaan%20sepeda.png)
* Rata-rata jumlah penyewaan sepeda tertinggi terjadi saat cuaca cerah (weathersit = 1) yaitu sekitar 4.876 sepeda/hari.
* Saat kondisi cuaca berawan (weathersit = 2), rata-rata penyewaan turun menjadi sekitar 4.035 sepeda/hari.
* Ketika cuaca memburuk menjadi hujan ringan atau salju ringan (weathersit = 3), penyewaan turun drastis menjadi sekitar 1.803 sepeda/hari.
* Tidak ada pelanggan yang menyewa sepeda saat cuaca hujan deras atau badai (weathersit = 4).
  
**Wawasan:** Cuaca memiliki pengaruh signifikan terhadap permintaan penyewaan sepeda. Kondisi cuaca yang baik sangat mendukung peningkatan jumlah penyewaan.

### Perbandingan Pengguna Registered dan Casual di Hari Kerja
![Plot Perbandingan Pengguna Registered dan Casual di Hari Kerja](https://github.com/Jirrooo/Bike-Sharing-Demand-Analysis/blob/main/assets/plot%20perbandingan%20penyewaan%20sepeda%20antara%20registered%20dan%20casual%20user.png)
* Pengguna *registered* memiliki rata-rata penyewaan yang lebih tinggi di hari kerja (sekitar 3.978 sepeda/hari) dibandingkan pengguna *casual* (sekitar 606 sepeda/hari).
* Pengguna *casual* meningkat di akhir pekan/hari libur (rata-rata 1.371 sepeda/hari).
  
**Wawasan:** Pengguna terdaftar cenderung menggunakan sepeda untuk kebutuhan rutin seperti perjalanan ke kantor atau sekolah, sementara pengguna kasual lebih sering menggunakannya untuk rekreasi di akhir pekan.

### Distribusi Penyewaan Sepeda Berdasarkan Musim
![Plot Distribusi Penyewaan Sepeda Berdasarkan Musim](https://github.com/Jirrooo/Bike-Sharing-Demand-Analysis/blob/main/assets/plot%20distribusi%20penyewaan%20sepeda%20berdasarkan%20musim.png
)
* Jumlah hari dengan penyewaan sepeda cukup merata di setiap musim (Musim Semi, Musim Panas, Musim Gugur, Musim Dingin), menunjukkan bahwa musim tidak terlalu memengaruhi kebiasaan pengguna dalam menyewa sepeda secara drastis.
  
**Wawasan:** Strategi promosi dan ketersediaan sepeda dapat dipertahankan secara fleksibel sepanjang tahun tanpa perlu terlalu berfokus pada musim tertentu.

---
