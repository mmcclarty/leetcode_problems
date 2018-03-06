class Solution(object):
    def findShortestSubArray(self, nums):
        """
        Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum           
	frequency of any one of its elements.

        Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same             
	degree as nums.

        :type nums: List[int]
        :rtype: int
        """
        
        num_dict = {}
        
        for idx, num in enumerate(nums):
            # Note that setdefault checks whether the key exists, if so, appends to the value, if not, creates
            num_dict.setdefault(num, []).append(idx)
            
        # Find the maximum length of the array of indexes for each number in the dictionary 
        mx_degree = max(len(arrs) for arrs in num_dict.itervalues())
        
        # Finally, return the minimum first-index-to-last-index count for each of the longest arrays in the                 
	dictionary
        return (min([((arrs[len(arrs)-1]+1) - arrs[0]) for arrs in num_dict.itervalues() if                            
	len(arrs)==mx_degree]))