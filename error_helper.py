# error_helper.py
import error_codes

def get_solution(error_code):
    return error_codes.error_solutions.get(error_code, "Error code not found. Please check the code and try again.")

def main():
    print("Welcome to the Lab Error Helper!")
    while True:
        error_code = input("Please enter the error code (or type 'exit' to quit): ").strip().upper()
        if error_code == 'EXIT':
            print("Goodbye!")
            break
        solution = get_solution(error_code)
        print(f"Solution for {error_code}: {solution}")

if __name__ == "__main__":
    main()
