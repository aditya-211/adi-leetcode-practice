class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x > 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit
            
        # Apply sign
        reversed_x *= sign
        
        # Check if the result overflows 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
            
        return reversed_x