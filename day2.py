import uaoc


class Day2(uaoc.Streaming):
    def check1(self, rule, password):
        count, char = rule.split()
        low, high = count.split("-")
        if int(low) <= password.count(char) <= int(high):
            self.part1 += 1

    def check2(self, rule, password):
        positions, char = rule.split()
        pos1, pos2 = positions.split("-")
        if password[int(pos1)] == char and password[int(pos2)] != char:
            self.part2 += 1
        elif password[int(pos1)] != char and password[int(pos2)] == char:
            self.part2 += 1

    def line(self, data):
        rule, password = data.split(":")
        self.check1(rule, password)
        self.check2(rule, password)


d = Day2("day2")
d.run()
d.display()
print(d)
