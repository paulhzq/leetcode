# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        brute force solution:
        get all the substring and get the longest length of substring.
        """
        if len(s)<=1:
            return len(s)
        substrlen =[]
        for i in range(len(s)):
            dict = {}
            dict[s[i]] = 1
            for j in range(i+1,len(s)):
                if s[j] in dict:
                    substrlen.append(j-i)# substrlen = j-1-i+1
                    break
                else:
                    dict[s[j]] = 1
            else:# loop fell through without break
                substrlen.append(j-i+1)
        return max(substrlen)

print(lengthOfLongestSubstring('abc'))
