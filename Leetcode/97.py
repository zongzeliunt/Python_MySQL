class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "" and s2 == "" and s3 == "":
            return 1
        if s1 == "": 
            if s3 == s2:
                return 1
            else:
                return 0
        if s2 == "": 
            if s3 == s1:
                return 1
            else:
                return 0
        
        self.s1_len = len(s1)
        self.s2_len = len(s2)
        self.s3_len = len(s3)
        
        matrix = []
        for i in range (self.s1_len + 1):
            tmp = []
            for j in range (self.s2_len + 1):
                tmp.append(0)
            matrix.append(tmp)
        
        if self.s3_len != self.s1_len + self.s2_len:
            return 0
        
        matrix[0][0] = 1
        

        for i in range (self.s1_len + 1):
            for j in range (self.s2_len + 1):
                if i == 0 and j == 0:
                    continue
                s1_pos = i - 1
                s2_pos = j - 1
                s3_pos = i + j - 1
                if j == 0:
                    left = 0
                else:
                    left = matrix[i][j-1]

                if i == 0:
                    up = 0
                else:
                    up = matrix[i-1][j]

                if left == 1 and up == 0:
                    if s3[s3_pos] == s2[s2_pos]:
                        matrix[i][j] = 1
                elif up == 1 and left == 0:
                    if s3[s3_pos] == s1[s1_pos]:
                        matrix[i][j] = 1
                elif up == 1 and left == 1:
                    matrix[i][j] = 1
                


        print ("matrix")

        tmp = "    "
        for i in range (self.s2_len + 1):
            if i != 0:
                tmp += s2[i - 1] + " "
        print(tmp)


        tmp = ""
        for i in range (self.s1_len + 1):
            if i != 0:
                tmp = s1[i - 1] + " "
            else:
                tmp = "  "
            for j in range (self.s2_len + 1): 
                tmp += str(matrix[i][j]) + " "
            print(tmp)

        if matrix[self.s1_len][self.s2_len] == 1:
            return 1
        return 0




#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbbbaccc"
#s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
#s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
#s3 = "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
#s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
#s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
#s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
s1 = "aabd"
s2 = "abdc"
s3 = "aabdbadc"


sol = Solution()

result = sol.isInterleave(s1,s2,s3)
print ("result")
print (result)

