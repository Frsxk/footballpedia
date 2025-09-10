# Tugas 2 PBP: Implementasi Model-View-Template (MVT) pada Django

Tautan ke aplikasi PWS: https://muhammad-faza44-footballpedia.pbp.cs.ui.ac.id

### Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Membuat sebuah proyek Django baru.
Langkah-langkah untuk membuat proyek Django baru sangat *straigtforward*. Diawali dengan membuat folder baru, untuk proyek saya diberi nama 'footballpedia'. Aktifkan python virtual environment dengan perintah `python -m venv env`  kemudian `env\Scripts\activate`. Buat folder 'requirements.txt' yang berisi *dependencies* yang perlu di-instal. Lakukan penginstalan dengan menjalankan perintah `pip install -r requirements.txt`. Langkah selanjutnya adalah membuat proyek Django dengan perintah `django-admin startproject footballpedia .` dengan 'footballpedia' adalah nama proyek saya. Tambahkan environment variable di file `.env` dan `.env.prod` untuk produksi. Modifikasi file `settings.py` dengan menambahkan kode untuk membaca file `.env`. Tambahkan konfigurasi di `settings.py` untuk production. Ubah pula pengaturan untuk konfigurasi database agar menggunakan data dari `.env.prod` di mode production dan menggunakan database SQLite biasa untuk development. Pembuatan proyek Django baru selesai.

#### Membuat aplikasi dengan nama main pada proyek tersebut.
Langkah awal untuk membuat aplikasi dengan nama main adalah mengaktifkan python virtual environment terlebih dahulu (perintah ada di checklist sebelumnya), kemudian menjalankan perintah `python manage.py startapp main` di folder utama. Tambahkan `'main'` ke dalam installed_apps di `settings.py` pada folder footballpedia. Pembuatan aplikasi dengan nama main selesai.

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Untuk melakukan routing pada proyek, buat file `urls.py` di folder main terlebih dahulu. Isi kode berikut ini:
```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Selanjutnya, buka file `urls.py` di folder footballpedia. Impor fungsi `include` dari `django.urls`. Tambahkan rute `path('', include('main.urls')),` ke variabel `url_patterns`. Routing berhasil dilakukan.

#### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
- `name` sebagai nama item dengan tipe CharField.
- `price` sebagai harga item dengan tipe IntegerField.
- `description` sebagai deskripsi item dengan tipe TextField.
- `thumbnail` sebagai gambar item dengan tipe URLField.
- `category` sebagai kategori item dengan tipe CharField.
- `is_featured` sebagai status unggulan item dengan tipe BooleanField.

Lakukan perubahan pada file `models.py` di folder main. Impor library `uuid` untuk membuat id unik. Tambahkan semua atribut yang wajib dibuat, sesuaikan dengan jenis tipe modelnya. Buat pula variabel category_choices untuk jenis kategori yang dapat dipilih. Pembuatan model pada aplikasi main selesai.

#### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Pertama, buat folder `template` dalam folder main, kemudian buat file `main.html` dalam folder tersebut. Gunakan html:5 dari Emmet Abbrevation untuk membuat kerangka file HTML kosong. Tambahkan heading dan paragraph yang sesuai, isi dengan variabel yang akan dibuat di `views.py`. Di file `views.py`, buat sebuah fungsi `show_main(request)` yang berisi variabel `context` bertipe dictionary, dengan key berupa nama variabel yang akan dibuat dan value adalah isi dari variabel tersebut. Tambahkan kode `return render(request, "main.html", context)` di bawah deklarasi variabel context. Langkah ini selesai.

#### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Sudah dilakukan di 2 langkah sebelumnya.

####  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Untuk melakukan deployment, buka Pacil Web Service dan buat sebuah aplikasi baru, simpan kredisial untuk login. Jalankan perintah yang sudah tertera di PWS. Masukkan kredisial yang sebelumnya dibuat. Buka aplikasi yang baru dibuat di sebelah kiri pada PWS. Pergi ke bagian Environs, copy paste `.env.prod` pada proyek ke raw editor di PWS. Tambahkan url yang menuju web yang sudah di-deploy ke file `settings.py`. Commit perubahan baru, dan push ke pws. Penting untuk diingat, langkah ini harus dilakukan **setelah** git diinisialisasi di proyek.

#### Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy
File ini adalah README.md


- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Berikut adalah bagan alur permintaan (request) dan respon dalam aplikasi Django:

```
[Client/Browser] -> HTTP Request -> [urls.py] -> [views.py] -> [models.py] -> [Database]
        ^                                            |              |
        |                                            |              V
        +----------- HTTP Response <-----------------+-------- [template.html]
