# Tugas 3 PBP: Implementasi Form dan Data Delivery pada Django

Tautan ke aplikasi PWS: https://muhammad-faza44-footballpedia.pbp.cs.ui.ac.id

# Checklist tugas

### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Membuat fungsi baru pada file `views.py` di folder main bernama `show_xml` dan `show_json` dengan parameter `request`. Kedua fungsi tersebut memiliki isi yang hampir sama, dimulai dengan membuat variabel `shop_list` yang mengambil semua produk yang dijual. Buat variabel `(type)_data` dengan *type* xml atau json sesuai dengan fungsi, yang diisi dengan method `serialize` dari library `django.core`. Kembalikan data berbentuk `Httpresponse` di akhir dengan `content_type="application/(type)` sesuai dengan tipe fungsi. Untuk fungsi `show_(type)_by_id`, tambahkan satu parameter lagi, yaitu `shop_id`. Gunakan **try_except** untuk memfilter apakah shop dengan id tersebut ada atau tidak. Jika tidak, kembalikan *response status* 404 Not Found. Untuk mencari produk dengan id, gunakan `Shop.objects.filter(pk=shop_id)`. parameter `pk` dalam method filter berarti *primary key*, dan memasukkan id yang akan dicari.

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
Melanjutkan poin 1, routing URL akan dilakukan di file `urls.py` di folder main. Lakukan import terlebih dahulu untuk semua fungsi yang baru dibuat. Buat path baru dengan format `path('path/to/', function, name='nama')`. Isi path/to/ dengan path yang ingin dibuat, misal untuk fungsi `show_xml` memiliki path `xml/`. Isi *function* dengan fungsi yang sesuai. Samakan parameter `name` dengan nama fungsinya. Routing sudah berhasil. 

### Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
Hal pertama yang perlu dilakukan adalah membuat template paling dasar untuk semua halaman yang nanti akan diimplementasikan. Buat sebuah folder baru di root project bernama `templates`, kemudian buat file `base.html`. Isi file tersebut dengan kode berikut ini:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>

<body>
    {% block content %} {% endblock content %}
</body>
</html>
```
Ini adalah kerangka utama untuk setiap halaman yang akan dibuat selanjutnya. Isinya tidak lebih dari menggunakan `html:5` dari Emmet Abbrevation. Tambahkan `{% block var %} {% endblock var %}` dengan var adalah key yang nanti dapat digunakan di implementasinya.

Setelah selesai membuat kerangka, implementasikan untuk file `main.html` di folder `main/templates/`. Tambahkan kode sedemikian hingga sesuai dengan yang diminta di soal, seperti inilah yang saya buat:
```html
{% extends "base.html" %}
{% block content %}

<h5>Nama Aplikasi:</h1>
<p>{{ application_name }}</p>
<h5>Nama:</h1>
<p>{{ name }}</p>
<h5>Kelas:</h1>
<p>{{ class }}</p>

<a href="{% url 'main:create_shop' %}">
    <button>+ Add Product</button>
</a>

<hr>

{% if not shop_list %}
<p>Belum ada produk yang ditambahkan.</p>
{% else %}

{% for shop in shop_list %}
<div>
    <a href="{% url 'main:show_shop' shop.id %}">
        <h2>{{ shop.name }}</h2>
    </a>

    <p><b>{{ shop.get_category_display }}</b>{% if shop.is_featured %} | 
    <b>Featured</b>{% endif %} | Rating: {{ shop.rating }} ⭐</p>

    {% if shop.thumbnail %}
    <img src="{{ shop.thumbnail }}" alt="Thumbnail" width="150px" height-auto>
    <br />
    {% endif %}

    <p>{{ shop.description|truncatewords:25 }}...</p>

    <p><a href="{% url 'main:show_shop' shop.id %}"><button>See Details</button></a></p>
</div>
<hr>
{% endfor %}
{% endif %}
{% endblock content %}
```
Setiap `{% xxx %}` merepresentasikan sebuah pemanggilan fungsi tertentu dari Django misalnya `{% url 'main:show_shop' shop.id %}` akan melakukan *redirect* ke halaman detail produk yang sesuai dengan `shop.id`, atau bisa juga untuk mengakses nilai dari suatu variabel, misalnya `shop.thumbnail`. Untuk membuat sebuah tombol, gunakan tag `<button>`.

### Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
Buat file html baru untuk halaman form di folder `main/templates/`, dengan nama `create_shop.html`. Isi file tersebut dengan implementasi dari file `base.html` di awal, seperti sebagai berikut:
```html
{% extends "base.html" %}
{% block content %}

