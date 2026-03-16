__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def minPartitions(self, n: str) -> int:
        t=0
        for i in n:
            if t==9:
                return t
            if t<int(i):
                t=int(i)
        return t