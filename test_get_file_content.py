from functions.get_file_content import get_file_content


def main() -> None:
    # Test lorem.txt truncation
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    # Test reading valid smaller files
    print("\nReading 'main.py':")
    print(get_file_content("calculator", "main.py"))

    print("\nReading 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Test error cases
    print("\nReading '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nReading 'pkg/does_not_exist.py':")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
