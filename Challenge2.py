import re

# Regular expression patterns for IP and MAC address formats
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
mac_pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

# Function to check if the IP address is valid
def is_valid_ip(ip_address):
    if re.match(ip_pattern, ip_address):
        parts = ip_address.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False

# Function to check if the MAC address is valid
def is_valid_mac(mac_address):
    return re.match(mac_pattern, mac_address) is not None

# Sample IP and MAC addresses (incorrect formats)
ip_address = "999.168.0.300"  # Incorrect: IP parts exceed the valid range
mac_address = "00:1G:2B:3C:4D:5Z"  # Incorrect: Contains invalid characters (G, Z)

# Run the tests
if is_valid_ip(ip_address):
    print(f"The IP address {ip_address} is in the correct format.")
else:
    print(f"The IP address {ip_address} is NOT in the correct format.")

if is_valid_mac(mac_address):
    print(f"The MAC address {mac_address} is in the correct format.")
else:
    print(f"The MAC address {mac_address} is NOT in the correct format.")
