class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without extra space.
        
        :type x: int
        :rtype: bool
        """
        ls_x = list(str(x))
        if ls_x == ls_x[::-1]:
            return True
        else: 
            return False