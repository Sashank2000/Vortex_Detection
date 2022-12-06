import os
import sys
sys.path.append("/home/sashankk/Downloads/visit3_3_0.linux-x86_64-ubuntu20/visit3_3_0.linux-x86_64/3.3.0/linux-x86_64/lib/site-packages/")
sys.path.append("/usr/local/lib/python3.7/dist-packages/")
from visit import *
from pathlib import Path


testfile = input("Enter Path of Database : ")
Launch()
testfile_path = "/home/sashankk/Proj/maxhelmaxrot/data_vz0/velocity10000"+testfile+".h5"
my_file = Path(testfile_path)



if my_file.is_file():
	OpenDatabase(testfile_path)
else :
	print("File Not Found !!")
	sys.exit(1)


DefineVectorExpression("v","{<PS/vx>,<PS/vy>,<PS/vz>}")
DeleteAllPlots()
AddPlot("Vector","v")


a=AnnotationAttributes()
a.axes3D.visible=0
a.axes3D.triadFlag=0
a.axes3D.bboxFlag=0
a.databaseInfoFlag=0
a.legendInfoFlag=0
SetAnnotationAttributes(a)

va=VectorAttributes()
va.colorTableName="amino_shapely"
va.nVectors=40000
va.lineStem=0
SetPlotOptions(va)


viewatt=View2DAttributes()
# viewatt.imageZoom=1.47
SetView2D(viewatt)
DrawPlots()
SaveWindow()



exit()
