#https://leetcode.cn/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        while s:
            if s[0]=='M':
                num+=1000
                s=s[1:]
                if len(s)==0:
                    break
            if s[0]=='C':
                if len(s)>1:
                    if s[1]=='M':
                        num+=900
                        s=s[2:]
                        if len(s)==0:
                            break
                    elif s[1]=='D':
                        num+=400
                        s=s[2:]
                        if len(s)==0:
                            break
                    else:
                        num+=100
                        s=s[1:]
                        if len(s)==0:
                            break
                else:
                    num+=100
                    s=s[1:]
                    if len(s)==0:
                        break
            if s[0]=='D':
                num+=500
                s=s[1:]
                if len(s)==0:
                    break
            if s[0]=='X':
                if len(s)>1:
                    if s[1]=='L':
                        num+=40
                        s=s[2:]
                        if len(s)==0:
                            break
                    elif s[1]=='C':
                        num+=90
                        s=s[2:]
                        if len(s)==0:
                            break
                    else:
                        num+=10
                        s=s[1:]
                        if len(s)==0:
                            break
                else:
                    num+=10
                    s=s[1:]
                    if len(s)==0:
                        break
            if s[0]=='L':
                num+=50
                s=s[1:]
                if len(s)==0:
                    break
            if s[0]=='I':
                if len(s)>1:
                    if s[1]=='X':
                        num+=9
                        s=s[2:]
                        if len(s)==0:
                            break
                    elif s[1]=='V':
                        num+=4
                        s=s[2:]
                        if len(s)==0:
                            break
                    else:
                        num+=1
                        s=s[1:]
                        if len(s)==0:
                            break
                else:
                    num+=1
                    s=s[1:]
                    if len(s)==0:
                        break
            if s[0]=='V':
                num+=5
                s=s[1:]
                if len(s)==0:
                    break
        return num
