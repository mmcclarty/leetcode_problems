class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
	
	# Convert to string
        x = str(x)
	
	# Reverse string
        rev_x = x[::-1]
        
	# Check for minus sign 
        if rev_x.endswith("-"):
            rev_x = list(rev_x)	
	    # Remove from list and rejoin at beginning
            rev_x.insert(0, rev_x.pop())
	    # Map list strings to integers		
            rev_int = int(''.join(map(str,rev_x)))
        else:
            rev_int = int(rev_x) 
        
	# Check for overflow
        if (abs(int(rev_int)) > (2 ** 31 - 1)):
            return 0
        else:
            return rev_int