# amoeba_wimbo.py
import re
import sys

def amoebaStr(s):
    if (s.endsWith(".txt"):
        with open(s,'r') as f:
            return [line for line in f]
                   
    return s.split("\n")

def amoebaResults(array):
    """
    Given the array of strings, parse the strings for the formats
    > Artist - Title - MediaType - Link
    > Artist - Title - MediaType
    > Title - MediaType
    and retrieve matched format into a comma separated string
    """
    recs_str = ""
    pattern = re.search(r'([\w\W]+) -([\w\W]+) \((LP|EP|DVD)\) ?(http[\w\W]+)?')
    for line in array:
        result = amoeba.match(line)
        if result.group(3) is None:
            recs_str += ",".join(result.group(1, 2))
        elif result.group(4) is None:
            recs_str += ",".join(result.group(1, 2, 3))
        else:
            recs_str += ",".join(result.group(1, 2, 3, 4))
                        
    return recs_str

if __name__ == "__main__":

    inputs = []
    if len(sys.argv) == 1:        
        inputs.append( input("Please input the data: ") )
    else:
        # the program assumes that either the arguments are text file names
        # or that it is one string with line breaks
        if not sys.argv[1].endsWith(".txt"):
            inputs.append(sys.argv[1])
        else:
            inputs.extend(sys.argv[1:])

    print(inputs)

    for f in inputs:
        
        a = amoebaStr(f)
        amoebaData = amoebaResults(a)
        # TODO: save the data into a file
        print(amoebaData) 

    

"They Might Be Giants - Flood (LP) \nKylie Minogue - Step Back In Time: The Definitive Collection (LP) \nThom Yorke - Tomorrow's Modern Boxes (LP) \nArt Of Noise - Who's Afraid Of The Art Of Noise? / Who's Afraid Of Goodbye? (LP) \nR.E.M. - Reckoning (LP) \nYellow Magic Orchestra - Yellow Magic Orchestra (LP) \nEmerson, Lake & Palmer - Pictures At An Exhibition (LP) \nSlothrust - parallel timeline (LP) \nDavid Lynch - Mulholland Drive (DVD) \nMy Hero Academia (DVD) \nKing Crimson - Red (LP) \nBob Stanley & Pete Wiggs - The Tears Of Technology (LP) \nOutkast - Speakerboxxx/The Love Below (LP) "
    
