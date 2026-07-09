class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=0
        c=0
        for i in range(len(guess)):
            b+=int(secret[i]==guess[i])
        for j in set(secret):
            c+=min(secret.count(j), guess.count(j))

        return f"{b}A{c-b}B"

            


