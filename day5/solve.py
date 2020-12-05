from array import array

seats = array(
    "Q",
    [0 for _ in range(16)],
)


def set_bit(s_id):
    longword = s_id // 64
    bit = s_id % 64
    lw = seats[longword]
    lw |= 1 << bit
    seats[longword] = lw


def find_empty(highest):
    initialempty = True
    for seat in range(highest):
        longword = seat // 64
        bit = seat % 64
        lw = seats[longword]
        if initialempty and (lw & 1 << bit):
            initialempty = False
        if not initialempty and not (lw & 1 << bit):
            print(seat)


def seat_id(line):
    row = int(line[:7].replace("B", "1").replace("F", "0"), 2)
    seat = int(line[7:].replace("R", "1").replace("L", "0"), 2)
    return row * 8 + seat


highest = 0
with open("day5/input") as f:
    for line in f.readlines():
        s_id = seat_id(line.strip())
        set_bit(s_id)
        if s_id > highest:
            highest = s_id

print(highest)
find_empty(highest)
