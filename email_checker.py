def main():
    email = "fattiger@2022yahoo.com"
    if valid_email(email):
        print("Valid email")
    else:
        print("Invalid email format")


def valid_email(email):
    """Check email format has @ and ."""
    return "@" in email and "." in email


if __name__ == '__main__':
    main()
