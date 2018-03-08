class Solution(object):
    def romanToInt(self, s):
        """
	Given a roman numeral, convert it to an integer.

	Input is guaranteed to be within the range from 1 to 3999.

        :type s: str
        :rtype: int
        """
        
	# Define all the Roman numerals 
        numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
        integer = 0
	
	# Loop through the input string
        for i in range(len(s)-1):
	# If the Roman numeral preceding is less than the current numeral, subtract it from result	
            if numerals[s[i]] < numerals[s[i+1]]:
                integer -= numerals[s[i]]
	# If it is greater or equal, add it to the result
            else:
                integer += numerals[s[i]]
        # Add the final numeral to the result
	else:
            integer += numerals[s[-1]]
        
        return integer