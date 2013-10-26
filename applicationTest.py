from simpleImage import *

myImage1=simpleImage(3,3)
print "Image 1"
print myImage1

myImage2=simpleImage(2,2)
print "Image 2"
print myImage2

myImage3=simpleImage(2,3)
print "Image 3"
print myImage3

print "Image 1 Modifications"

myImage1.increaseContrast(2.5)
print myImage1

myImage1.setPixelAt(154,1,2)
print myImage1

print "Image 2 Modifications"

myImage2.setGrayLevel(55)
print myImage2
myImage1.saveToPGM("image1Test")

myImage2.addToBrightness(100)
print myImage2

myImage2.increaseContrast(0.75)
print myImage2
myImage2.saveToPGM("image2Test")

print "Image 3 Modifications"

myImage3.negative()
print myImage3

myImage3.addToBrightness(-25)
print myImage3

myImage3.saveToPGM("image3Test")


