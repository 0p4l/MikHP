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

def active_ppp():
    try:
        # Connect to MikroTik
        api = connect(
            host=MIKROTIK_HOST,
            port=MIKROTIK_PORT,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASSWORD
        )
        
        # Retrieve PPP secrets (active PPP sessions)
        ppp_active = list(api('/ppp/active/print'))  # Convert generator to list
        api.close()
        
        if ppp_active:
            # Format the PPP active information
            result = ["===== PPP Active ====="]
            for session in ppp_active:
                result.append(
                    f"ID: {session.get('.id', 'N/A')}\n"
                    f"Name: {session.get('name', 'N/A')}\n"
                    f"Service: {session.get('service', 'N/A')}\n"
                    f"Caller ID: {session.get('caller-id', 'N/A')}\n"
                    f"Address: {session.get('address', 'N/A')}\n"
                    f"Uptime: {session.get('uptime', 'N/A')}\n"
                    f"Encoding: {session.get('encoding', 'N/A')}\n"
                    f"Session ID: {session.get('session-id', 'N/A')}\n"
                    f"Limit Bytes In: {session.get('limit-bytes-in', '0')}\n"
                    f"Limit Bytes Out: {session.get('limit-bytes-out', '0')}\n"
                    f"Radius: {session.get('radius', 'False')}\n"
                    f"==========\n"
                )
            return "\n".join(result)
        else:
            return "No PPP active sessions available."
    except Exception as e:
        return f"Error retrieving PPP active sessions: {e}"

# Example usage
if __name__ == "__main__":
    print(active_ppp())
