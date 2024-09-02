from librouteros import connect
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MikroTik credentials
MIKROTIK_HOST = os.getenv('M_HOST')
MIKROTIK_PORT = int(os.getenv('M_PORT', 8728))  # Default port 8728
MIKROTIK_USER = os.getenv('M_USER')
MIKROTIK_PASSWORD = os.getenv('M_PASS')

def ttl():
    api = None
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )

        # Mengambil data dari endpoint /ip/hotspot/user/print
        users = api('/ip/hotspot/user/print')
        active_users = api('/ip/hotspot/active/print')
        
        # Menghitung jumlah pengguna
        user_count = 0
        active_count = 0

        # Mengumpulkan data dan menghitung jumlah pengguna
        for _ in users:
            user_count += 1

        for _ in active_users:
            active_count += 1

        # Format data sebagai string
        result = (
            "===== Pengguna Hotspot =====\n\n"
            f"Jumlah pengguna yang tersedia: {user_count}\n"
            f"Jumlah pengguna aktif: {active_count}\n"
        )
        return result

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

    finally:
        # Menutup koneksi jika ada
        if api:
            try:
                api.close()
            except Exception as close_error:
                print(f"Terjadi kesalahan saat menutup koneksi: {close_error}")

