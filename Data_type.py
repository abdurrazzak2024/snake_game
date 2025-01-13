
# Define the dictionary to represent an attack
"""
attack_details = {
    "attack_id": 101,
    "type": "Cyber Attack",
    "attacker": {
        "name": "Unknown",
        "ip_address": "192.168.1.10",
        "organization": "Hacker Group XYZ"
    },
    "target": {
        "system": "Web Server",
        "ip_address": "10.0.0.5"
    },
    "method": "SQL Injection",
    "status": "Ongoing",
    "timestamp": "2025-01-12T15:00:00",
    "defense": {
        "status": "Monitoring",
        "measures": [
            "Firewall Activated",
            "Traffic Blocked",
            "Alert Sent to Admin"
        ]
    },
    "impact": {
        "data_breach": True,
        "records_compromised": 5000,
        "financial_loss": "$10,000"
    }
}

# Example: Accessing information from the dictionary
print("Attack Type:", attack_details["type"])
print("Target System:", attack_details["target"]["system"])
print("Defense Status:", attack_details["defense"]["status"])
"""
"""
import itertools
import string

def brute_force_password(password, max_length=6):
    # Define the character set to use (e.g., lowercase letters, digits, etc.)
    char_set = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        # Generate all possible combinations of the given length
        for attempt in itertools.product(char_set, repeat=length):
            guess = ''.join(attempt)
            print(f"Trying: {guess}")  # Show current attempt
            if guess == password:
                return f"Password found: {guess}"
    return "Password not found within the given length constraints."

# Example usage
if __name__ == "__main__":
    target_password = "nur111163"  # The password to guess
    result = brute_force_password(target_password, max_length=100)
    print(result)
"""
#saltinh code for hacked
import bcrypt

def hash_password(password: str) -> str:
    """Hashes a password with a unique salt."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(password: str, hashed: str) -> bool:
    """Verifies a password against a hashed value."""
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Example usage
if __name__ == "__main__":
    # User's password
    password = "SecurePassword123!"

    # Hash the password
    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)

    # Verify the password
    is_valid = verify_password(password, hashed_password)
    print("Password valid:", is_valid)
