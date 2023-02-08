# amoeba_wimbo.py
import re
import sys

def amoebaStr(s):
##    if (s.endsWith(".txt"):
##        with open(s,'r') as f:
##            return [line for line in f]
                   
    return s.split("\n")

def amoebaResults(array):
    """
    Given the array of strings, parse the strings for the formats
    > Artist - Title - MediaType - Link
    > Artist - Title - MediaType
    > Title - MediaType
    and retrieve matched format into a comma separated string
    """
    pattern = re.compile(r'(?:([\w\W^]+) -)?([\w\W]+)\((LP|EP|DVD)\) ?(http[\w\W]+)?')
    for line in array:
        result = pattern.match(line)
        print(",".join(result.groups("")))
       
    return result

if __name__ == "__main__":
    
    a = amoebaStr(sys.argv[1])
    amoebaData = amoebaResults(a)
    # TODO: save the data into a file
    # print(amoebaData)    
