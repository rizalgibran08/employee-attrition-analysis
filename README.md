# Monitoring Attrition of Employee

# 🔰 Proyek : Menyelesaikan Permasalahan Perusahaan Edutech

## 🗂️ Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### 🔍 Permasalahan Bisnis

Berikut beberapa permasalahan utama yang ingin diselesaikan dalam proyek ini:

1. Mengetahui **kelompok usia dan jabatan** mana yang paling rentan mengalami attrition.
2. Mengidentifikasi **departemen dengan tingkat attrition tertinggi**.
3. Menganalisis pengaruh **gaji bulanan (monthly income)** terhadap keputusan karyawan untuk keluar atau tetap.
4. Menganalisis pengaruh **lama bekerja (years at company)** terhadap attrition.
5. Menggali apakah faktor seperti **gender, marital status, dan job level** turut memengaruhi attrition.
6. Memberikan **insight visual interaktif** agar tim HR dapat melakukan analisis lebih dalam secara mandiri.

### 📌 Cakupan Proyek

Berdasarkan penjelasan tersebut, submission yang kamu kerjakan adalah proyek employee attrition analysis dengan tiga tujuan utama:
1. Mengidentifikasi faktor-faktor yang mempengaruhi attrition (karyawan keluar).
2. Membangun business dashboard untuk monitoring faktor-faktor tersebut.
3. Membuat model machine learning untuk membantu departemen HR
   
### ⚙️ Persiapan

Dataset yang digunakan adalah:

[Employee Attrition & Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Dataset ini berisi data historis tentang karyawan seperti usia, jenis kelamin, pendidikan, jabatan, tingkat kepuasan kerja, hingga apakah karyawan tersebut akhirnya keluar dari perusahaan.

Setup Environment - Anaconda
```
conda create --name myenv python=3.10
conda activate myenv
pip install -r requirements.txt
```
Setup Environment - Shell/Terminal
```
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
Untuk menjalankan proyek ini secara lokal, diperlukan environment Python dengan dependensi berikut:
```
pip install pandas numpy scikit-learn xgboost streamlit joblib
```
Struktur folder:
```
project/
│
├── model/
│   ├── model_xgb.joblib
│   ├── scaler.joblib
│   └── encoders.joblib
│
└──app.py         # File Streamlit
```
Langkah-langkah preprocessing dan pelatihan model disusun dalam notebook terpisah untuk eksperimen.

## 📊 Business Dashboard

Dashboard ini dibuat untuk membantu tim Human Resources (HR) dalam menganalisis faktor-faktor yang memengaruhi **tingginya angka attrition (resign)** karyawan di perusahaan. Visualisasi dibangun menggunakan **Tableau**, dengan menampilkan segmentasi attrition berdasarkan usia, jabatan, pendapatan bulanan, masa kerja, hingga departemen.

Dashboard menyediakan fitur interaktif berupa filter berdasarkan:
- Age
- Department
- Gender
- Job Level
- Job Role
- Job Satisfaction
- Marital Status

Berikut adalah tautan akses ke dashboard online:
**[👉 Lihat Dashboard Tableau](https://public.tableau.com/views/HRD_17470193340890/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**


## 🚀 Menjalankan Sistem Machine Learning
Untuk menjalankan prototype sistem prediksi risiko karyawan keluar, ikuti langkah berikut:
1. Clone repository atau salin semua file proyek ke dalam satu direktori.
2. Pastikan semua file model (.joblib) tersedia di folder model/.
3. Jalankan aplikasi Streamlit dengan perintah:
```
streamlit run app.py
or
python -m streamlit run app.py
```
4. Akses aplikasi melalui browser di:
```
http://localhost:8501
```
### 🔗 Akses Online Prototype

Prototype juga dapat diakses secara online melalui Streamlit Cloud:

[Link Streamlit](https://prediction-employee-attrition.streamlit.app/)

## ✅ Conclusion

Berdasarkan hasil visualisasi dan analisis data attrition:

- Departemen Research & Development menyumbang attrition tertinggi dengan jumlah 107 karyawan resign atau sebesar 59,78% dari keseluruhan.
- Job role dengan resign tertinggi adalah Laboratory Technician sebanyak 49 resign, Sales Executive 39 resign dan Research Scientist 38 resign.
- Resign paling banyak terjadi pada tingkat kepuasan kerja 1 dan 3.
- Sebagian besar resign terjadi pada karyawan dengan WLB level 2 (94 orang).
- Karyawan yang resign memiliki rata-rata gaji lebih rendah (4.873) dibanding yang bertahan (6.983).
- Usia dengan attrition tertinggi adalah 28–30 tahun, dengan puncak di usia 28 sebanyak 22 karyawan resign.
- Karyawan dengan pendapatan bulanan rendah (di bawah rata-rata) cenderung lebih banyak resign.

Berdasarkan analisis data employee attrition yang ditampilkan pada dashboard HRD, dapat disimpulkan bahwa perusahaan tengah menghadapi tantangan serius terkait tingkat pengunduran diri karyawan, khususnya pada departemen Sales dan beberapa peran teknis seperti Laboratory Technician serta Research Scientist. Meskipun tingkat kepuasan kerja dan work-life balance menjadi indikator penting, namun faktor seperti usia muda, gaji yang lebih rendah, serta masa kerja yang relatif singkat juga tampak sangat berpengaruh dalam keputusan resign. Karyawan dengan usia 28–30 tahun terlihat paling rentan untuk meninggalkan perusahaan.

Hal ini mengindikasikan bahwa selain faktor internal seperti kompensasi dan kondisi kerja, faktor eksternal seperti peluang karier atau dinamika pasar tenaga kerja juga turut memengaruhi keputusan tersebut.


### Rekomendasi Action Items

Untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan, berikut beberapa rekomendasi strategi yang dapat dilakukan oleh tim HR:

#### 🎯 Action Item 1: Review dan Revisi Struktur Gaji
Tinjau kembali struktur kompensasi, terutama pada role dengan gaji di bawah rata-rata. Pertimbangkan sistem insentif berbasis performa yang adil untuk semua divisi.

#### 🎯 Action Item 2: Program Retensi Karyawan
Bangun program engagement untuk karyawan muda dan baru, seperti coaching, mentorship, pengembangan karir untuk karyawan berusia di bawah 30 tahun. Ciptakan jalur pengembangan profesional yang jelas (career path clarity).

#### 🎯 Action Item 3: Peningkatan Program Work-Life Balance
Terapkan opsi kerja fleksibel atau hybrid (jika memungkinkan). Tambahkan program kesejahteraan seperti health & wellness benefits dan employee assistance program.

