import torch as tor
import torch.nn as nn 


class Cnn (nn.Module):
    def __init__(self):
      
      # 1 input image chanel , 6 input channels, 5x5 squre convolution kernel
      
      super(Cnn, self).__init__()   
      self.conv1 = nn.Conv2d(1,6,5)   #This  are the convolution layers
      self.conv2 = nn.Conv2d(6,16,5)  # nn.Conv2d ("Number of images in input" ,
                                      # "Number of images to be gained through output" ,
                                      # "Size of the output image which would be 5x5
                                      # hence last parameter is 5 else if rectungular image is desired then 
                                      # under parantesis using commmas the size can be altered" ) {like this -> #self.conv1 = nn.Conv2d(1,6,(5,4))}
      # the number of input in the 2nd convulation layer is the same of the number of output from the 1st convolution layer which is 6 
      
      #Am affime operation y = Wx + b 
      
      self.fc1 = nn.Linear(16 * 5* 5 , 120) # this will convert the output images into flatened layers .
      self.fc2 = nn.Linear(120 , 84)
      self.fc3 = nn.Linear(84 , 10)
      
      
      
   
      
                
    def forward(self,x): # this forward function takes the output of the images that is generated ehich is a tensor or in the other words x is the batch input which is 16
      x = tor.max_pool2d(tor.relu(self.conv1(x)) , (2,2))
      
      #  As the output of the image is 2x2 this can be defined as 2 only
      
    # x = tor.max_pool2d(tor.relu(self.conv2(x)) , 2 )
      
      #tor.relu( ) is a linear function .
      x = x.view(-1 , self.num_flat_featurs(x))
      x = tor.relu(self.fc1(x))
      x = tor.relu(self.fc2(x))
      x = self.fc3(x)
      
      return x 