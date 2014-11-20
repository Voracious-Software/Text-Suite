from modules import text_suite

print("READ OR WRITE? (CASE SENSITIVE)")
choice = input()

if choice == "READ":
    text_suite.write_text()

if choice == "WRITE":
    text_suite.read_text()
