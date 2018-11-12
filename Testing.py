import sys
import os
import nibabel
import numpy
import matplotlib
from maps import *

# Make sources available using relative paths from this file's directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#import nibabel
#print("first")

#import matplotlib
#print("second")
from nilearn.plotting.img_plotting import *
print("third")




img = nibabel.load("C:\\Users\\tinas\\Desktop\\Sync\\Rec\\abi_40_average.nii.gz")
img_data = img.get_fdata()

#plot_img(img,cut_coords= (4,4,4),black_bg=False,display_mode = 'ortho2')
#plot_stat_map(img,display_mode = 'ortho2')
plot_anat(display_mode='ortho2')
h = stat("C:/Users/tinas/Desktop/Sync/Rec/abi_nii overlay/energy.nii.gz")
print("fig done")
#plot.show()

z = 70

mesh = matplotlib.pyplot.imread("C:\\Users\\tinas\\Desktop\\Nilearn_MeshTestPic.png")
hm = matplotlib.pyplot.gcf()

rect = 0.4,0.1,0.5,0.5
ax_mesh = hm.add_axes(rect)


#ax_mesh = hm.add_subplot(224)
ax_mesh.get_xaxis().set_visible(False)
ax_mesh.get_yaxis().set_visible(False)
ax_mesh.patch.set_alpha(0.1)
ax_mesh.spines["top"].set_visible(False)
ax_mesh.spines["bottom"].set_visible(False)
ax_mesh.spines["right"].set_visible(False)
ax_mesh.spines["left"].set_visible(False)

img_mesh = matplotlib.pyplot.imshow(mesh)
matplotlib.pyplot.show()

z = 70







