import argparse
import os

def remove_comments_and_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]

    with open(file_path, 'w') as file:
        file.writelines('\n'.join(filtered_lines))

def main():
    parser = argparse.ArgumentParser(description='Remove comments and empty lines from a .gitignore file.')
    parser.add_argument('file_path', help='Path to the .gitignore file')
    args = parser.parse_args()

    remove_comments_and_empty_lines(args.file_path)
    print(f"Comments and empty lines removed from {args.file_path}")

if __name__ == '__main__':
    main()
