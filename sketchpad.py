from matplotlib.path import Path
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

#tupVerts=[(86, 52), (85, 52), (81, 53), (80, 52), (79, 48), (81, 49), (86, 53),
# (85, 51), (82, 54), (84, 54), (83, 49), (81, 52), (80, 50), (81, 48),
# (85, 50), (86, 54), (85, 54), (80, 48), (79, 50), (85, 49), (80, 51),
# (85, 53), (82, 49), (83, 54), (82, 53), (84, 49), (79, 49)]
tupVerts=[(1,1),(1,4),(4,4),(3,1)]
img = np.ones((10, 10)) * range(0, 10)
x, y = np.meshgrid(np.arange(10), np.arange(10)) # make a canvas with coordinates
x, y = x.flatten(), y.flatten()
points = np.vstack((x,y)).T 

p = Path(tupVerts) # make a polygon
print("p ={}".format(p))
grid = p.contains_points(points)
print("points ={}".format(points))
print("grid ={}".format(grid))
mask = grid.reshape(10,10) # now you have a mask with points inside a polygon
print("mask ={}".format(mask))

extract = np.extract(mask, img)
#extract = np.transpose(extract)
#result = np.where(mask == True)
mean = np.mean(extract)
result = np.nonzero(mask)
print("img={}".format(img))
print("extract ={}".format(extract))
print("mean ={}".format(mean))
print("result ={}".format(result))
listOfCoordinates= list(zip(result[0], result[1]))
for cord in listOfCoordinates:
    print(cord)

