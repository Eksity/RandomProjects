#pip install validator-collection
import validator_collection
import sys

def main():
    try:
        validator_collection.validators.email(input("Email: "))
        print("Valid")
    except validator_collection.errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()