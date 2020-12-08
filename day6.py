import uaoc


class Day6(uaoc.Streaming):
    answerset1 = set()
    answerset2 = set()
    newset = True

    def line(self, data):
        self.answerset1.update(data)
        if self.newset:
            self.answerset2 = set(data)
            self.newset = False
        else:
            self.answerset2.intersection_update(set(data))

    def emptyline(self, data=None):
        self.newset = True
        self.eof(data)

    def eof(self, data=None):
        self.part1 += len(self.answerset1)
        self.answerset1 = set()
        self.part2 += len(self.answerset2)


d = Day6("day6")
d.run()
d.display()
print(d)