```

**Penjelasan Alur:**

1.  **Client Request**: Pengguna melakukan aksi di browser, seperti mengetik URL atau mengklik tautan. Browser mengirimkan sebuah HTTP Request ke server Django.
2.  **`urls.py`**: Django menerima request dan pertama kali melihat file `urls.py` pada proyek. File ini bertindak sebagai "penunjuk arah". Django akan mencari pola URL yang cocok dengan path yang diminta oleh client. Jika ditemukan, Django akan meneruskan request ke fungsi view yang terkait.
3.  **`views.py`**: Setelah `urls.py` menemukan view yang sesuai, fungsi di dalam `views.py` akan dieksekusi. File ini berisi logika bisnis aplikasi. Fungsi view akan memproses request, berinteraksi dengan model jika perlu, dan memutuskan data apa yang akan ditampilkan.
4.  **`models.py`**: Jika view perlu mengambil atau memanipulasi data dari database (misalnya, mengambil daftar produk), ia akan berkomunikasi dengan `models.py`. File ini mendefinisikan struktur data aplikasi dan menyediakan cara untuk berinteraksi dengan database (membuat, membaca, memperbarui, menghapus data) tanpa perlu menulis query SQL secara langsung.
5.  **`template.html`**: Setelah view mendapatkan data yang diperlukan dari model, ia akan meneruskan data tersebut ke sebuah file template HTML. Template ini berisi struktur halaman web dan menggunakan sintaks khusus Django untuk menampilkan data yang diterima dari view secara dinamis.
6.  **HTTP Response**: Fungsi view me-*render* template dengan data yang ada, menghasilkan sebuah halaman HTML lengkap. Halaman HTML ini kemudian dikirim kembali ke browser client sebagai HTTP Response. Browser akan menampilkan halaman tersebut kepada pengguna.

- Jelaskan peran settings.py dalam proyek Django!

File `settings.py` adalah pusat konfigurasi untuk sebuah proyek Django. File ini berisi semua pengaturan yang diperlukan agar aplikasi dapat berjalan, mulai dari konfigurasi database hingga daftar aplikasi yang terpasang. Peran utamanya adalah sebagai "papan kontrol" proyek, di mana pengembang dapat menyesuaikan perilaku Django.

Beberapa peran kunci dari `settings.py` antara lain:
- **`INSTALLED_APPS`**: Mendaftarkan semua aplikasi yang digunakan dalam proyek, baik itu aplikasi bawaan Django, aplikasi pihak ketiga, maupun aplikasi yang kita buat sendiri (seperti aplikasi `main`).
- **`DATABASES`**: Mengatur koneksi ke database. Di sinilah kita menentukan jenis database yang digunakan (misalnya, SQLite, PostgreSQL), nama database, serta kredensial untuk mengaksesnya.
- **`SECRET_KEY`**: Menyimpan kunci rahasia yang digunakan untuk keamanan kriptografi, seperti untuk sesi (*sessions*) dan token CSRF.
- **`DEBUG`**: Sebuah flag boolean yang mengaktifkan atau menonaktifkan mode debug. Saat `DEBUG=True`, Django akan menampilkan halaman *error* yang detail, yang sangat membantu saat pengembangan. Nilai ini harus `False` di lingkungan produksi.
- **`ALLOWED_HOSTS`**: Menentukan daftar nama domain atau alamat IP yang diizinkan untuk melayani aplikasi Django ini.
- **`STATIC_URL` dan `STATICFILES_DIRS`**: Mengonfigurasi cara Django menangani file statis seperti CSS, JavaScript, dan gambar.
- **`TEMPLATES`**: Mengatur *template engine* dan lokasi direktori tempat file-file template HTML disimpan.
- **`MIDDLEWARE`**: Mendaftarkan kelas-kelas *middleware* yang memproses *request* dan *response* secara global, seperti untuk otentikasi, keamanan, dan manajemen sesi.

Secara singkat, `settings.py` adalah file yang menyatukan semua bagian dari proyek Django dan mendefinisikan bagaimana mereka harus berinteraksi satu sama lain.

- Bagaimana cara kerja migrasi database di Django?

Sistem migrasi Django adalah cara untuk mengelola perubahan skema database secara terstruktur dan terversioning, sejalan dengan perubahan pada file `models.py`. Proses ini pada dasarnya adalah sistem kontrol versi untuk struktur database Anda. Cara kerjanya dapat dibagi menjadi dua langkah utama:

1.  **`python manage.py makemigrations`**
    -   Ketika Anda menjalankan perintah ini, Django akan memeriksa file `models.py` di setiap aplikasi Anda.
    -   Django membandingkan keadaan model Anda saat ini dengan versi yang disimpan dalam file migrasi terakhir yang ada di direktori `migrations/` aplikasi tersebut.
    -   Jika Django mendeteksi adanya perubahan (seperti penambahan field baru, penghapusan model, atau modifikasi atribut field), ia akan membuat file Python baru di dalam direktori `migrations/` (contoh: `0002_auto_...py`).
    -   File ini bukanlah perintah SQL, melainkan sebuah "resep" atau deskripsi deklaratif tentang perubahan yang perlu dilakukan. Ini membuat migrasi bersifat *database-agnostic*, artinya file migrasi yang sama dapat diterapkan pada database yang berbeda (misalnya, SQLite, PostgreSQL, MySQL).

2.  **`python manage.py migrate`**
    -   Perintah ini adalah yang benar-benar menerapkan perubahan ke database.
    -   Django akan melihat tabel khusus di database Anda yang bernama `django_migrations`. Tabel ini mencatat migrasi mana yang sudah diterapkan.
    -   Django kemudian memeriksa file-file di direktori `migrations/` dan membandingkannya dengan catatan di tabel `django_migrations`.
    -   Untuk setiap file migrasi yang belum diterapkan, Django akan menerjemahkan "resep" Python dari file tersebut menjadi perintah SQL yang sesuai untuk database yang Anda gunakan (yang dikonfigurasi di `settings.py`).
    -   Terakhir, Django mengeksekusi perintah SQL tersebut pada database, sehingga mengubah skema (misalnya, membuat tabel baru, menambahkan kolom, dll.) agar sesuai dengan definisi di `models.py`.

Singkatnya, `makemigrations` membuat rencana perubahan berdasarkan model Anda, dan `migrate` melaksanakan rencana tersebut untuk mengubah struktur database Anda.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan titik awal yang sangat baik untuk pembelajaran pengembangan perangkat lunak, khususnya pengembangan web, karena beberapa alasan kuat:

1.  **Filosofi "Batteries-Included"**: Django hadir dengan banyak fungsionalitas yang sudah siap pakai, seperti panel admin, sistem otentikasi pengguna, dan ORM (Object-Relational Mapper). Ini memungkinkan pemula untuk fokus pada pemahaman konsep inti pengembangan web (seperti alur request-response dan model data) tanpa harus bingung memilih dan mengintegrasikan banyak pustaka dari pihak ketiga untuk tugas-tugas umum.
2.  **Struktur yang Jelas dan Terorganisir**: Django menerapkan arsitektur Model-View-Template (MVT) yang mendorong pemisahan yang jelas antara logika bisnis (views), struktur data (models), dan presentasi (templates). Struktur yang terdefinisi dengan baik ini sangat membantu pemula untuk memahami bagaimana berbagai komponen aplikasi web saling berhubungan dan membangun kebiasaan pengkodean yang baik.
3.  **ORM yang Intuitif**: Django ORM memungkinkan pengembang berinteraksi dengan database menggunakan kode Python, bukan SQL mentah. Bagi pemula, ini secara signifikan menyederhanakan operasi database dan mengurangi kemungkinan kesalahan. Mereka dapat membuat, membaca, memperbarui, dan menghapus data dengan cara yang lebih mudah dipahami.
4.  **Dokumentasi Luar Biasa**: Django memiliki salah satu dokumentasi terbaik di dunia *open-source*. Dokumentasinya sangat lengkap, terstruktur dengan baik, dan menyertakan tutorial langkah-demi-langkah yang sangat bagus untuk pemula, serta referensi mendalam untuk pengguna tingkat lanjut.
5.  **Panel Admin Otomatis**: Salah satu fitur unggulan Django adalah panel admin yang dibuat secara otomatis dari model data Anda. Fitur ini sangat berharga bagi pemula karena memungkinkan mereka untuk dengan cepat mengelola data aplikasi (CRUD - Create, Read, Update, Delete) melalui antarmuka web tanpa perlu menulis kode tambahan.
6.  **Keamanan Bawaan**: Django secara default menyediakan perlindungan terhadap banyak kerentanan web umum seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), dan SQL Injection. Ini menanamkan praktik keamanan yang baik sejak awal, bahkan sebelum pemula sepenuhnya memahami ancaman tersebut.

Kombinasi dari kurva belajar yang landai, struktur yang terarah, dan kelengkapan fitur menjadikan Django pilihan yang sangat efektif untuk memperkenalkan konsep-konsep fundamental pengembangan perangkat lunak secara praktis dan komprehensif.

- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Sampai saat ini, asisten dosen tutorial 1 sangat baik, membantu mahasiswa jika ada kesulitan, dan *standby* di Discord pada saat pengerjaan lab.
