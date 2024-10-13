#!/usr/bin/python


class Solution:
    def __init__(self):
        pass
    def run(self, message):
        output = ""
        for char in message:
            if char == "y":
                output += "a"
            elif char == "z":
                output += "b"
            elif ord("a") <= ord(char) < ord("y"):
                output += chr(ord(char) + 2)
            else:
                output += char
        print(output)




answer = Solution()
answer.run("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
answer.run("map")