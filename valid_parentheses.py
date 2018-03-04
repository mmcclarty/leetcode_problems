class Solution(object):
    def isValid(self, s):
        """
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
	

        :type s: str
        :rtype: bool
        
        """
        
        openers = []

        for i in range(0, len(s)):
	    # Extract all of the opening brackets and append to dedicated list
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                openers.append(s[i])
	    # With remaining closing contents, check for direct match in openers list
            if s[i] == ']':
                if openers == [] or openers.pop() != '[':
                    return False
            if s[i] == ')':
                if openers == [] or openers.pop() != '(':
                    return False
            if s[i] == '}':
                if openers == [] or openers.pop() != '{':
                    return False
	# If any unmatched openers remain, return False
        if openers != []:
            print(openers)
            return False
        else:
            print(openers)
            return True