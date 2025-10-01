# Tugas 5 PBP: Desain Web menggunakan HTML, CSS dan Framework CSS

Tautan ke aplikasi PWS: https://muhammad-faza44-footballpedia.pbp.cs.ui.ac.id

# Checklist tugas

### Implementasikan fungsi untuk menghapus dan mengedit product.
Untuk menambahkan fitur baru ini, buka file `views.py` di folder `main`, kemudian tambahkan 2 fungsi baru. 

Pertama, fungsi `edit_product(request, id)` dengan implementasinya adalah mencari produk menggunakan id, kemudian ambil `ProductForm()` dari `forms.py` yang isinya sama dengan saat kita menambahkan produk. Kemudian simpan form, buat menjadi context dan return render ke `edit_product.html`. Buat halaman `edit_product.html` di folder `main/templates/`, isi kontennya mirip dengan `create_product.html`.

Kedua, fungsi `delete_product(request, id)` dengan implementasinya adalah mencari produk menggunakan id, kemudian panggil method `delete()` pada object tersebut. Kembalikan `HttpResponseRedirect` ke halaman utama. Langkah ini selesai

### Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

#### Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.

Semua implementasi desain menggunakan Tailwind CSS saya berdasarkan dokumentasi dari website https://tailwindcss.com/docs/. 

#### Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
- Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.

Implementasi ini dapat dilakukan dengan pengecekan `if` pada file `main.html`. Kita bisa mengecek apakah `product_list` masih kosong atau sudah ada isinya, kemudian tambahkan desain menggunakan Tailwind CSS.

- Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).

Lanjutkan dari implementasi sebelumnya, tapi yang ini dimasukkan ke bagian `else`. Kita bisa menampilkan tiap produk dengan menggunakan `for product in product_list`, kemudian sesuaikan desain *card* menggunakan Tailwind CSS. Buat tiap kartu ada di sebuah grid agar kartu dapat menyesuaikan tempatnya masing-masing dan membuat website menjadi responsif di semua perangkat.

- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

Masih melanjutkan kode sebelumnya, di setiap kartu saya menambahkan 3 tombol, yaitu details, edit, dan delete. Tiap implementasinya sudah ada di `main.html` di bagian komentar `Action Buttons`. Untuk tombol edit dan delete, hanya pengguna yang membuat produk tersebut yang bisa melihatnya. Gunakan `if` untuk pengecekan user yang benar.

- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Untuk membuat navbar (atau elemen apapun) menjadi responsif, kita bisa menambahkan tag yang memberi tahu css agar menyesuaikan, seperti `md:` untuk *device* ukuran *medium* (biasanya laptop atau desktop) atau `sm:` untuk *device* ukuran *small*.

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

#### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritasnya adalah Inline Styles (menambahkan atribut styles di tag secara langsung), ID selector (eksternal atau internal css yang menggunakan selector #), terakhir class dan element selector (eksternam atau internal css menggunakan selector . atau nama tag langsung, misal `p`).

#### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design menjadi konsep yang krusial karena memastikan sebuah aplikasi web dapat memberikan tampilan dan pengalaman pengguna (UX) yang optimal di berbagai perangkat dengan ukuran layar yang berbeda, mulai dari desktop, tablet, hingga smartphone.

Tanpa desain yang responsif, pengguna perangkat mobile akan dipaksa melihat versi desktop dari sebuah situs, yang mengakibatkan teks menjadi terlalu kecil, gambar tidak proporsional, dan navigasi menjadi sangat sulit karena harus terus-menerus melakukan pinch-and-zoom.

#### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**Margin** adalah ruang transparan di luar elemen, **padding** adalah ruang di dalam elemen (antara konten dan border), dan **border** adalah garis yang membingkai elemen di antara margin dan padding. Ketiganya adalah komponen fundamental dari **CSS Box Model**, yang mendefinisikan bagaimana elemen HTML dirender di halaman.

Untuk contoh implementasinya, misal kita mempunyai tag berikut di file html:
```html
<div class="box">
    Konten di dalam box.
</div>
```
Implementasi margin, padding, dan border jika menggunakan CSS adalah sebagai berikut:
```css
.box {
  /* Padding: 20px di semua sisi (atas, kanan, bawah, kiri) */
  padding: 20px;

  /* Border: tebal 2px, jenis solid (garis lurus), warna hitam */
  border: 2px solid black;

  /* Margin: 30px di semua sisi untuk memberi jarak dengan elemen lain */
  margin: 30px;
}
```
Jika menggunakan Tailwind CSS, class yang ditambahkan berikut ini dapat digunakan untuk implementasi yang sama:
```html
<div class="
  p-5
  border-2
  border-black
  m-8">
  Konten di dalam box.
</div>
```

#### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
*Flexbox* adalah model layout untuk mengatur item dalam satu dimensi (baik sebagai baris atau kolom), sedangkan *Grid* adalah model layout untuk mengatur item dalam dua dimensi (baris dan kolom secara bersamaan). Keduanya adalah alat modern di CSS untuk menggantikan metode layout lama (seperti float dan position) yang lebih rumit.

Flexbox sangat ideal untuk komponen aplikasi dan layout skala kecil, seperti:
- Navigation Bar: Meratakan item menu secara horizontal dan memberikan jarak yang sama di antaranya.
- Centering Content: Memusatkan sebuah item secara vertikal dan horizontal dengan mudah.
- Card Layout: Membuat daftar kartu (misalnya, produk di e-commerce) yang berbaris rapi dan bisa turun ke baris berikutnya (wrapping) jika tidak muat.
- Form Controls: Menyejajarkan label dan input field dalam sebuah formulir.

Sementara itu, grid sangat cocok untuk layout halaman web secara keseluruhan, seperti:
- Layout Halaman Utama: Mengatur struktur utama halaman seperti header, sidebar, konten utama, dan footer.
- Galeri Gambar: Membuat galeri dengan gambar berukuran berbeda yang tetap tersusun rapi dalam baris dan kolom.
- Formulir Kompleks: Mengatur tata letak formulir yang rumit di mana label dan input perlu sejajar di kedua sumbu.
- Dashboard: Membangun antarmuka dashboard dengan banyak widget yang perlu diatur dalam tata letak kisi yang ketat.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Sudah ditulis di atas.

### Melakukan add-commit-push ke GitHub.
Selesai.
