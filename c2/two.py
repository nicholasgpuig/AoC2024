def main():
    with open('input.txt') as f:
        lines = f.readlines()
    
    safe = 0
    for line in lines:
        nums = list(map(int, line.split()))
        if is_safe(nums):
            safe += 1
        else:
            for i in range(len(nums)):
                modified_nums = nums[:i] + nums[i+1:]
                if is_safe(modified_nums):
                    safe += 1
                    break
    return safe


def is_safe(nums):
    if len(nums) < 2:
        return True

    increasing = all(1 <= nums[i+1] - nums[i] <= 3 for i in range(len(nums) - 1))
    decreasing = all(-3 <= nums[i+1] - nums[i] <= -1 for i in range(len(nums) - 1))
    return increasing or decreasing


if __name__ == "__main__":
    print(main())