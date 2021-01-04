"""给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # rch = ''.join(ch.lower() for ch in s if ch.isalnum())
        # return rch == rch[::-1]

        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True


test = Solution()
a = test.isPalindrome('race a car')
print(a)