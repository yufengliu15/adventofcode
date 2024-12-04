import re

def part1():
    pattern = r"mul\((\d+),(\d+)\)"
    sum = 0
    with open("input.txt") as f:
        for row in f:
            matches = re.findall(pattern, row)
            for i in matches:
                sum += int(i[0]) * int(i[1])

    return sum

def part2():
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"(don't\(\))|(do\(\))"

    mul_regex = re.compile(mul_pattern)
    do_regex = re.compile(do_pattern)
    sum = 0
    with open("input.txt") as f:
        str = ""
        for row in f:
            str += row
        matches = []

        for match in do_regex.finditer(str):
            matches.append((match.start(), match.group()))
        for match in mul_regex.finditer(str):
            matches.append((match.start(), (int(match.group(1)), int(match.group(2)))))
        
        # Sort matches by their position in the string
        matches.sort()
            
        do = True
        dont_count = 0
        do_count = 0
        #print(type(matches[0:4][1]))
        for i in matches:
            if do and isinstance(i[1], tuple):
                sum += i[1][0] * i[1][1]
            else:
                if ("don't()" in i[1]):
                    do = False
                    dont_count += 1
                elif ("do()" in i[1]):
                    do = True
                    do_count += 1
            print(f"calculating? {do}")
            print(i[0], i[1])
    
    print(dont_count)
    print(do_count)
    return sum

if __name__ == "__main__":
    print(part2())