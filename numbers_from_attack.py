import regex

file = open("list.txt", "r")
r_str = r"\d\d\d \d\d\d \d\d \d\d"
lines = file.read()
matches = regex.findall(r_str, lines)

wfile = open("yemek_numbers.txt", "w")
for match in matches:
    wfile.write(match.replace(" ","") + "\n")