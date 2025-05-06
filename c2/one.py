def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    safe = 0
    for line in lines:
        isSafe = True
        nums = list(map(int, line.split()))
        i = 0
        lastdiff = 0
        while i < len(nums) - 1:
            diff = nums[i + 1] - nums[i]
            if abs(diff) == 0 or abs(diff) > 3 or (lastdiff * diff) < 0:
                isSafe = False
            i += 1
            lastdiff = diff
        safe += 1 if isSafe else 0
    return safe


if __name__ == "__main__":
    print(main())