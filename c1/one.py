def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    leftcol = []
    rightcol = []
    for line in lines:
        left, right = line.split()
        leftcol.append(int(left))
        rightcol.append(int(right))
    
    leftcol.sort()
    rightcol.sort()

    total = 0
    for i in range(len(leftcol)):
        dist = abs(leftcol[i] - rightcol[i])
        total += dist
    
    return total


if __name__ == '__main__':
    print(main())