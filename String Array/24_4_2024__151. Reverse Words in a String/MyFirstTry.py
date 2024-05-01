class Solution:
    def reverseWords(self, s: str) -> str:
        list = []
        words = []
        result = ''
        for char in s:
            if char in '           ':
                if len(words):
                    list.append(''.join(words))
                    words = []
            else:
                words.append(char)

        if len(words):
            list.append(''.join(words))

        n = len(list)

        for word in range(n):
            result += list.pop()
            if word == n - 1:
                continue
            result += ' '

        return result
        
        
