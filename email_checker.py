def main():
    email = "fattiger.2022@yahoo.com"
    if valid_email(email):
        print("Valid email")
    else:
        print("Invalid email format")


def valid_email(email):
    """Check email format has @ and . in this order"""
    return email.find("@") < email.rfind(".")


if __name__ == '__main__':
    main()
