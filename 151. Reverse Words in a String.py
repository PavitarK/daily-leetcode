"""
Leetcode Problem 151 
Reverse Words in a String
"""
# beats 95% of submissions
# parses list once
def reverseWords(self, s: str) -> str:
    words = s.split(" ")
    output = ''
    for word in reversed(words): 
        if word != '':
            if output == '':
                output = word
            else: 
                output = output + " " + word
    return output