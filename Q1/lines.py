class Line:
    def __init__(self,x1=None,x2=None):
        self.x1=x1
        self.x2=x2



def overlap(line1=None, line2=None):
##denote OVERLAP as a true, and false as they do not.

    #make sure nonempty
    if (line1==None or line2==None):
        raise Exception("Both lines have to be non empty")

    if(line1.x1==None or line1.x2==None or line2.x1==None or line2.x2==None):
        raise Exception("Both lines have to have components x1 x2 that are non empty")
    if (line1.x1==line1.x2):
        raise Exception("Line 1 has length 0")
    if (line2.x2==line2.x1):
        raise Exception("Line 2 has length 0")

    #if any component is the same, they overlap by definition
    if line1.x1==line2.x1 or line1.x1==line2.x2 or line1.x2==line2.x1 or line1.x2==line2.x2:
        return True

#Checks if lines overlap. If so, return true. if not, return false. we do it all in 1 statement to reduce complexity
    return not (line2.x2 < line1.x1 or line1.x2 < line2.x1)
    
line1=Line(2,6)
line2=Line(3,4)
print(overlap(line1,line2))