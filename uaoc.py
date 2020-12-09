import machine
from ssd1306 import SSD1306_I2C


class Streaming:
    def __init__(self, day):
        self.part1 = 0
        self.part2 = 0
        self.filename = "{}.txt".format(day)
        self.i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))

        self.oled = SSD1306_I2C(128, 64, self.i2c, 0x3C)
        self.oled.fill(0)
        self.oled.text("Running {}".format(day), 0, 0)
        self.oled.show()

    def __repr__(self):
        output = """Todays problem
---------
Part1: {}
Part2: {}"""
        return output.format(self.part1, self.part2)

    def line(self, data):
        pass

    def emptyline(self, data=None):
        pass

    def eof(self, data=None):
        pass

    def do_part1(self):
        pass

    def do_part2(self):
        pass

    def display(self):
        self.oled.fill(0)
        self.oled.text("Result", 0, 0)
        self.oled.text("Part 1: {}".format(self.part1), 0, 10)
        self.oled.text("Part 2: {}".format(self.part2), 0, 20)
        self.oled.show()

    def run(self):
        with open(self.filename) as f:
            while True:
                line = f.readline()
                if line and not line == "\n":
                    self.line(line.strip())
                if line == "\n":
                    self.emptyline(line)
                if not line:
                    self.eof(line)
                    break
        self.do_part1()
        self.do_part2()
