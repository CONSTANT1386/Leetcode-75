# Can't satisfy the requirement for O(1) space complexity

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        count = 1
        for index, char in enumerate(chars):
            if index == 0:
                result.append(char)
                continue
            if char == chars[index-1]:
                count = count + 1
            else:
                if count != 1:
                    for n in str(count):
                        result.append(n)
                    count = 1
                result.append(char)
        if count != 1:
            for x in str(count):
                result.append(x)
        chars = result
        return len(result)
