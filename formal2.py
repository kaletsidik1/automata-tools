import itertools

def generate_strings(n):
    alphabet = "abc0"   

    for tail_strings in itertools.product(alphabet, repeat=n-1):
        s = 'a' + ''.join(tail_strings)
        if "b0" in s:
            yield s


MAX_LENGTH = 10  

while True:
    print("\n===== STRING GENERATOR MENU =====")
    print("1. Generate Strings")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        while True:
            length_input = input(f"\nEnter string length (3 to {MAX_LENGTH}): ").strip()

            if not length_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            n = int(length_input)
            if n < 3:
                print(" Length must be at least 3 to contain 'b0'. Try again.")
                continue
            if n > MAX_LENGTH:
                print(f" Length too large. Maximum allowed is {MAX_LENGTH}. Try again.")
                continue

            
            print(f"\nGenerating strings of length {n} using alphabet {{a,b,c,0}} starting with 'a' and containing 'b0':\n")

            found = False
            for s in generate_strings(n):
                print(s)
                found = True

            if not found:
                print("No valid strings found.")

            break  

    elif choice == "2":
        print("Exiting program... ")
        break

    else:
        print(" Invalid choice. Please enter 1 or 2.")
