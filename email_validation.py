import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Take email input from user
email = input("Enter your email: ")

# Validate and print result
if is_valid_email(email):
    print("✅ Valid email address!")
else:
    print("❌ Invalid email address. Please try again.")
