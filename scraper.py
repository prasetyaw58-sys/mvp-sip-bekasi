import hashlib
import os
import requests
from bs4 import BeautifulSoup

def run_scraper():
    # Target awal: JDIH Jabar (bisa diganti atau ditambah nanti)
    target_url = "https://jdih.jabarprov.go.id/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    print(f"Memeriksa pembaruan dari: {target_url}")
    
    try:
        response = requests.get(target_url, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"Gagal mengakses situs. Status: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Contoh elemen produk hukum (nanti kita sesuaikan dengan struktur aslinya)
        print("Koneksi berhasil! Siap mengekstrak data regulasi.")

    except Exception as e:
        print(f"Terjadi kesalahan saat scraping: {e}")

if __name__ == "__main__":
    run_scraper()
