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

def user_ppp():
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )
        
        # Retrieve PPP profiles
        ppp_profiles = list(api('/ppp/secret/print'))  # Convert generator to list
        api.close()
        
        if ppp_profiles:
            # Format the PPP profile information
            result = ["===== PPP User ====="]
            for profile in ppp_profiles:
                result.append(
                    f"- ID: {profile.get('.id', 'N/A')}\n"
                    f"- Name: {profile.get('name', 'N/A')}\n"
                    f"- Service: {profile.get('service', 'N/A')}\n"
                    f"- Caller ID: {profile.get('caller-id', 'N/A')}\n"
                    f"- Password: {profile.get('password', 'N/A')}\n"
                    f"- Profile: {profile.get('profile', 'N/A')}\n"
                    f"- Local Address: {profile.get('local-address', 'N/A')}\n"
                    f"- Remote Address: {profile.get('remote-address', 'N/A')}\n"
                    f"- Routes: {profile.get('routes', 'N/A')}\n"
                    f"- IPV6 Routes: {profile.get('ipv6-routes', 'N/A')}\n"
                    f"- Limit Bytes In: {profile.get('limit-bytes-in', 'N/A')}\n"
                    f"- Limit Bytes Out: {profile.get('limit-bytes-out', 'N/A')}\n"
                    f"- Last Log-out: {profile.get('last-logged-out', 'N/A')}\n"
                    f"- Last DC Reason: {profile.get('last-disconnect-reason', 'N/A')}\n"
                    f"- Disable: {profile.get('disable', 'N/A')}\n"
                    f"==========\n"
                )
            return "\n".join(result)
        else:
            return "No PPP profiles available."
    except Exception as e:
        return f"Error retrieving PPP profiles: {e}"

# Example usage
if __name__ == "__main__":
    print(user_ppp())