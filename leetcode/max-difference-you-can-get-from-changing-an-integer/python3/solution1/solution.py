from typing import Iterator, Iterable, Optional, Tuple


class Solution:
    def maxDiff(self, n: int) -> int:
        digits = list(to_digits(n))
        
        max_from = digits[0]
        max_to = 9
        for d in digits:
            if d == 9:
                continue
            max_from = d
            break
        
        min_from = digits[0]
        min_to = 1
        for i, d in enumerate(digits):
            if d == 0:
                continue
            if d == 1:
                continue
            min_from = d
            if i != 0:
                min_to = 0
            break
        
        max_num = mount_to_int([max_to if e == max_from else e for e in digits])
        min_num = mount_to_int([min_to if e == min_from else e for e in digits])
        
        return max_num - min_num


def largest_power_of_or_none(x: int, base: int = 10) -> Optional[int]:
    try:
        return largest_power_of(x, base)
    except Exception:
        return None


def largest_power_of(x: int, base: int = 10) -> int:
    _, power = largest_exponent_and_power_of(x, base)
    return power


def largest_exponent_and_power_of(x: int, base: int = 10) -> Tuple[int, int]:
    exponent = 0
    power = 1
    while power * base <= x:
        power *= base
        exponent += 1
    return exponent, power


def to_digits(n: int, radix: int = 10) -> Iterator[int]:
    self = abs(n)
    power = largest_power_of_or_none(self, radix)
    if power is None:
        power = 1
    
    while power > 0:
        yield self // power
        self %= power
        power //= radix


def mount_to_int(digits: Iterable[int], radix: int = 10) -> int:
    mounted = 0
    for digit in digits:
        mounted *= radix
        mounted += abs(digit)
    return mounted
