# === GROUP MEMBERS ===
# Biruk Demissie       UGR/1666/15
# Bisrat Alemayehu     UGR/0633/15
# Kaletsidik Ayalew    UGR/9300/15
# Khalid Abdifetah     UGR/9210/15

import itertools
transition = {
    'S': {'a': 'A', 'b': 'B'},
    'A': {'a': 'A', 'b': 'C'},
    'B': {'a': 'C', 'b': 'B'},
    'C': {'b': 'D'},          
    'D': {'a': 'D'}           
}

start_state = 'S'
accept_states = {'C', 'D'}
alphabet = ['a', 'b']
MAX_LENGTH = 10



def validate_string(s, verbose=True):
    state = start_state
    if verbose:
        print(f"Start at state: {state}")
    for i, char in enumerate(s, start=1):
        if char not in alphabet:
            return False, f"Invalid symbol '{char}'"
        if char not in transition[state]:
            return False, f"No transition from state {state} on '{char}'"
        next_state = transition[state][char]
        if verbose:
            print(f" step {i}: {state} --{char}--> {next_state}")
        state = next_state
    accepted = (state in accept_states)
    return accepted, state


def generate_all_valid_strings(length):
    if length > MAX_LENGTH:
        return f"Length too long (max {MAX_LENGTH})."
    all_combinations = itertools.product(alphabet, repeat=length)
    valid_strings = []
    for combo in all_combinations:
        s = ''.join(combo)
        valid, _ = validate_string(s, verbose=False)
        if valid:
            valid_strings.append(s)
    return valid_strings


def generate_strings(n):
    alphabet2 = "abc0"
    for tail in itertools.product(alphabet2, repeat=n-1):
        s = 'a' + ''.join(tail)
        if "b0" in s:
            yield s

def menu():
    while True:
        print("\n==== Menu ====")
        print("1. Generate all valid strings")
        print("2. Validate a string")
        print("3. Generate the set of strings that starts with 'a' and containing 'b0' on {a,b,c,0}")
        print("4. Exit")
        choice = input("Select (1-4): ").strip()
        if choice == "1":
            try:
                length = int(input("Length (max 10): "))
            except ValueError:
                print("Invalid length. Must be an integer.")
                continue
            strings = generate_all_valid_strings(length)
            if isinstance(strings, str):
                print(strings)
                continue
            print(f"All valid strings of length {length}:")
            for s in strings:
                print(s)
            print(f"Total valid strings: {len(strings)}")
        elif choice == "2":
            s = input("Enter string: ").strip()
            valid, msg = validate_string(s, verbose=True)
            if valid:
                print(f"\nRESULT: VALID (final state = {msg})")
            else:
                print(f"\nRESULT: INVALID ({msg})")
        elif choice == "3":
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
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice!")


if __name__ == '__main__':
    menu()
