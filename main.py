import string

def count(x):
    return len(x)

with open("books/frankenstein.txt") as f:
    file = f.read()

count(file.split())

az = string.ascii_lowercase
letters = {}
for w in file.lower():
    if w in az:
        letters[w] = letters[w] + 1 if w in letters else 1

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count(file.split()):d} words found in the document")
print("")
for c in sorted(letters):
    print(f"The '{c:s}' character was found {letters[c]:d} times")
print("--- End report ---")