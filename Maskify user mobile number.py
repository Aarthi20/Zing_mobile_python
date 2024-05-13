def maskify(mobile_number):
    if len(mobile_number) <= 3:
        return mobile_number
    else:
        masked = '#' * (len(mobile_number) - 3) + mobile_number[-3:]
        return masked

# Test the function
mobile_number = input("Enter your mobile number: ")
masked_number = maskify(mobile_number)
print(masked_number)  # Output: "#######655"
