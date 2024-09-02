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

def profil_ppp():
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )
        
        # Retrieve PPP profiles
        ppp_profiles = list(api('/ppp/profile/print'))  # Convert generator to list
        api.close()
        
        if ppp_profiles:
            # Format the PPP profile information
            result = ["===== PPP Profiles ====="]
            for profile in ppp_profiles:
                result.append(
                    f"Profile Name: {profile.get('.id', 'N/A')}\n"
                    f"- Local Address: {profile.get('name', 'N/A')}\n"
                    f"- DNS Servers: {profile.get('local-address', 'N/A')}\n"
                    f"- Remote Address: {profile.get('remote-address', 'N/A')}\n"
                    f"- Bridge Learning: {profile.get('bridge-learning', 'N/A')}\n"
                    f"- Use MPLS: {profile.get('use-mpls', 'N/A')}\n"
                    f"- Use Compression: {profile.get('use-compression', 'N/A')}\n"
                    f"- Use Encryption: {profile.get('use-encryption', 'N/A')}\n"
                    f"- Only One: {profile.get('only-one', 'N/A')}\n"
                    f"- Change TCP MSS: {profile.get('change-tcp-mss', 'N/A')}\n"
                    f"- Use UPNP: {profile.get('use-upnp', 'N/A')}\n"
                    f"- Address List: {profile.get('address-list', 'N/A')}\n"
                    f"- On Up: {profile.get('on-up', 'N/A')}\n"
                    f"- On Down: {profile.get('on-down', 'N/A')}\n"
                    f"- Default: {profile.get('default', 'N/A')}\n"
                    f"==========\n"
                )
            return "\n".join(result)
        else:
            return "No PPP profiles available."
    except Exception as e:
        return f"Error retrieving PPP profiles: {e}"

# Example usage
if __name__ == "__main__":
    print(profil_ppp())