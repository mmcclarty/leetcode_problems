class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        Given a list of sorted characters letters containing only lowercase letters, and given a target letter             target, find the smallest element in the list that is larger than the given target.

        Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer           is 'a'.

        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Make a sorted list of only unique values of original list
        letters = list(sorted(set(letters)))
        
        for i in range(0, len(letters)):
            # If the target is between two elements in the list, return the larger
            if letters[i] < target < letters[i + 1] or letters[i] == target:
                return letters[i + 1]
            # If it is less than the element, return the element
            elif target < letters[i]:
                return letters[i]
            # If it is greater or equal to the last element, return the first element
            elif target >= letters[len(letters)-1]:
                return letters[0]
            else:
                continue
        