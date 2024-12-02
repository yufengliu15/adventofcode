def part2():
    safe_count = 0
    with open("text.txt") as f:
        for row in f:
            prev_level = None
            dec = None
            safe = True
            unsafe_count = 0
            print(row)
            for level in row.strip().split(" "):
                if prev_level == None:
                    prev_level = int(level)
                    continue
                difference = int(level) - prev_level

                if (difference < 0 and dec == None):
                    dec = True
                elif (difference > 0 and dec == None):
                    dec = False

                if (abs(difference) > 3 or abs(difference) < 1):
                    unsafe_count += 2
                    safe = False
                if (difference > 0 and dec or difference < 0 and not dec):
                    unsafe_count += 1
                    safe = False
                prev_level = int(level)
            print(f"Safe: {safe}, unsafe_count: {unsafe_count}")
            
            if safe or unsafe_count < 2:
                safe_count += 1     

    print(safe_count)    
                
def part1():
    safe_count = 0
    with open("text.txt") as f:
        for row in f:
            prev_level = None
            dec = None
            safe = True
            for level in row.strip().split(" "):
                if prev_level == None:
                    prev_level = int(level)
                    continue
                difference = int(level) - prev_level

                if (difference < 0 and dec == None):
                    dec = True
                elif (difference > 0 and dec == None):
                    dec = False

                if (abs(difference) > 3 or abs(difference) < 1):
                    safe = False
                if (difference > 0 and dec or difference < 0 and not dec):
                    safe = False
                prev_level = int(level)
            
            if safe:
                safe_count += 1     

    print(safe_count)  

if __name__ == "__main__":
    part2()