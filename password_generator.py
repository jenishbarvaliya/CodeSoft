import random
import string

def generate_password(length):
    if length < 2:
        raise ValueError("Password length should be at least 2.")
    
    capital_letter = random.choice(string.ascii_uppercase)
    special_character = random.choice('@#$')
    remaining_characters = string.ascii_letters + string.digits + '@#$'

    other_characters = ''.join(random.choice(remaining_characters) for i in range(length - 2))

    password = capital_letter + special_character + other_characters

    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 2:
            print("Password length should be at least 2.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
