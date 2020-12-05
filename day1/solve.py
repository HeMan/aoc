import utime

def part1(data):
    head, *tail = data
    while tail:
        rest = 2020 - head
        if rest in tail:
            return head * rest
        head, *tail = tail


def part2(data):
    head1, *tail1 = data
    while tail1:
        head2, *tail2 = tail1
        while tail2:
            rest = 2020 - head1 - head2
            if rest in tail2:
                return head1 * head2 * rest
            head2, *tail2 = tail2
        head1, *tail1 = tail1

t0 = utime.ticks_us()

with open("day1/input") as f:
    data = sorted([int(line.rstrip()) for line in f])

t1 = utime.ticks_us()
print(part1(data))
t2 = utime.ticks_us()
print(part2(data))
t3 = utime.ticks_us()

print(utime.ticks_diff(t1,t0))
print(utime.ticks_diff(t2,t1))
print(utime.ticks_diff(t3,t2))

print(utime.ticks_diff(t3,t0))