class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        newbinaire = 0
        ch = bin(n)[2:].zfill(32)
        for i in range(len(ch)):
            if (ch[i] == '1'):
                newbinaire+= 2**count
            count+=1
        return newbinaire

print(Solution().reverseBits(43261596))
print(Solution().reverseBits(2147483644))