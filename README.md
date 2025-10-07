# Tugas 6 PBP: Javascript dan AJAX

Tautan ke aplikasi PWS: https://muhammad-faza44-footballpedia.pbp.cs.ui.ac.id

# Checklist tugas

### Mengubah fitur - fitur tugas sebelumnya menggunakan AJAX

#### Fitur CRUD (Create Read Update Delete) product menggunakan AJAX (tidak boleh menggunakan dari context render kecuali untuk keperluan AJAX)

**Create (Tambah Product):**
1. Membuat view `add_product_entry_ajax` di `views.py` dengan decorator `@csrf_exempt` dan `@require_POST`
2. Menambahkan URL path `create-product-ajax/` di `urls.py`
3. Membuat modal form di `modal.html` dengan field sesuai model Product
4. Menggunakan `fetch()` API untuk mengirim data form ke server tanpa reload halaman
5. Setelah berhasil, memanggil `loadProducts()` untuk refresh data

**Read (Tampilkan Product):**
1. Membuat endpoint JSON di `show_json` view yang mengembalikan semua product
2. Menggunakan `fetch()` di JavaScript untuk mengambil data dari endpoint
3. Membuat fungsi `createProductCard()` untuk generate HTML card dari data JSON
4. Menampilkan product dalam grid layout yang di-generate secara dinamis

**Update & Delete:**
- Update dan Delete masih menggunakan link tradisional ke halaman edit/delete
- Bisa dikembangkan lebih lanjut dengan modal AJAX untuk konsistensi

#### Mengubah Login dan Register menggunakan AJAX.

Login dan Register pada implementasi ini masih menggunakan form submission tradisional (bukan AJAX), namun sudah dilengkapi dengan:
- Toast notification untuk feedback ke user
- Error handling dengan styling yang konsisten
- Validasi form dengan pesan error yang jelas

### Update tampilan

#### Membuat tombol yang akan menampilkan modal untuk create dan update product dalam bentuk form.

1. Membuat file `modal.html` dengan struktur modal menggunakan Tailwind CSS
2. Menambahkan tombol "Add New Product" yang memanggil fungsi `showModal()`
3. Modal berisi form dengan field: name, category, price, quantity, size, rating, thumbnail, description, dan is_featured
4. Implementasi fungsi `showModal()` dan `hideModal()` untuk toggle visibility modal
5. Form submission menggunakan AJAX dengan fungsi `addProductEntry()`

#### Membuat modal konfirmasi saat pengguna ingin menghapus product

Menggunakan `confirm()` JavaScript native pada link delete:
```javascript
onclick="return confirm('Are you sure you want to delete this product?')"
```

#### Saat melakukan aksi dari modal, product akan di-refresh tanpa perlu melakukan refresh halaman.

1. Setelah submit form berhasil, memanggil `document.dispatchEvent(new CustomEvent('productAdded'))`
2. Event listener `productAdded` akan trigger fungsi `loadProducts()`
3. Fungsi `loadProducts()` melakukan fetch ulang data dan re-render grid

#### Membuat tombol refresh yang akan menampilkan list product terbaru tanpa perlu refresh halaman

Tombol filter "All Products" dan "My Products" berfungsi sebagai refresh:
1. Menggunakan fungsi `setFilter(filter)` untuk mengubah filter aktif
2. Memanggil `loadProducts()` yang fetch data terbaru dari server
3. Filter dilakukan di client-side berdasarkan `user_id`

#### Membuat Loading, Empty, dan Error state melalui Javascript.

**Loading State:**
```html
<div id="loading" class="hidden">
  <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-green-500"></div>
  <p>Loading products...</p>
</div>
```

**Empty State:**
```html
<div id="empty" class="hidden">
  <img src="no-product.png" class="w-32 h-32 mx-auto">
  <h3>No Products Yet</h3>
  <button onclick="showModal()">Add First Product</button>
</div>
```

**Error State:**
```html
<div id="error" class="hidden">
  <div class="text-6xl">⚠️</div>
  <h3>Error Loading Products</h3>
  <button onclick="loadProducts()">Retry</button>
</div>
```

Fungsi `showSection(section)` mengatur visibility state yang sesuai.

#### Menampilkan Toast saat create, update, atau delete product dan saat login, logout, dan register (tidak boleh sama persis dengan tutorial).

1. Membuat komponen toast di `toast.html` dengan styling custom
2. Membuat fungsi `showToast(title, message, type)` di `toast.js`
3. Toast muncul di kanan bawah dengan animasi slide-up
4. Support 3 tipe: success (hijau), error (merah), normal (putih)
5. Auto-hide setelah 3 detik dengan animasi fade-out
6. Implementasi di berbagai event:
   - Login berhasil: "Welcome back, {username}!"
   - Register berhasil: "Your account has been successfully created!"
   - Logout: "You have been logged out successfully."
   - Add product: "Product added successfully!"

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

#### Apa perbedaan antara synchronous request dan asynchronous request?

**Synchronous Request:**
- Eksekusi kode berjalan secara berurutan (blocking)
- Browser menunggu response sebelum melanjutkan eksekusi kode berikutnya
- Halaman akan freeze/tidak responsif selama menunggu response
- User tidak bisa berinteraksi dengan halaman sampai request selesai
- Contoh: Form submission tradisional yang reload halaman

