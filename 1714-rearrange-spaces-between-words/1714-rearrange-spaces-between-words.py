class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        total_spaces = text.count(' ')
        n = len(words)
        if n == 1:
            return words[0] + ' ' * total_spaces
        spaces_between = total_spaces // (n - 1)
        extra_spaces = total_spaces % (n - 1)
        res = (' ' * spaces_between).join(words)
        res += ' ' * extra_spaces
        return res
