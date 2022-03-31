

def main():
    email = "fattiger@2022yahoo.com"
    if "@" in email and "." in email:
        print("Valid email")
    else:
        print("Invalid email format")


if __name__ == '__main__':
    main()