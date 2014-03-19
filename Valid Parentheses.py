__author__ = 'song.yang'

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution:
    # @return a boolean
    def isValid(self, s):
        counterpart = {')':'(','}':'{',']':'['}
        left_brackets = ['(','{','[']
        right_brackets = [')','}',']']

        stack = []

        for char in s:
            if char in left_brackets:
                stack.append(char)
            if char in right_brackets:
                if stack: # Do not forget empty judgment!
                    bracket = stack.pop()
                    if counterpart.get(char) == bracket:
                        continue
                    else: return False
                else: return False

        return False if stack else True

if __name__ == '__main__':
    solution = Solution()
    print solution.isValid("([])")
