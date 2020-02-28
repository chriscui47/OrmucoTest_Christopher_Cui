import re
def compare(ver1,ver2):


    #assumes < major >.< minor >.< patch >-< buildnumb> pattern match

    #Cannot have negative input
    if (ver1==None or ver2==None):
        return ("Invalid empty input")
    if (len(ver1)==0 or len(ver2)==0):
        return ("Invalid empty input")

    if(ver1[0]=='-' or ver2[0]=='-'):
        return ("Negative value versions not accepted")
    #we make sure, that the ONLY inputs are integers and decimal. If this regex match does not match input, then we know there
    #was an invalid input
    ver1Match=re.match('^\d+(\.+\d+)*$',ver1)
    ver2Match=re.match('^\d+(\.+\d+)*$',ver2)

    if not (ver2Match and ver1Match):
       return ("Wrong format")

    ver1Split=ver1.split(".")
    ver2Split=ver2.split(".")
    if len(ver1Split)<len(ver2Split):
        shortest=ver1Split
        longest=ver2Split
    elif len(ver2Split)<len(ver1Split):
        shortest=ver2Split
        longest=ver1Split
    #set arbitrary to smaller or shortest if they are same length. doesn't effect loop length if both same length
    else:
        shortest=ver2Split
        longest=ver1Split
    
    #we iterate thru shortest version. 
  
    for i in range(len(longest)):
        
        v1=int(shortest[i]) if i<len(shortest) else 0
        v2=int(longest[i])
        if v2>v1:
            return "{} is GREATER than {}".format(".".join(longest),".".join(shortest))
        if v2<v1:
            return "{} is SMALLER than {}".format(".".join(longest),".".join(shortest))

    
    #then, after comparasons if doesnt return, hen they must be equal
    EQUAL= "{} is EQUAL to {}".format(".".join(longest),".".join(shortest))
    return EQUAL
 
 
            
print(compare("41.4123211.2","4.4.1"))
        