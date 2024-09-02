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

def bytes_to_kilobytes(bytes_value):
    """Convert bytes to kilobytes."""
    return bytes_value / (1024 * 1024)

def hUser():
    api = None
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )
        
        # Retrieve hotspot user information
        hotspot_user = api('/ip/hotspot/user/print')

        result = []

        result.append("Voucher/Pengguna Tersedia :")
        result.append("")  # Add an empty line for spacing

        for user in hotspot_user:
            name = user.get('name', 'N/A')
            server = user.get('server', 'N/A')  # Pastikan key ini sesuai dengan data Anda
            profile = user.get('profile', 'N/A')  # Pastikan key ini sesuai dengan data Anda
            uptime = user.get('uptime', 'N/A')  # Pastikan key ini sesuai dengan data Anda
            mac_address = user.get('mac-address', 'N/A')  # Mengambil alamat MAC

            # Convert bytes to kilobytes
            bytes_in = user.get('bytes-in', '0')
            bytes_out = user.get('bytes-out', '0')
            try:
                bytes_in_kb = bytes_to_kilobytes(int(bytes_in))
                bytes_out_kb = bytes_to_kilobytes(int(bytes_out))

                result.append(
                    f"Name: {name}\n"
                    f"MAC Address: {mac_address}\n"
                    f"Server: {server}\n"
                    f"Profile: {profile}\n"
                    f"Uptime: {uptime}\n"
                    f"Bytes In: {bytes_in_kb:.2f} MB\n"
                    f"Bytes Out: {bytes_out_kb:.2f} MB\n"
                    "==========\n"
                )

            except ValueError:
                result.append(
                    f"Name: {name}\n"
                    f"MAC Address: {mac_address}\n"
                    f"Server: {server}\n"
                    f"Profile: {profile}\n"
                    f"Uptime: {uptime}\n"
                    f"Bytes In: {bytes_in} (cannot convert to KB)\n"
                    f"Bytes Out: {bytes_out} (cannot convert to KB)\n"
                    "==========\n"
                )

        return "\n".join(result)

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

    finally:
        # Menutup koneksi jika ada
        if api:
            try:
                api.close()
            except Exception as close_error:
                print(f"Terjadi kesalahan saat menutup koneksi: {close_error}")

# Contoh penggunaan
if __name__ == "__main__":
    print(hUser())
