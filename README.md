# Tugas 2 PBP: Implementasi Model-View-Template (MVT) pada Django

Tautan ke aplikasi PWS: 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Membuat sebuah proyek Django baru.
Langkah-langkah untuk membuat proyek Django baru sangat *straigtforward*. Diawali dengan membuat folder baru, untuk proyek saya diberi nama 'footballpedia'. Aktifkan python virtual environment dengan perintah `python -m venv env`  kemudian `env\Scripts\activate`. Buat folder 'requirements.txt' yang berisi *dependencies* yang perlu di-instal. Lakukan penginstalan dengan menjalankan perintah `pip install -r requirements.txt`. Langkah terakhir adalah membuat proyek Django dengan perintah `django-admin startproject footballpedia .` dengan 'footballpedia' adalah nama proyek saya.

#### Membuat aplikasi dengan nama main pada proyek tersebut.


#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.


#### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
- `name` sebagai nama item dengan tipe CharField.
- `price` sebagai harga item dengan tipe IntegerField.
- `description` sebagai deskripsi item dengan tipe TextField.
- `thumbnail` sebagai gambar item dengan tipe URLField.
- `category` sebagai kategori item dengan tipe CharField.
- `is_featured` sebagai status unggulan item dengan tipe BooleanField.



#### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.


#### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.


####  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.


#### Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy



- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.



- Jelaskan peran settings.py dalam proyek Django!



- Bagaimana cara kerja migrasi database di Django?



- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?



- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?


