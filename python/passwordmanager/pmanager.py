
"""generates and retrieves passwords"""
from argparse import ArgumentParser
from password import generate_password
from store import store_password, retrieve_password

def argument_parser():
    """__summary__"""
    global_parser = ArgumentParser(prog = "pmanager")
    subparsers = global_parser.add_subparsers(dest = "command")

    generate_parser = subparsers.add_parser("generate", help = "generate passwords")
    generate_parser.add_argument(
        "-l", "--length",
        type = int,
        default = 12,
        help = "length of the password to be generated, default = 12"
    )
    generate_parser.add_argument(
        "-d", "--include-digits",
        action = "store_true",
        help = "weather include digits in the password."
    )
    generate_parser.add_argument(
        "-c", "--include-special_characters",
        action = "store_true",
        help = "weather ot include special characters in the password."
    )
    generate_parser.add_argument(
        "-U", "--min-upper",
        type = int,
        default = 1,
        help = "minimum number of uppercase letters."
    )
    generate_parser.add_argument(
        "-L", "--min-lower",
        type = int,
        default = 1,
        help = "minimum number of lowercase letters."
    )
    generate_parser.add_argument(
        "-D", "--min-digit",
        type = int,
        default = 1,
        help = "minimum number of digits letters."
    )
    generate_parser.add_argument(
        "-C", "--min-special-chars",
        type = int,
        default = 1,
        help = "minimum number of special characters letters."
    )
    generate_parser.add_argument(
        "-s", "--service",
        type = str,
        help = "service for which password generated"
    )
    generate_parser.add_argument(
        "-u", "--username",
        type = str,
        help = "username used for the service"
    )


    retrieve_parser = subparsers.add_parser("retrieve", help = "retrieve's password")
    retrieve_parser.add_argument(
        "-s", "--service",
        type = str,
        help = "service for which password generated"
    )
    return global_parser.parse_args()

def main():
    """This function will parse arguments and execute commands"""
    args = argument_parser()

    if args.command == "generate":
        password = generate_password(
            length=args.length,
            include_digits=args.include_digits,
            include_special_characters= args.include_special_characters,
            min_upper=args.min_upper,
            min_lower=args.min_lower,
            min_digit=args.min_digit,
            min_special_characters=args.min_special_chars
        )

        store_password(
            service_name=args.service,
            user_name=args.username,
            password=password
        )
        print("Password was successfully generated and stored."
              "Use the retrieve command to fetch it.")     
    elif args.command == "retrieve":
        (username, password) = retrieve_password(
            service_name=args.service
        )
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print(f"No password found for service: {args.service}")
if __name__ == "__main__":
    main()
