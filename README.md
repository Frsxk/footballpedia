# Tugas 4 PBP: Implementasi Form dan Data Delivery pada Django

Tautan ke aplikasi PWS: https://muhammad-faza44-footballpedia.pbp.cs.ui.ac.id

# Checklist tugas

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Pengimplementasian fungsi-fungsi tersebut dapat dilakukan dengan membuat sebuah fungsi baru untuk setiap fitur yang ingin diimplementasikan di file `views.py`. Sebelum itu, siapkan *import* module yang akan digunakan, diantaranya:
```py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
```
Setelah melakukan import, buat 4 fungsi baru dengan nama yang sesuai dengan fitur yang akan diimplementasikan, yaitu `register(request)`, `login_user(request)`, dan `logout_user(request)`. Implementasinya adalah sebagai berikut:
```py
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    return response
```
Jangan lupa untuk menambahkan fungsi-fungsi tersebut ke `urls.py` di folder `./main/`. Lakukan import fungsi-fungsi tersebut terlebih dahulu dari `main.views`. Kemudian tambahkan path dengan format `path('fungsi/', nama_fungsi, name='fungsi')`, sesuaikan untuk setiap fungsi yang telah dibuat di atas tadi.

Untuk merestriksi akses ke halaman agar memerlukan login, cukup menambahkan decorator `@login_required(login_url='/login/')` di atas fungsi views yang ingin direstriksi. Untuk proyek ini, diberikan ke funsgi `show_main(request)` dan `show_product(request, id)`.

### Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Pembuatan akun dapat dilakukan dengan mengakses halaman register yang terletak di `/register/`. Isi username dengan nama user yang akan dibuat, kemudian buat password yang aman sesuai dengan ketentuan.

Untuk pembuatan *dummy data* (produk), log in ke salah satu user yang telah dibuat terlebih dahulu, kemudian klik tombol `+ Add Product`. Halaman akan berpindah ke `/create/`, dimana kita bisa membuat suatu data produk baru. Isi bagian yang kosong dengan informasi data yang sesuai, kemudian klik tombol `Add Product` di paling bawah untuk menyimpan produk ke database. Lakukan langkah ini 3 kali di tiap user.

### Menghubungkan model Product dengan User.
Untuk menghubungkan Product dengan User, lakukan modifikasi di file `models.py`. Tambahkan *import* class User dari `django.contrib.auth.models`. Buat sebuah variabel baru di dalam class Product:
```py
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```
Model Product dengan User sudah berhasil dihubungkan. Untuk implementasinya, kita bisa menambahkan *author* dari setiap produk. Modifikasi file `product_detail.html`. Tambahkan kode berikut ini setelah pemanggilan variabel `product.description`:
```py
{% if product.user %}
    <p>Product by: {{ product.user.username }}</p>
{% else %}
    <p>Product by: Anonymous</p>
{% endif %}
```
Langkah ini selesai.

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Untuk menampilkan informasi pengguna yang sedang *logged in* dan implementasi cookies di halaman utama, kita perlu menambahkan dua context tambahan di fungsi `show_main(request)` pada file `views.py`. Buat entri baru dengan key `'last_login'` dan value `request.COOKIES.get('last_login', 'Never')`, kemudian satu entri baru lagi dengan key `current_user` dan value `request.user`.

Selanjutnya, implementasi cookie dimulai dengan modifikasi fungsi `login_user(request)` di file yang sama. Tambahkan kode ini `response.set_cookie('last_login', str(datetime.datetime.now()))` dibawah definisi variabel response. Ini akan menyimpan sebuah cookie dengan nama `last_login` dengan valuenya adalah waktu saat ini dari *library* `datetime`. Kita juga perlu menghapus cookie saat user melakukan *log out*. Tambahkan kode `response.delete_cookie('last_login')` dibawah definisi variabel response pada fungsi `logout_user(request)` di file yang sama.

Terakhir, implementasi menampilkan detail informasi pengguna yang sedang *logged in* dilakukan dengan melakukan perubahan pada file `main.html` di folder `./main/templates/`. Kita bisa mendapatkan nama user (*username*) dari pengguna yang sedang login saat ini dengan pemanggilan variabel `current_user.username`. Contoh implementasinya adalah sebagai berikut:
`<h5>User saat ini: {{ current_user.username }}</h5>`. Langkah selesai.

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
#### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah sebuah form bawaan dari framework Django yang secara khusus dirancang untuk menangani proses login pengguna. Form ini memeriksa apakah username dan password yang dimasukkan oleh pengguna valid dan apakah akun pengguna tersebut aktif.

