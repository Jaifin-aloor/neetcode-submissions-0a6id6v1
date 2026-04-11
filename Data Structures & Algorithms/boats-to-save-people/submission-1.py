class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people)-1

        while l <= r:
            if people[r] == limit: 
                res += 1
                r -= 1
                continue
            if people[r] + people[l] > limit:
                res += 1
                r -= 1
            else:
                res += 1
                l, r = l + 1, r - 1
        return res
                
