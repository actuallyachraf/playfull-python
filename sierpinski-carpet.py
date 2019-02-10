import numpy as np
from PIL import Image

total = 8

# size of the image 
size = 3**total 
  
# creating an image 
square = np.empty([size, size, 3], dtype = np.uint8) 
color = np.array([0, 0, 0], dtype = np.uint8) 
  
# filling it black 
square.fill(255) 
  
for i in range(0, total + 1): 
    stepdown = 3**(total - i) 
    for x in range(0, 3**i): 
          
        # checking for the centremost square 
        if x % 3 == 1: 
            for y in range(0, 3**i): 
                if y % 3 == 1: 
                      
                    # changing its color 
                    square[y * stepdown:(y + 1)*stepdown, x * stepdown:(x + 1)*stepdown] = color 
  
# saving the image produced 
save_file = "sierpinski-black.jpg"
Image.fromarray(square).save(save_file) 
  
