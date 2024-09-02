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

def host():
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
        print("Retrieving active hotspot host...")
        hactive = list(api('/ip/hotspot/host/print'))

        # Display active hotspot users
        result = []

        result.append("===== Host Hotspot =====")
        if not hactive:
            result.append("Tidak ada data tersedia.")
        else:
            for user in hactive:
                result.append(f"ID: {user.get('.id', 'N/A')}")
                result.append(f"MAC Address: {user.get('mac-address', 'N/A')}")
                result.append(f"Address: {user.get('address', 'N/A')}")
                result.append(f"To Address: {user.get('to-address', 'N/A')}")
                result.append(f"Server: {user.get('server', 'N/A')}")
                result.append(f"Uptime: {user.get('uptime', 'N/A')}")
                result.append(f"Idle Time: {user.get('idle-time', 'N/A')}")
                result.append(f"Keepalive Timeout: {user.get('keepalive-timeout', 'N/A')}")
                result.append(f"Host Dead Time: {user.get('host-dead-time', 'N/A')}")
                
                # Convert bytes to kilobytes
                bytes_in = user.get('bytes-in', '0')
                bytes_out = user.get('bytes-out', '0')
                packets_in = user.get('packets-in', '0')
                packets_out = user.get('packets-out', '0')
                try:
                    bytes_in_kb = bytes_to_kilobytes(int(bytes_in))
                    bytes_out_kb = bytes_to_kilobytes(int(bytes_out))
                    packets_in_kb = bytes_to_kilobytes(int(packets_in))
                    packets_out_kb = bytes_to_kilobytes(int(packets_out))

                    result.append(f"Bytes In: {bytes_in_kb:.2f} MB")
                    result.append(f"Bytes Out: {bytes_out_kb:.2f} MB")
                    result.append(f"Bytes In: {packets_in_kb:.2f} MB")
                    result.append(f"Bytes Out: {packets_out_kb:.2f} MB")

                except ValueError:
                    result.append(f"Bytes In: {bytes_in}")
                    result.append(f"Bytes Out: {bytes_out}")
                    result.append(f"Bytes In: {packets_in}")
                    result.append(f"Bytes Out: {packets_out}")

                result.append(f"Found By: {user.get('found-by', 'N/A')}")
                result.append(f"Authorized: {user.get('authorized', 'N/A')}")
                result.append(f"Bypassed: {user.get('bypassed', 'N/A')}")

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
    output = host()
    print(output)
