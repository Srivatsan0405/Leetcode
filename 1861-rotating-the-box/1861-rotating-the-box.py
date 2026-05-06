class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        for i in range(n):
            empty = m - 1
            for j in range(m - 1, -1, -1):

                if boxGrid[i][j] == '*':
                    empty = j - 1

                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1

        rev = boxGrid[::-1]

        rotated = []

        for col in range(len(rev[0])):
            new_row = []

            for row in range(len(rev)):
                new_row.append(rev[row][col])

            rotated.append(new_row)

        return rotated