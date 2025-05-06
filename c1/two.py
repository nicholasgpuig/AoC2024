def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    leftcol = {}
    rightcol = []
    for line in lines:
        left, right = map(int, line.split())
        leftcol[left] = 0
        rightcol.append(right)
    
    for num in rightcol:
        if num in leftcol:
            leftcol[num] += num
    
    return sum(leftcol.values())
    
if __name__ == "__main__":
    print(main())