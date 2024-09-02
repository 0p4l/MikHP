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

def hProfile():
    api = None
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )

        # Retrieve hotspot profiles
        print("Retrieving hotspot profiles...")
        uprof = list(api('/ip/hotspot/user/profile/print'))
        sprof = list(api('/ip/hotspot/profile/print'))

        # Display hotspot server profiles
        result = []

        result.append("===== Hotspot Server Profiles =====")
        for sprofile in sprof:
            result.append(f"Profile Name: {sprofile.get('name', 'N/A')}")
            result.append(f"- DNS Names: {sprofile.get('dns-names', 'N/A')}")
            result.append(f"- HTML Directory: {sprofile.get('html-directory', 'N/A')}")
            result.append(f"- Rate Limit: {sprofile.get('rate-limit', 'N/A')}")
            result.append(f"- Login By: {sprofile.get('login-by', 'N/A')}")
            result.append(f"- Cookie Lifetime: {sprofile.get('http-cookie-lifetime', 'N/A')}")
            result.append(f"- Split Domain: {sprofile.get('split-user-domain', 'N/A')}")
            result.append(f"- Radius: {sprofile.get('use-radius', 'N/A')}")
            result.append(f"- Default Address: {sprofile.get('hotspot-address', 'N/A')}")
            result.append("")

        result.append("===== Hotspot User Profiles =====")
        for profile in uprof:
            result.append(f"Profile ID: {profile.get('.id', 'N/A')}")
            result.append(f"Name: {profile.get('name', 'N/A')}")
            result.append(f"Address Pool: {profile.get('address-pool', 'N/A')}")
            result.append(f"Idle Timeout: {profile.get('idle-timeout', 'N/A')}")
            result.append(f"Keepalive Timeout: {profile.get('keepalive-timeout', 'N/A')}")
            result.append(f"Status Autorefresh: {profile.get('status-autorefresh', 'N/A')}")
            result.append(f"Shared Users: {profile.get('shared-users', 'N/A')}")
            result.append(f"MAC Cookie Timeout: {profile.get('mac-cookie-timeout', 'N/A')}")
            result.append(f"Rate Limit: {profile.get('rate-limit', 'N/A')}")
            result.append(f"Parent Queue: {profile.get('parent-queue', 'N/A')}")
            result.append(f"Address List: {profile.get('address-list', 'N/A')}")
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
