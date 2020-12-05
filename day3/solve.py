def parsefile(f, right, down):
    pos = right
    count = 0
    f.seek(0)
    for d in range(down):
        f.readline()
    while True:
        line = f.readline()
        if not line:
            break
        if line[pos % 31] == "#":
            count += 1
        pos += right
        for d in range(down-1):
            f.readline()
    return count

product = 1
with open("day3/input") as f:
    product *= parsefile(f, 1, 1)
    product *= parsefile(f, 3, 1)
    product *= parsefile(f, 5, 1)
    product *= parsefile(f, 7, 1)
    product *= parsefile(f, 1, 2)
    
    print(product)
