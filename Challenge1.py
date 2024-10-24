# Define the expected values
expected_location = "TIP_Manila"
expected_ip_address = "192.168.45.100"
expected_subnet_mask = "255.255.0.0"

# Sample data for R1
R1 = {
    "location": "TIP_Manila",
    "ip_address": "192.168.45.25",
    "subnet_mask": "255.255.255.0"
}

# Test to check if R1's values match the expected ones
def test_r1_configuration(router):
    if router["location"] == expected_location and \
       router["ip_address"] == expected_ip_address and \
       router["subnet_mask"] == expected_subnet_mask:
        return "Test Passed: R1 configuration is correct."
    else:
        return "Test Failed: R1 configuration is incorrect."

# Run the test
result = test_r1_configuration(R1)
print(result)
