class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        n = len(digits)-1
        while carry and n>-1:
            if carry:
                digits[n] += 1
                carry = False
            if digits[n] == 10:
                digits[n] = 0
                carry = True
            n -= 1
        if carry: digits = [1] + digits
        return digits
                

            
        