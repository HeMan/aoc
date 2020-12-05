def check1(rule, password):
    count, char = rule.split()
    low, high = count.split("-")
    return int(low) <= password.count(char) <= int(high)

def check2(rule, password):
    positions, char = rule.split()
    pos1, pos2 = positions.split("-")
    if password[int(pos1)] == char and password[int(pos2)] != char:
        return True
    if password[int(pos1)] != char and password[int(pos2)] == char:
        return True
    return False

count1 = 0
count2 = 0
with open("day2/input") as f:
    while True:
        try:
            rule, password = f.readline().strip().split(":")
        except ValueError:
            break
        if check1(rule, password):
            count1 += 1
        if check2(rule, password):
            count2 += 1
            
print(count1)
print(count2)
