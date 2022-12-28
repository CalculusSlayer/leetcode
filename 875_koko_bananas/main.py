# Leetcode 875. Koko Eating Bananas
# Nayeel Imtiaz
# 12/28/22

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        lo = 1
        hi = max(piles)

        min_bananas = None
        while lo <= hi:
            mid = (hi - lo)//2
            if verify(piles, mid, h) == True:
                min_bananas = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return min_bananas

        """

        def verify(piles, k, h):
            hour_sum = 0
            for pile in piles:
                hour_sum += math.ceil(pile/k)
            if hour_sum <= h:
                return True
            else:
                return False
        
        # print(verify(piles, 4, 8))
        # print(verify(piles, 3, 8))
        # return 0
        
        lo = 1
        hi = max(piles)

        min_bananas = None
        while lo <= hi:
            mid = (lo+hi)//2
            print(f"lo = {lo}, "
                  f"hi = {hi}, "
                  f"mid = {mid}, "
                  f"min_bananas = {min_bananas}")

            if verify(piles, mid, h):
                min_bananas = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return min_bananas


def main():
    piles = [3, 6, 7, 11]
    piles2 = [30,11,23,4,20]
    piles3 = [1000]

    s = Solution()

    print(s.minEatingSpeed(piles, 8))
    print()

    print(s.minEatingSpeed(piles2, 5))
    print()

    print(s.minEatingSpeed(piles2, 6))
    print()

    print(s.minEatingSpeed(piles3, 2000))
    print()

    print(s.minEatingSpeed(piles3, 1))
    print()


if __name__ == '__main__':
    main()