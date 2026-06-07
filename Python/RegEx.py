
# Python Regular Expression


import re
taxt = "15 hasan is a good boy"
pattern = "[a-n]"
a = re.findall(pattern,taxt)
print(a)

pattern1 = "^1"
b = re.findall(pattern1,taxt)
if b:
    print("1 is a spcel carecter")
else:
    print("1 is not a spcel carecter")


pattern2 = r"\d"    #r = Raw string
                       # এটি হলো Python-এর একটি string টাইপ, যেটা backslash (\)–কে special meaning না দিয়ে একে একে character হিসেবে ধরে।
c = re.findall(pattern2,taxt)
# if c:
#     print("1 is a spcec carecter")
print(c)

# Metacharacters
# Character	     Description	                                                                      Example

# [ ]	         A set of characters	                                                              "[a-m]"
# \	             Signals a special sequence (can also be used to escape special characters)          	"\d"
# .	             Any character (except newline character)	                                           "he..o"
# ^	             Starts with                                                                           "^hello"
# $	             Ends with	                                                                           "planet$"
# *	             Zero or more occurrences	                                                           "he.*o"
# +	             One or more occurrences	                                                            "he.+o"
# ?	             Zero or one occurrences	                                                           "he.?o"
# {}	         Exactly the specified number of occurrences                                          "he.{2}o"
# |	             Either or	                                                                        "falls|stays"

# Special Sequences
# \A	Returns a match if the specified characters are at the beginning of the string
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
 	    #(the "r" in the beginning is making sure that the string is being treated as a "raw string")
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
 	    #(the "r" in the beginning is making sure that the string is being treated as a "raw string")
# \d	Returns a match where the string contains digits (numbers from 0-9)
# \D	Returns a match where the string DOES NOT contain digits
# \s	Returns a match where the string contains a white space character
# \S	Returns a match where the string DOES NOT contain a white space character
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W	Returns a match where the string DOES NOT contain any word characters
# \Z	Returns a match if the specified characters are at the end of the string

# Flag	           Shorthand	       Description
# re.ASCII	       re.A                Returns only ASCII matches
# re.DEBUG		   ____                Returns debug information
# re.DOTALL	       re.S	               Makes the . character match all characters (including newline character)
# re.IGNORECASE	   re.I	               Case-insensitive matching
# re.MULTILINE	   re.M	               Returns only matches at the beginning of each line
# re.NOFLAG		   ____                Specifies that no flag is set for this pattern
# re.UNICODE	   re.U	               Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches
# re.VERBOSE	   re.X	               Allows whitespaces and comments inside patterns. Makes the pattern more readable

# Example
import re
txt = "Aland"

#Find all ASCII matches:
print(re.findall(r"\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall(r"\w", txt))

#Same result using the shorthand re.A flag:
print(re.findall(r"\w", txt, re.A))