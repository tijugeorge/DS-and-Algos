def main():
    count = [0]*10
    data = open('test.dat')

    for line in data:
        count[int(line)] = count[int(line)] + 1

    idx = 0
    for num in count:
        print idx, " occured ", num, " times."
        idx += 1
