#
# [mst] regex.py 
# doodling with regular expressions matching in python
#
# log:
# -simple regex "match to list" search
# -[wip] replace a match group
#

import re   # regex matching functionality


##### simple patten matching
pattern = re.compile("[\n ]+")  # match a new line or a space char
if pattern.search("data "):
    print("match")
else:
    print("no match")


############################################# [here]
#[wip] refresh this
# with open('py2_file.py') as f:
#     patt = re.compile('print') 
#     for line in f:
#         match = re.search('print', line)
#         if match:
#             print ("spotted a print")
      
            
# refresh this [wip][here]
###matches_list = [re.findall(r'print(?!\s*[\(\)])\s*(.*)',line)
###matches_list = [re.findall(r'print',line) 
###     for line in open('py2_file.py')]

f = open('py2_file.py','r')
fl = f.readlines() # readlines reads the individual lines into a list
for line in fl:
    matches_list = re.findall(r'print',line)

print (matches_list)
# 
# replace_str = 'print'
# print (replace_str + str(matches_list[1]))

