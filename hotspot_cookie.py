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
    return bytes_value / 1024

def hCookie():
    api = None
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )

        # Retrieve active hotspot users
        print("Retrieving Cookie users...")
        hactive = list(api('/ip/hotspot/cookie/print'))

        # Display active hotspot users
        result = []

        result.append("===== Cookie Pengguna =====")
        if not hactive:
            result.append("Tidak ada data cookie pengguna.")
        else:
            for user in hactive:
                result.append(f"ID: {user.get('.id', 'N/A')}")
                result.append(f"User: {user.get('user', 'N/A')}")
                result.append(f"MAC Address: {user.get('mac-address', 'N/A')}")
                result.append(f"MAC Cookie: {user.get('mac-cookie', 'N/A')}")
                result.append(f"Expires In: {user.get('expires-in', 'N/A')}")

                result.append("")

        return "\n".join(result)

    except Exception as e:
        return f"Terjadi kesalahan: {e}"
    finally:
        # Close the connection if it's open
        if api:
            try:
                api.close()
            except Exception as close_error:
                print(f"Terjadi kesalahan saat menutup koneksi: {close_error}")

# Example usage
if __name__ == "__main__":
    output = hCookie()
    print(output)
