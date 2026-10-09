from functions.run_python_file import run_python_file


def main() -> None:
    print("Test 1: main.py usage instructions")
    print(run_python_file("calculator", "main.py"))

    print("\nTest 2: main.py with expression")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nTest 3: tests.py")
    print(run_python_file("calculator", "tests.py"))

    print("\nTest 4: ../main.py (outside dir)")
    print(run_python_file("calculator", "../main.py"))

    print("\nTest 5: nonexistent.py")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nTest 6: lorem.txt (non-Python file)")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
