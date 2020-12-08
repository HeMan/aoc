import uaoc


class Day3(uaoc.Streaming):
    def parsefile(self, right, down):
        pos = right
        count = 0
        self.file.seek(0)
        for d in range(down):
            self.file.readline()
        while True:
            line = self.file.readline()
            if not line:
                break
            if line[pos % 31] == "#":
                count += 1
            pos += right
            for d in range(down - 1):
                self.file.readline()
        return count

    def run(self):
        with open(self.filename) as self.file:
            self.part1 = self.parsefile(3, 1)
            self.part2 = self.part1
            self.part2 *= self.parsefile(1, 1)
            self.part2 *= self.parsefile(5, 1)
            self.part2 *= self.parsefile(7, 1)
            self.part2 *= self.parsefile(1, 2)


d = Day3("day3")
d.run()
d.display()
print(d)
