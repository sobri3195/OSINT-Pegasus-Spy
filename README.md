# OSINT-Pegasus Spy

**OSINT-Pegasus Spy** adalah alat investigasi berbasis OSINT (Open-Source Intelligence) yang dirancang untuk melakukan pengumpulan informasi dari berbagai sumber terbuka. Alat ini mendukung berbagai fungsi seperti analisis Bitcoin, pengujian keamanan server, analisis malware, hingga pengumpulan informasi domain dan email.

## Fitur
- **Bitcoin Analysis**: Mendapatkan informasi terbaru tentang block Bitcoin, berdasarkan tanggal, atau alamat dompet tertentu.
- **SSL Cipher Scanning**: Menampilkan cipher SSL yang didukung oleh server/domain tertentu.
- **Heart Bleed Check**: Memeriksa apakah server rentan terhadap serangan Heart Bleed.
- **Domain Reconnaissance**: Melakukan pengumpulan informasi detail tentang domain tertentu.
- **Email Reconnaissance**: Menemukan informasi terkait alamat email.
- **IoT Device Exploration**: Menganalisis perangkat Internet of Things (IoT).
- **IP WHOIS Lookup**: Mendapatkan informasi WHOIS tentang alamat IP.
- **Malware Analysis**: Mengirim file ke VirusTotal untuk analisis malware.
- **JSON Output**: Mendukung format output JSON untuk integrasi lebih lanjut.

## Cara Penggunaan
1. Jalankan program:
   ```bash
   python osint_pegasus_spy.py

2. Pilih opsi dari menu yang tersedia dengan memasukkan angka (1-11), misalnya:
1 untuk mendapatkan informasi block Bitcoin terbaru.
2 untuk mendapatkan informasi block Bitcoin berdasarkan tanggal (format: YYYYMMDD).
3 untuk informasi alamat dompet Bitcoin tertentu.
4 untuk memeriksa SSL cipher pada domain tertentu.
5 untuk memeriksa server apakah rentan terhadap Heart Bleed.
6 untuk melakukan domain reconnaissance.
7 untuk melakukan email reconnaissance.
8 untuk mengeksplorasi perangkat IoT (Internet of Things).
9 untuk melakukan WHOIS lookup pada alamat IP.
10 untuk mengirim file ke VirusTotal untuk analisis malware.
11 untuk keluar dari program.
   
Masukkan informasi tambahan sesuai kebutuhan (contoh: tanggal, domain, atau file path).
Ikuti instruksi lanjutan untuk menampilkan hasil dalam format teks atau JSON.

## Struktur Menu
1. Get latest bitcoin block info
2. Get bitcoin block info by date (e.g., 20190614)
3. Get info of any bitcoin wallet address
4. List out supported SSL ciphers used by any domain
5. Check whether server is vulnerable to heart bleed
6. Perform domain recon
7. Perform email recon
8. Explore the Internet of Things (IoT)
9. WHOIS IP Lookup
10. Send files to VirusTotal for malware analysis
11. Exit
## Catatan Penting
Alat ini dirancang untuk keperluan edukasi dan investigasi legal.
Penggunaan alat ini di luar kerangka hukum tidak dianjurkan dan menjadi tanggung jawab pengguna.

## Penulis
Muhammad Sobri Maulana
