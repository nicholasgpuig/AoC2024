import re

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    #lines = ["}why()'//mul(118,270)who(768,873)'mul(303,230)'"]

    total = 0
    enabled = True
    for line in lines:
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        out = re.findall(pattern, line)
        print(out)
        for pat in out:
            if pat == "do()":
                enabled = True
            elif pat == "don't()":
                enabled = False
            elif enabled:
                digits = r"\d{1,3}"
                d = list(map(int, re.findall(digits, pat)))
                total += d[0] * d[1]
    return total
print(main())