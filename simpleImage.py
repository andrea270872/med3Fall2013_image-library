# Edited by Andrea Valente
# Original code by (alphabetical order)
# - Steven Moensted Nielsen
# - Victor Mihaita
# - Vlad Andrei Fagarasan

class simpleImage(object):

    def __init__(self,width,height):
        self.width = width # number of columns
        self.height = height # number of rows

        # create the matrix of pixels
        self._pixels=[]
        for i in range(self.height):
            self._pixels.append( [0]*self.width ) # python trick :)

    def getPixelAt(self,row,column):
        assert row>=0 and row<self.height,"The row index is out of range"
        assert column>=0 and column<self.width,"The column index is out of range"
        return self._pixels[row][column]

    def setPixelAt(self,graylevel, row,column):
        #And thus we got rid of the exceeded boundary problem. 
        if graylevel > 255:
            graylevel = 255      
        if graylevel < 0:
            graylevel = 0
        self._pixels[row][column] = graylevel

    def __str__(self):
        description = ""
        for rowIndex in range(self.height):
            description += str(self._pixels[rowIndex]) + "\n"
        return description

    def saveToPGM(self,fileName):
        """ For details about the PGM format:
            http://paulbourke.net/dataformats/ppm/ """
        f = open(fileName+".pgm", 'w')

        f.write("P2\n") # magic number
        f.write( ("%d %d \n" % (self.width,self.height) )) # dimensions
        f.write("255\n") # how many gray levels
        for rowIndex in range(self.height):
            for colIndex in range(self.width):
                #print rowIndex,colIndex
                f.write( ("%03d " % self.getPixelAt(rowIndex,colIndex)) )
            f.write("\n")
        f.close()
        
    def negative(self):
        for rowIndex in range(self.height):
            for colIndex in range(self.width):
                # good idea to explicitate some intermediary steps ;)
                newValue = 255 - self.getPixelAt(rowIndex,colIndex)
                self.setPixelAt(newValue,rowIndex,colIndex)


    def addToBrightness(self,deltaBrightness):
        for rowIndex in range(self.height):
            for colIndex in range(self.width):
                newValue = deltaBrightness + self.getPixelAt(rowIndex,colIndex)
                self.setPixelAt(newValue,rowIndex,colIndex)

    def setGrayLevel(self,graylevel):
        for rowIndex in range(self.height):
            for colIndex in range(self.width):
                self.setPixelAt(graylevel,rowIndex,colIndex)
        # ... possibly optimization: use the same trick as in the __init__

    def increaseContrast(self,contrastFactor):
        assert contrastFactor>=0,"The contrast value has to be positive"
        for rowIndex in range(self.height):
            for colIndex in range(self.width):
                # it is important to cast the newValue to int, otherwise
                # all pixels will be turned into float :(
                newValue = int( contrastFactor * self.getPixelAt(rowIndex,colIndex) )
                self.setPixelAt(newValue,rowIndex,colIndex)


    # this should be a class method,
    # so I can call it to create an image
    # - Fixed to be more independent from the formatting :)
    @staticmethod
    def readPGM(fileName):
        tempImg = simpleImage(1,1)
        f = open(fileName+ ".pgm",'r')
        tempImg.magicNo = f.readline()
        tempImg.width, tempImg.height = [int(x) for x in f.readline().split()]
        tempImg.maxGrayLevel = f.readline()
        
        values = []
        for line in f.readlines():
            values.extend(line.split())
        #print values
        
        count = 0
        tempImg._pixels = []
        for j in range(tempImg.height):
            column = []
            for i in range(tempImg.width):
                column.append( int(values[count]) )
                count += 1
            tempImg._pixels.append( column )
        return tempImg
    
    def clone(self):
        clonedImage = simpleImage(self.width,self.height)
        for row in range(self.height):
            for col in range(self.width):
                value = self.getPixelAt(row,col)
                clonedImage.setPixelAt(value,row,col)
        return clonedImage

    ### see:
    ### http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/?wpmp_tp=1
    # fills all pixels from a give location (row,column)
    # when the pixel is different from oldGrayLevel, it stops filling
    def floodFillAt(self,oldGrayLevel,newGrayLevel,row,column):
        # first check that row and column exist!
        if row<0 or row>=self.height:
            return
        if column<0 or column>=self.width:
            return
        
        currentPixel = self.getPixelAt(row,column)
        if currentPixel != oldGrayLevel: # the base case
            return
        self.setPixelAt(newGrayLevel,row,column)
        
        self.floodFillAt(oldGrayLevel,newGrayLevel,row,column+1) # right
        self.floodFillAt(oldGrayLevel,newGrayLevel,row,column-1) # left
        self.floodFillAt(oldGrayLevel,newGrayLevel,row+1,column) # down
        self.floodFillAt(oldGrayLevel,newGrayLevel,row-1,column) # up


## TO DO ==========================================================
    # Implement a thresholding operator.
    # READ MORE: http://en.wikipedia.org/wiki/Thresholding_(image_processing)
    def threshold(self,thresholdValue):
        """ Apply thresholding on a grayscale image, to convert it to a
            binary (black/white) image.
            All values below or equal to the given thresholdValue
            will be mapped to 0, otherwise they get mapped to 255 """
        # TO DO
        pass

    def median1D(self):
        # TO DO
        """ implement a median filter. 1D case, with radius 3. """
        pass


    def median(self):
        # TO DO
        """ see if you can implement the pseudo-code in 
          http://en.wikipedia.org/wiki/Median_filter#2D_median_filter_pseudo_code
          with fixed radius = 3
        """
        pass

# =======================================================

def test1():
    myImage = simpleImage(9,10)
    print myImage

    myImage.negative()
    print myImage # the image should be negative!

    myImage.addToBrightness(20)
    print myImage # the image should be brighter!

    myImage.setGrayLevel(15)
    myImage.setGrayLevel(-5)
    print myImage

    myImage.setPixelAt(10,1,1)
    myImage.setPixelAt(200,1,2)

    myImage.increaseContrast(1.5)
    print myImage

    myImage.saveToPGM("test")
    
def test2():
    myImage = simpleImage.readPGM("test123")
    print myImage

    myImage.floodFillAt(0,123,5,5)
    print myImage
    myImage.saveToPGM("test2")

    
if __name__ == "__main__":
    #test1()
    test2()
