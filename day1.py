import uaoc


class Day1(uaoc.Streaming):
    alldata = []

    def line(self, data):
        self.alldata.append(int(data))

    def do_part1(self):
        head, *tail = self.alldata
        while tail:
            rest = 2020 - head
            if rest in tail:
                self.part1 = head * rest
                return
            head, *tail = tail

    def do_part2(self):
        head1, *tail1 = self.alldata
        while tail1:
            head2, *tail2 = tail1
            while tail2:
                rest = 2020 - head1 - head2
                if rest in tail2:
                    self.part2 = head1 * head2 * rest
                    return
                head2, *tail2 = tail2
            head1, *tail1 = tail1


d = Day1("day1")
d.run()
d.display()
print(d)
