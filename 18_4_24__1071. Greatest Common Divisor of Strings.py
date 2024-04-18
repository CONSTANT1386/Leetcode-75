class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        flag = 0
        m = len(str1)
        n = len(str2)
        gcd = ''
        str3 = ''
        for chars in str1:
            str3 += chars
            temp = str3
            while(len(temp)<=max(m,n)):
                if str1 == temp:
                    flag += 1
                if str2 == temp:
                    flag += 1
                if flag == 2:
                    gcd = str3
                temp += str3
            flag = 0
        return gcd
                
Note:
1. the comparasion of len() need using =