<h1>Add New Product</h1>
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" value="Add Product"></td>
        </tr>
    </table>

{% endblock content %}
```
Kode tersebut akan membuat form secara otomatis menggunakan `form.as_table`. Jangan lupa untuk menambahkan fungsi `{% csrf_token %}` di awal form untuk alasan keamanan. Lakukan *set up* csrf di file `settings.py` di folder footballpedia, tambahkan kode berikut: `CSRF_TRUSTED_ORIGINS = ["https://link-to-deployed-url/]`, dengan *link* yang diisi dengan tautan ke aplikasi pws yang sudah di-*deploy*.

### Membuat halaman yang menampilkan detail dari setiap data objek model.
Lakukan hal yang sama di langkah sebelumnya. Buat file `shop_detail.html` di folder `main/templates/`. Isi dengan kode berikut ini:
```html
{% extends "base.html" %}
{% block content %}

<p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

<h1>{{ shop.name }}</h1>
<p><b>{{ shop.get_category_display }}</b>{% if shop.is_featured %} | 
    <b>Featured</b>{% endif %} | Rating: {{ shop.rating }} ⭐ | {{ shop.quantity }} sold</p>

{% if shop.thumbnail %}
<img src="{{ shop.thumbnail }}" alt="shop thumbnail" width="300">
<br /><br />
{% endif %}

<p>{{ shop.description }}</p>

{% endblock content %}
```
Sesuaikan pemanggilan variabel dengan lokasinya, tambahkan *redirect* untuk kembali ke halaman utama. Sesuaikan pula ukuran gambar `thumbnail` dalam tag `<img>` dalam ukuran piksel (px).

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan *data delivery* dalam pengimplementasian sebuah *platform* karena data itu sendiri adalah nyawa dari *platform*. Tanpa mekanisme pengiriman data yang andal dan efisien, *platform* tersebut tidak lebih dari sekadar tampilan kosong yang tidak fungsional. *Platform* tersebut menjadi tidak bisa menyajikan informasi, merespons pengguna, atau menjalankan proses bisnis.

#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, data dalam bentuk JSON lebih baik daripada XML, karena JSON bisa lebih cepat daripada XML dan memiliki kompabilitas penuh dengan JavaScript. JSON lebih populer dibanding XML karena proses parsing yang lebih cepat dan efisien, mudah dibaca dan ditulis, juga struktur data yang  fleksibel.

#### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi utama dari method is_valid() pada form Django adalah untuk memvalidasi data yang dikirim oleh pengguna. Method ini akan menjalankan pemeriksaan keamanan pada form sebelum dikirim, agar data dapat dikirim secara aman.

#### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token saat membuat form di Django sebagai mekanisme keamanan untuk mencegah serangan CSRF (Cross-Site Request Forgery). Token ini memastikan bahwa permintaan, seperti pengiriman form, yang diterima oleh server akan benar-benar berasal dari situs web yang sesuai dan diinisiasi oleh pengguna secara sadar, bukan dari situs lain yang berbahaya.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Sudah ditulis di atas.

#### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sejauh ini kinerja tim asisten dosen sudah baik, tidak ada yang perlu diperbaiki.

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![http://127.0.0.1:8000/json/](https://i.ibb.co.com/5Xrzr5fW/image-2025-09-16-215141647.png)
![http://127.0.0.1:8000/xml/](https://i.ibb.co.com/840x9qkr/image-2025-09-16-215508316.png)
![http://127.0.0.1:8000/json/cca301b5-97cb-4a1d-9567-54436d356715/](https://i.ibb.co.com/PZJpmpnW/image-2025-09-17-064458957.png)
![http://127.0.0.1:8000/xml/cca301b5-97cb-4a1d-9567-54436d356715/](https://i.ibb.co.com/PzcN0GR2/image-2025-09-17-064239393.png)

### Melakukan add-commit-push ke GitHub.
Selesai.
