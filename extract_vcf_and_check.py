import regex

num_file = open("yemek_numbers.txt", "r")
s = set()
for line in num_file:
    line = line[0:-1]
    s.add(line)
    #print(line)

file = open("numbers.vcf", "r")
r_str = "type=pref:\+*(.*)\n"

s2 = set()
lines = file.read()
matches = regex.findall(r_str, lines)
for match in matches:
    match = match.replace("(", "").replace(")", "")
    if match.startswith("90"):
        match =  match.removeprefix("90").strip().replace(" ","")

    elif match.startswith("00 90"):
        match = match.removeprefix("00 90").strip().replace(" ", "")
    elif match.startswith("0"):
        match = match.removeprefix("0").strip().replace(" ", "")
    
    s2.add(match)

print(s2)
print(s.intersection(s2))