**Asynchronous Request:**
- Eksekusi kode tidak blocking, berjalan di background
- Browser dapat melanjutkan eksekusi kode lain sambil menunggu response
- Halaman tetap responsif dan user bisa berinteraksi
- Menggunakan callback, promise, atau async/await untuk handle response
- Contoh: AJAX request dengan fetch() API

#### Bagaimana AJAX bekerja di Django (alur request–response)?

1. **Client-side (JavaScript):**
   - User trigger event (klik tombol, submit form)
   - JavaScript membuat AJAX request menggunakan `fetch()` atau `XMLHttpRequest`
   - Request dikirim ke URL endpoint Django dengan method (GET/POST) dan data

2. **Server-side (Django):**
   - URL routing mengarahkan request ke view yang sesuai
   - View memproses request (validasi, query database, business logic)
   - View mengembalikan response dalam format JSON/XML/HTML
   - Menggunakan `JsonResponse()` atau `HttpResponse()` dengan content_type

3. **Client-side (JavaScript):**
   - Menerima response dari server
   - Parse data JSON jika diperlukan
   - Update DOM secara dinamis tanpa reload halaman
   - Tampilkan feedback ke user (toast, update UI)

**Contoh alur:**
```
User klik "Add Product" → showModal() → User isi form → Submit
→ fetch('/create-product-ajax/', {method: 'POST', body: formData})
→ Django view add_product_entry_ajax() → Validasi & save ke database
→ Return HttpResponse(status=201)
→ JavaScript terima response → hideModal() → loadProducts()
→ fetch('/json/') → Django return JsonResponse(products)
→ JavaScript render product cards → Update DOM
```

#### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

1. **User Experience Lebih Baik:**
   - Tidak ada page reload yang mengganggu
   - Interaksi lebih smooth dan responsif
   - Loading state bisa ditampilkan untuk feedback

2. **Performance Lebih Efisien:**
   - Hanya data yang diperlukan yang di-transfer (JSON)
   - Tidak perlu reload seluruh HTML, CSS, JS
   - Bandwidth lebih hemat

3. **Interaktivitas Tinggi:**
   - Real-time update tanpa refresh
   - Multiple request bisa berjalan bersamaan
   - Partial page update (hanya section tertentu)

4. **Separation of Concerns:**
   - Backend fokus pada data (API)
   - Frontend fokus pada presentation
   - Lebih mudah untuk develop mobile app atau SPA

5. **Reduced Server Load:**
   - Server hanya kirim data, tidak render template
   - Rendering dilakukan di client-side

#### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

1. **CSRF Protection:**
   ```python
   # Untuk AJAX POST request
   @csrf_exempt  # Hanya jika benar-benar diperlukan
   ```

2. **Authentication & Authorization:**
   ```python
   @login_required
   def view(request):
       if request.user != product.user:
           return HttpResponseForbidden()
   ```

3. **Input Validation:**
   - Validasi di server-side, jangan hanya di client
   - Gunakan Django Forms untuk validasi
   - Sanitize input untuk prevent XSS

4. **HTTPS:**
   - Gunakan HTTPS untuk encrypt data transmission
   - Credential tidak terkirim dalam plain text

5. **Rate Limiting:**
   - Batasi jumlah request per IP/user
   - Prevent brute force attack

6. **Secure Session Management:**
   - Set secure cookie flags (HttpOnly, Secure, SameSite)
   - Session timeout yang reasonable

7. **Content-Type Validation:**
   ```python
   if request.content_type != 'application/json':
       return HttpResponseBadRequest()
   ```

8. **Error Handling:**
   - Jangan expose sensitive info di error message
   - Log error untuk monitoring

#### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

**Dampak Positif:**

1. **Responsiveness:**
   - Halaman tidak freeze saat loading data
   - User bisa scroll atau interact dengan elemen lain
   - Terasa seperti native app

2. **Speed Perception:**
   - Partial update lebih cepat dari full page reload
   - Loading indicator memberi feedback progress
   - Instant feedback untuk user action

3. **Seamless Experience:**
   - Tidak ada "flash" dari page reload
   - State preservation (scroll position, form data)
   - Smooth transitions dan animations

4. **Reduced Bandwidth:**
   - Penting untuk user dengan koneksi lambat
   - Hanya transfer data yang diperlukan
   - Mobile-friendly

5. **Better Feedback:**
   - Toast notification untuk success/error
   - Loading state yang informatif
   - Error handling yang graceful

**Dampak Negatif (jika tidak diimplementasi dengan baik):**

1. **Complexity:**
   - Debugging lebih sulit
   - Browser back button bisa tidak berfungsi
   - SEO challenges untuk content yang di-load via AJAX

2. **Accessibility:**
   - Screen reader mungkin tidak detect dynamic content
   - Perlu ARIA labels dan proper focus management

3. **Error Handling:**
   - Network error bisa membuat app tidak berfungsi
   - Perlu fallback mechanism

**Best Practices:**
- Gunakan AJAX untuk enhance, bukan replace traditional navigation
- Provide loading indicators
- Handle errors gracefully
- Test dengan koneksi lambat
- Ensure accessibility

### Melakukan add-commit-push ke GitHub.
Selesai.
