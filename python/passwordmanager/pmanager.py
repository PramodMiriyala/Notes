
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
        )

        store_password(
            service_name=args.service,
            user_name=args.username,
            password=password
        )
        print("Password was successfully generated and stored."
              "Use the retrieve command to fetch it.")     
    elif args.command == "retrieve":
        (decrypted_username, decrypted_password) = retrieve_password(
            service_name=args.service
        )
        print(f"Username: {decrypted_username}")
        print(f"Password: {decrypted_password}")
    else:
        print(f"No password found for service: {args.service}")
if __name__ == "__main__":
    main()
