with open("input") as f:
    data = sorted([int(line.rstrip()) for line in f])


def part1(data):
    head, *tail = data
    while tail:
        rest = 2020 - head
        if rest in tail:
            print(head * rest)
        head, *tail = tail


def part2(data):
    head1, *tail1 = data
    while tail1:
        head2, *tail2 = tail1
        while tail2:
            rest = 2020 - head1 - head2
            if rest in tail2:
                print(head1 * head2 * rest)
            head2, *tail2 = tail2
        head1, *tail1 = tail1


part1(data)
part2(data)