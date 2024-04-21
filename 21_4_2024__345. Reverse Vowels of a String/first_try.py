class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels:list = []
        temp:str = []
        result:str = []
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                temp.append('_')
                vowels.append(char)
            else:
                temp.append(char)
            
        for i in temp:
            if i == ('_'):
                result.append(vowels.pop())
            else:
                result.append(i)
        return ''.join(result)
                
