import ure

musthaves = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate(data):
    key, value = data
    if key == "byr":
        return 1920 <= int(value) <= 2002
    if key == "iyr":
        return 2010 <= int(value) <= 2020
    if key == "eyr":
        return 2020 <= int(value) <= 2030
    if key == "hgt":
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        if value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
    if key == "hcl":
        return (
            ure.search("^\#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", value)
            is not None
        )
    if key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        return ure.search("^\d\d\d\d\d\d\d\d\d$", value) is not None
    if key == "cid":
        return True
    return False


with open("day4/input") as f:
    valid = []
    passport = set()
    count1 = 0
    count2 = 0
    while True:
        line = f.readline()
        if not line:
            if not musthaves - passport:
                count1 += 1
                if all(valid):
                    count2 += 1
            break

        if line == "\n":
            if not musthaves - passport:
                count1 += 1
                if all(valid):
                    count2 += 1
            valid = []
            passport = set()
            continue

        fields = line.split()
        passport.update({f.split(":")[0] for f in fields})
        valid.extend([validate(f.split(":")) for f in fields])


print(count1)
print(count2)
