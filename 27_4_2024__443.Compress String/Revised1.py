class Solution:
    def compress(self, chars: List[str]) -> int:
        # left: the left edge of string group
        # right: the index of reading -> the right edge of string group
        # write: the index of writing
        write = left = 0
        n = len(chars)
        for read in range(n):
            if read == n-1 or chars[read] != chars[read+1]:
                chars[write] = chars[read]
                write += 1
                count = read - left +1
                if count > 1:
                    for char in str(count):
                        chars[write] = char
                        write += 1
                left = read + 1
        return write
