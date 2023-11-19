import os 
import random
import string

def generate_password(min_lenght, numbers=True, special_carac= True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_carac:
        characters += special

    pwd=""
    meets_critere = False
    has_number = False
    has_special = False

    while not meets_critere or len(pwd) < min_lenght:

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:

            has_number = True

        elif new_char in special:

            has_special = True


        meets_critere = True
        if numbers:
            meets_critere = has_number
            if special_carac:
                meets_critere= meets_critere and has_special
    

    return pwd

min_lenght = int(input("Enter the minimum lenght : " + "\n"))
has_number = input("Do you want to have numbers in your password ? (y/n) : " + "\n").lower() == "y"
has_special = input("Do you want to have special charactere in your password ? (y/n) : " + "\n").lower() == "y"
pwd = generate_password(min_lenght, has_number, has_special)
print("The generated password is : ", pwd)

generate_password(10)

