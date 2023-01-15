import numpy as np

# my_array = np.array([
#   [1,4,1,13,1,2,1],
#   [4,1,4,1,101,5,1],
#    [4,5,1,2,151,7,1],
#     [11,3,3,1,10,1,7]
# ])

class SliceIndexConverter:
  def __init__(self,array,y1,y2,x1,x2):
    self.y1 = y1
    self.y2 = y2
    self.x1 = x1
    self.x2 = x2
    self.height = array.shape[0]
    self.width = array.shape[1]

  def get_slice(self,array):
    return array[self.y1:self.y2,self.x1:self.x2]

  #given an index in the slice it gives the corresponding index in the container
  def container_index(self,slice_y,slice_x):
    y = self.y1+slice_y
    x = self.x1+slice_x
    return (y,x)


#returns the indices within container array
#of an element in a slice of the container that has the value equal to the most frequent value in that slice
def get_seed_indicies(container_array,y1,y2,x1,x2):
  slice_index_converter= SliceIndexConverter(container_array,1,-1,3,-1)
  slice = slice_index_converter.get_slice(container_array)
  values,counts = np.unique(slice,return_counts=True)
  ind = np.argmax(counts)
  most_frequent = values[ind]
  row_indicies,col_indicies,_ = np.where(slice==most_frequent)
  slice_y = row_indicies[len(row_indicies)//2]
  slice_x = col_indicies[len(col_indicies)//2]
  container_y,container_x = slice_index_converter.container_index(slice_y,slice_x)
  return (container_y,container_x)