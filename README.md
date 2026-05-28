# Website Landing Page & FAQ

Modul Odoo 19 untuk mengelola **Landing Page** dan **FAQ** melalui aplikasi Website.

## Instalasi

1. Pastikan container Odoo berjalan:

```bash
docker compose up -d
```

2. Buka Odoo: http://localhost:8069
3. Aktifkan **Developer Mode** (Settings → Activate Developer Mode)
4. Apps → Update Apps List
5. Cari **"Website Landing Page & FAQ"** → Install

> Modul ini membutuhkan modul **Website** (ter-install otomatis sebagai dependensi).

## Halaman Publik

| URL | Deskripsi |
|-----|-----------|
| `/` | Landing page dinamis (section dari backend) |
| `/landing` | Alias ke landing page |
| `/faq` | FAQ (accordion) |
| `/electricity/faqs` | Alias FAQ (menu Electricity) |
| Menu lainnya | Halaman placeholder via **Website → Pages** (data XML) |

Menu header didefinisikan di `data/website_menu.xml`. Halaman konten menu didefinisikan di `data/website_pages.xml` dan dapat diedit dari backend.

## Pengelolaan Konten (Backend)

Menu: **Website → Configuration → Landing & FAQ**

- **Landing Page** — kelola section (Hero, Fitur, Testimoni, CTA, Kustom)
- **FAQ** — kelola pertanyaan & jawaban
- **Kategori FAQ** — kelompokkan pertanyaan

Halaman menu (About, Solar Power, dll.) dapat disesuaikan di **Website → Site → Pages**.

### Tipe Section Landing

| Tipe | Kegunaan |
|------|----------|
| Hero | Banner utama + gambar + tombol CTA |
| Fitur | Grid fitur (konten HTML bebas) |
| Testimoni | Kutipan pelanggan |
| CTA | Call-to-action dengan tombol |
| Kustom | Section bebas |

Centang **Dipublikasikan** agar section/FAQ tampil di website.

## Upgrade Modul

Setelah mengubah kode modul:

```bash
docker compose restart odoo
```

Lalu di Odoo: Apps → modul → Upgrade.
