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
MAX_LEN = 10

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
    if length > MAX_LEN:
        return "Length too long (max 10)."
    all_combinations = itertools.product(alphabet, repeat=length)
    valid_strings = []
    for combo in all_combinations:
        s = ''.join(combo)
        valid, _ = validate_string(s, verbose=False)
        if valid:
            valid_strings.append(s)
    return valid_strings

def menu():
    while True:
        print("\n---- DFA MENU ----")
        print("1. Generate all valid strings")
        print("2. Validate a string")
        print("3. Exit")
        choice = input("Select (1-3): ").strip()
        if choice == "1":
            length = int(input("Length (max 10): "))
            strings = generate_all_valid_strings(length)
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
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice!")

menu()
