from modules import text_suite as ts

print("READ OR WRITE? (CASE SENSITIVE)")
choice = input()

if choice == "READ":
    ts.write_text()

if choice == "WRITE":
    ts.read_text()
