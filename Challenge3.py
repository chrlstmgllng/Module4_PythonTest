def check_device_type(device_name):
    # Define known device types
    routers = ["router", "r1", "r2", "r3"]
    pcs = ["pc", "laptop", "desktop", "personal computer"]
    switches = ["switch", "s1", "s2", "s3"]
    servers = ["server", "web server", "database server"]

    # Convert the input to lowercase for case-insensitive comparison
    device_name = device_name.lower()

    # Check what type of device it is
    if device_name in routers:
        return "The device is a Router."
    else:
        # If it's not a router, check if it's a PC, Switch, or Server
        if device_name in pcs:
            return "The device is not a router, it is a Personal Computer."
        elif device_name in switches:
            return "The device is not a router, it is a Switch."
        elif device_name in servers:
            return "The device is not a router, it is a Server."
        else:
            return "The device is not a router and its type is unknown."

# Sample test cases (You can change these or get user input)
device_name = input("Enter the device name: ")  # Or manually set device_name

# Run the test
result = check_device_type(device_name)
print(result)
