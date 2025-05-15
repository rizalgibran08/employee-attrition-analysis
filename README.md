# Monitoring Attrition of Employee

# 🔰 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

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

Setup environment:

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
1. Clone repository (jika tersedia di GitHub) atau salin semua file proyek ke dalam satu direktori.
2. Pastikan semua file model (.joblib) tersedia di folder model/.
3. Jalankan aplikasi Streamlit dengan perintah:
```
streamlit run app.py
```
4. Akses aplikasi melalui browser di:
```
http://localhost:8501
```
### 🔗 Akses Online Prototype

Prototype juga dapat diakses secara online melalui Streamlit Cloud:

[Link Streamlit]()

## ✅ Conclusion

Berdasarkan hasil visualisasi dan analisis data attrition:

- Kelompok usia 26–34 tahun menunjukkan tingkat attrition yang paling tinggi.
- Karyawan dengan pendapatan bulanan rendah (di bawah rata-rata) cenderung lebih banyak resign.
- Masa kerja di bawah 5 tahun juga memiliki korelasi tinggi terhadap angka resign.
- Departemen **Sales** memiliki proporsi attrition terbesar dibanding HR dan R&D.
- Status pernikahan dan gender juga menunjukkan variasi dalam angka attrition, karyawan yang melakukan resign kerbanyakan masih berstatus single.

Hal ini menunjukkan bahwa faktor keuangan, pengalaman kerja awal, dan dinamika per departemen menjadi penentu utama dalam tingginya tingkat turnover.


### Rekomendasi Action Items

Untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan, berikut beberapa rekomendasi strategi yang dapat dilakukan oleh tim HR:

#### 🎯 Action Item 1: Review dan Revisi Struktur Gaji
Lakukan evaluasi terhadap struktur gaji terutama pada posisi entry-level atau dengan masa kerja < 5 tahun. Pertimbangkan penyesuaian gaji berbasis performa dan kompetensi, terutama untuk departemen dengan attrition tinggi seperti Sales.

#### 🎯 Action Item 2: Program Retensi dan Keterlibatan Karyawan
Bangun program engagement untuk karyawan muda dan baru, seperti coaching, mentorship, pengembangan karir, dan keseimbangan kerja–hidup (work-life balance). Fokus pada kelompok usia 26–35 tahun dan jabatan level menengah ke bawah.