**Kelebihan:**
- **Keamanan Bawaan**. Sudah dilengkapi dengan proteksi terhadap serangan umum seperti *Cross-Site Request Forgery* (CSRF). Django secara otomatis akan menangani token CSRF.
- **Validasi Otomatis**. Secara otomatis memvalidasi apakah pengguna ada, kata sandi benar, dan akun pengguna berstatus aktif. Ini mengurangi jumlah kode yang perlu ditulis.
- **Terintegrasi dengan Baik**. Terintegrasi secara mulus dengan sistem autentikasi bawaan Django lainnya, seperti model User dan fungsi `login()`.

**Kekurangan:**
- **Kustomisasi Terbatas**. Meskipun bisa diperluas, melakukan kustomisasi yang signifikan (misalnya, menambahkan login dengan email sebagai pengganti username atau menambahkan field lain seperti CAPTCHA) bisa menjadi sedikit lebih rumit dibandingkan membuat form dari awal.
- **Tampilan Default Sederhana**. Tampilan visual bawaannya sangat dasar, sehingga perlu untuk menata sendiri menggunakan CSS agar sesuai dengan desain situs web.

#### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Secara sederhana, autentikasi adalah tentang siapa, sedangkan otorisasi adalah tentang apa yang boleh dilakukan.

**Autentikasi (*Authentication*)**: Ini adalah proses verifikasi identitas pengguna. Tujuannya adalah untuk memastikan bahwa seseorang adalah benar-benar seperti yang mereka klaim. Contoh paling umum adalah saat kita memasukkan username dan password untuk login. Sistem akan memeriksa apakah kredensial tersebut cocok dengan yang ada di database. Django memiliki sistem autentikasi yang sangat kuat dan lengkap yang berada di `django.contrib.auth`. Implementasinya meliputi Model `User`, yaitu model bawaan untuk menyimpan informasi pengguna seperti username, password (yang di-*hash*), email, nama depan, dan nama belakang. Forms, misalnya `AuthenticationForm` untuk login dan `UserCreationForm` untuk registrasi. Views, *view* bawaan untuk proses seperti login, logout, dan manajemen kata sandi.

**Otorisasi (*Authorization*)**: Ini adalah proses menentukan hak akses atau izin yang dimiliki oleh pengguna yang telah terautentikasi. Setelah sistem mengetahui siapa kita, otorisasi akan menentukan halaman mana yang bisa dilihat, data apa yang bisa diubah, atau tindakan apa yang bisa dilakukan. Contohnya, pengguna biasa mungkin hanya bisa membaca data, sedangkan administrator bisa membuat, membaca, mengubah, dan menghapus data (CRUD). Django juga menyediakan kerangka kerja otorisasi bawaan yang fleksibel, seperti `Permissions` (Izin), yaitu sistem izin bawaan yang memungkinkan untuk memberikan izin spesifik kepada pengguna atau grup. Setiap model Django secara otomatis membuat empat izin dasar: add, change, delete, dan view. `Groups` (Grup), digunakan untuk mengelompokkan pengguna ke dalam grup dan memberikan izin ke grup tersebut. Setiap pengguna dalam grup akan mewarisi semua izin dari grup tersebut. `Decorators`, Django menyediakan decorator seperti `@login_required` (untuk memastikan pengguna sudah login sebelum mengakses view) dan `@permission_required` (untuk memeriksa apakah pengguna memiliki izin spesifik).

#### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies dan sessions adalah dua mekanisme utama untuk menyimpan *state* (informasi) pengguna saat mereka bernavigasi di situs web, karena protokol HTTP sendiri bersifat *stateless* (tidak menyimpan informasi).

**Cookies**

**Kelebihan:**
- Penyimpanan di Sisi Klien: Disimpan di browser pengguna, sehingga tidak membebani server.
- Persisten: Cookies dapat diatur untuk bertahan lama (berhari-hari atau bahkan bertahun-tahun), sehingga cocok untuk mengingat preferensi pengguna atau status "ingat saya" saat login.
- Sederhana: Mudah dibuat dan dibaca baik di sisi klien (JavaScript) maupun sisi server.

