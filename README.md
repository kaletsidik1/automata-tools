# Deterministic Finite Automata (DFA) and String Generators

Short description
- DFA validator and string generators: generate/validate strings for a sample DFA and produce strings starting with `a` containing `b0` over `{a,b,c,0}`.

Files
- `formal1.py`: Original DFA implementation — validator and generator for the sample DFA.
- `formal2.py`: Original string generator producing strings that start with `a` and contain `b0` over alphabet `{a,b,c,0}`.
- `main.py`: Merged interactive program combining `formal1.py` and `formal2.py` functionality (interactive menu).

Usage
- Run the interactive program:
```
python -u "d:\@year - 4\assignment\main.py"
```
- Menu options in `main.py`:
  - `1` Generate all valid strings for the DFA (specify length)
  - `2` Validate an input string against the DFA
  - `3` Generate strings that start with `a` and contain `b0` over `{a,b,c,0}` (specify length)
  - `4` Exit

Suggested repository name
- `dfa-strings`

License
- Add a license of your choice (e.g., MIT) if you plan to publish this repository.
