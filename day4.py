import ure

import uaoc


class Day4(uaoc.Streaming):
    musthaves = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = []
    passport = set()

    def validate(self, data):
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
                ure.search(
                    "^\#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$", value
                )
                is not None
            )
        if key == "ecl":
            return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if key == "pid":
            return ure.search("^\d\d\d\d\d\d\d\d\d$", value) is not None
        if key == "cid":
            return True
        return False

    def line(self, data):
        fields = data.split()
        self.passport.update({f.split(":")[0] for f in fields})
        self.valid.extend([self.validate(f.split(":")) for f in fields])

    def emptyline(self, data=None):
        if not self.musthaves - self.passport:
            self.part1 += 1
            if all(self.valid):
                self.part2 += 1
        self.valid = []
        self.passport = set()

    def eof(self, data=None):
        if not self.musthaves - self.passport:
            self.part1 += 1
            if all(self.valid):
                self.part2 += 1


d = Day4("day4")
d.run()
d.display()
print(d)
