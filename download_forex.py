import requests
import os
from datetime import datetime

def download_forex_rates():
    url = "https://sbi.bank.in/documents/16012/1400784/FOREX_CARD_RATES.pdf"
    
    download_dir = "forex_rates"
    os.makedirs(download_dir, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{download_dir}/FOREX_CARD_RATES_{date_str}.pdf"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        file_size = len(response.content) / 1024
        print(f"Downloaded successfully: {filename}")
        print(f"File size: {file_size:.2f} KB")
        print(f"Date: {date_str}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")
        return False

if __name__ == "__main__":
    success = download_forex_rates()
    exit(0 if success else 1)
