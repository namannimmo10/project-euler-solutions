# code created by Deepankar Agrawal(@deep110)
# 10:55pm, October 03, 2019 UTC+05:30.

"""
- divide like how we divide by hand
- whenever remainder repeats, return the length of previous remainders list
"""
N = 1000

def divide(num: int) -> (bool, int):
    """
    divide 1/num and return if fraction is recurring and
    if yes, length of its recurring cycle
    """
    rems = set()
    remainder = 1
    while not ((remainder == 0) and (remainder in rems)):
        remainder = (10 * remainder) % num

        if remainder == 0:
            return (False, -1)
        
        if remainder in rems:
            return (True, len(rems))
        else:
            rems.add(remainder)


def main():
    longest_rc_number = 1
    longest_rc_value = 1

    for i in range(2, N):
        is_rc, rc_value = divide(i)
        if is_rc and rc_value > longest_rc_value:
            longest_rc_value = rc_value
            longest_rc_number = i
    
    print(longest_rc_number)

if __name__ == "__main__":
    main()