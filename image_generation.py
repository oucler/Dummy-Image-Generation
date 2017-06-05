import numpy as np
import argparse
import matplotlib.pyplot as plt

class imageGeneration:
    def __init__(self,args):
        self.pass_image_dir = args.pass_image_dir
        self.failure_image_dir = args.failure_image_dir
        self.image_size = args.image_size
    def generate(self):
        #image = np.zeros([self.image_size[0],self.image_size[1],3]).astype(np.uint8)
        #orig_img = np.zeros([self.image_size[0],self.image_size[1],3]).astype(np.uint8)
        rows = np.random.permutation(self.image_size[0])
        columns = np.random.permutation(self.image_size[1])
        for row in rows:
            for column in columns:
                image = np.zeros([self.image_size[0],self.image_size[1],3]).astype(np.uint8)
                image[row,column] = [255,255,255]
                if ( (column*row > ((self.image_size[1]/2)*(self.image_size[0]/2))) ):
                    img_name  = self.failure_image_dir + "/" + str(row*column) +".png"
                else:
                    img_name  = self.pass_image_dir + "/" + str(row*column) +".png"
                plt.imsave(img_name,image)   
            #image = orig_img
        #plt.imshow(image)
        
def main():
    parser = argparse.ArgumentParser(description="Generating dummy images")
    parser.add_argument('-pass_image_dir',help='passing images',dest='pass_image_dir',type=str,default='data/pass')
    parser.add_argument('-failure_image_dir',help='failing images',dest='failure_image_dir',type=str,default='data/failure')
    parser.add_argument('-image_size',help='image size',dest='image_size',type=int,default=(32,32))
    args = parser.parse_args()
    
    ig = imageGeneration(args)
    ig.generate()

if __name__ == '__main__':
    main()