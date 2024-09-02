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

def bytes_to_megabytes(bytes_value):
    """Convert bytes to megabytes."""
    return bytes_value / (1024 * 1024)

def profil():
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )
        
        # Retrieve system information
        print ("Mengambil data sistem...")
        system_info = list(api('/system/resource/print'))  # Convert generator to list
        api.close()
        
        if system_info:
            # Format the system information
            system = system_info[0]  # Assuming single result
            info_message = (
                f"OPALNET\n"
                f"Lancar dan cepat\n\n"
                f"===== Mikrotik Information =====\n\n"
                f"Uptime: {system['uptime']}\n\n"
                f"CPU\n"
                f"- CPU Frequency: {system['cpu-frequency']} MHz\n"
                f"- CPU Load: {system['cpu-load']} %\n\n"
                f"Storage and RAM\n"
                f"- Storage: {bytes_to_megabytes(int(system['total-hdd-space'])):.2f} MB\n"
                f"- Free Storage: {bytes_to_megabytes(int(system['free-hdd-space'])):.2f} MB\n"
                f"- RAM: {bytes_to_megabytes(int(system['total-memory'])):.2f} MB\n"
                f"- Free RAM: {bytes_to_megabytes(int(system['free-memory'])):.2f} MB\n\n"
                f"System Info\n"
                f"- Model: {system['board-name']}\n"
                f"- Version: {system['version']}\n"
                f"- Build: {system['build-time']}\n"
            )
            return info_message
        else:
            return "No system information available."
    except Exception as e:
        return f"Error retrieving system information: {e}"

# Example usage
if __name__ == "__main__":
    print(profil())