**Kekurangan:**
- Ukuran Terbatas: Ukuran cookie sangat terbatas (biasanya sekitar 4KB), jadi tidak bisa digunakan untuk menyimpan data yang besar.
- Tidak Aman untuk Data Sensitif: Karena disimpan di sisi klien, data dalam cookie dapat dilihat dan dimanipulasi oleh pengguna. Oleh karena itu, sangat tidak disarankan menyimpan informasi sensitif seperti password di dalamnya.
- Dikirim di Setiap Request: Cookies dikirimkan ke server pada setiap permintaan HTTP, yang dapat sedikit menambah overhead pada bandwidth.

**Sessions**

**Kelebihan:**
- Lebih Aman: Data sesi disimpan di sisi server, sehingga jauh lebih aman. Browser klien hanya menyimpan ID sesi (*session ID*) dalam sebuah cookie untuk identifikasi.
- Ukuran Lebih Besar: Karena data disimpan di server, tidak ada batasan ukuran praktis seperti pada cookies. Kita bisa menyimpan objek yang kompleks.
- Kontrol di Sisi Server: Server memiliki kontrol penuh atas masa berlaku dan data sesi.

**Kekurangan:**
- Membebani Server: Setiap sesi pengguna aktif akan menggunakan memori atau ruang penyimpanan di server. Jika situs memiliki banyak pengguna secara bersamaan, ini bisa menjadi masalah skalabilitas.
- Kompleksitas Skalabilitas: Dalam lingkungan dengan banyak server (*load balancing*), manajemen sesi menjadi lebih kompleks karena sesi yang dibuat di satu server harus dapat diakses oleh server lainnya. Ini biasanya memerlukan solusi penyimpanan sesi terpusat seperti Redis atau database.

#### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
**Tidak**, penggunaan cookies tidak aman secara *default*. Ada beberapa risiko potensial yang harus diwaspadai:
1. **Pencurian Cookie (Cookie Theft/Hijacking)**: Jika seorang penyerang mendapatkan cookie sesi browser (misalnya melalui serangan Cross-Site Scripting (XSS) atau dengan mengendus lalu lintas jaringan yang tidak terenkripsi), mereka dapat meniru dan mendapatkan akses ke akun kita.
2. **Cross-Site Request Forgery (CSRF)**: Penyerang dapat membuat situs web berbahaya yang memaksa browser yang sudah terautentikasi untuk mengirim permintaan ke situs web lain tanpa sepengetahuan kita, memanfaatkan cookie yang tersimpan.
3. **Manipulasi Data**: Karena cookies disimpan di klien, pengguna (atau penyerang) dapat dengan mudah mengubah isinya jika tidak dilindungi dengan benar.

Django sangat serius dalam hal keamanan dan menyediakan beberapa mekanisme bawaan untuk mengatasi risiko-risiko ini:
- **Signed Cookies**: Untuk cookie sesi (*session cookie*), Django tidak menyimpan data sesi langsung di cookie. Sebaliknya, ia hanya menyimpan ID sesi yang tidak berarti apa-apa dengan sendirinya. Untuk cookies lain yang  diatur secara manual, Django menggunakan *cryptographic signing*(penandatanganan kriptografis). Artinya, Django menambahkan tanda tangan digital ke cookie. Jika seseorang mencoba mengubah isi cookie, tanda tangannya menjadi tidak valid, dan Django akan menolak cookie tersebut.
- **Atribut HttpOnly**: Django mengatur atribut HttpOnly pada cookie sesi secara *default*. Atribut ini memberi tahu browser bahwa cookie tersebut tidak boleh diakses oleh skrip sisi klien (JavaScript). Ini adalah mitigasi yang sangat efektif terhadap pencurian cookie melalui serangan XSS.
- **Proteksi CSRF Bawaan**: Django memiliki salah satu sistem perlindungan CSRF terbaik. Ia bekerja dengan memeriksa token rahasia yang unik untuk setiap pengguna pada setiap permintaan POST. Ini memastikan bahwa permintaan tersebut berasal dari situs ini sendiri dan bukan dari situs berbahaya pihak ketiga.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Sudah ditulis di atas.

### Melakukan add-commit-push ke GitHub.
Selesai.
