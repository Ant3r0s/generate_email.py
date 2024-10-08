import random
import string

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

if __name__ == "__main__":
    print("Generated Email:", generate_random_email())
