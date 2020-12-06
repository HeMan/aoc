with open("day6/input") as f:
    answers1 = 0
    answers2 = 0
    answerset1 = set()
    newset = True
    while True:
        line = f.readline()
        if line and not line == "\n":
            answerset1.update(line.strip())
            if newset:
                answerset2 = set(line.strip())
                newset = False
            else:
                answerset2.intersection_update(set(line.strip()))
        else:
            answers1 += len(answerset1)
            answerset1 = set()
            answers2 += len(answerset2)
        if not line:
            break
        if line == "\n":
            newset = True

    print(answers1)
    print(answers2)
