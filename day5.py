from array import array

import uaoc


class Day5(uaoc.Streaming):
    def __init__(self, filename):
        super().__init__(filename)
        self.seats = array(
            "Q",
            [0 for _ in range(16)],
        )

    def set_bit(self, s_id):
        longword = s_id // 64
        bit = s_id % 64
        lw = self.seats[longword]
        lw |= 1 << bit
        self.seats[longword] = lw

    def do_part2(self):
        initialempty = True
        for seat in range(self.part1):
            longword = seat // 64
            bit = seat % 64
            lw = self.seats[longword]
            if initialempty and (lw & 1 << bit):
                initialempty = False
            if not initialempty and not (lw & 1 << bit):
                self.part2 = seat

    def line(self, data):
        row = int(data[:7].replace("B", "1").replace("F", "0"), 2)
        seat = int(data[7:].replace("R", "1").replace("L", "0"), 2)
        s_id = row * 8 + seat
        self.set_bit(s_id)
        if s_id > self.part1:
            self.part1 = s_id


d = Day5("day5")
d.run()
d.display()
print(d)
