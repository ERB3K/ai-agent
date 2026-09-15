from functions.run_python_file import run_python_file


def main():
    print("--- 1. main.py (Usage) ---")
    print(run_python_file("calculator", "main.py"))

    print("\n--- 2. main.py ['3 + 5'] ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\n--- 3. tests.py ---")
    print(run_python_file("calculator", "tests.py"))

    print("\n--- 4. ../main.py ---")
    print(run_python_file("calculator", "../main.py"))

    print("\n--- 5. nonexistent.py ---")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\n--- 6. lorem.txt ---")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()