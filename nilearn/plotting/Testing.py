import sys
import os
import nibabel
import numpy
import matplotlib
#from maps import *

# Make sources available using relative paths from this file's directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#import nibabel
#print("first")

#import matplotlib
#print("second")
from nilearn.plotting.img_plotting import *
print("third")




img = nibabel.load("C:/Users/tinas/Desktop/Sync/dsurqec_40micron.nii")
img_data = img.get_fdata()

stat = nibabel.load("C:/Users/tinas/Desktop/Sync/Rec/warped_applyTransform.nii.gz")

#dis = plot_anat(anat_img=img,display_mode = 'ortho2',cmap=plt.cm.gist_yarg)
#plot_anat(display_mode='ortho2')
#h = stat("C:/Users/tinas/Desktop/Sync/Rec/abi_nii overlay/energy.nii.gz")
#dis.add_overlay(img,cmap=plt.cm.gist_yarg)
#dis.add_overlay(stat,threshold = 1,colorbar = True)
print("fig done")

#display = plot_img(img)
#vo = display.find_cut_coords(stat,1)
#display.add_overlay(stat,threshold = 1,colorbar = True)


#cutco = nilearn.plotting.find_cuts.find_xyz_cut_coords(stat,activation_threshold=1)
#cutco2 = nilearn.plotting.find_cuts.find_xyz_cut_coords(img,activation_threshold=1)

#coords = plot_img(stat)

#plot_img(img,cut_coords= (4,4,4),black_bg=False,display_mode = 'ortho2')
##dis = plot_stat_map(stat,bg_img=img,display_mode = 'ortho2',threshold = 1)
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(0,0,0))
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(1,1,1))
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(2,2,2))
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(3,3,3))
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(4,4,4))
dis3 = plot_stat_map(stat,bg_img=img,threshold = 1,symmetric_cbar=False,cut_coords=(-2,-2,-2))
#dis2 = plot_stat_map(stat,bg_img=img,cut_coords=cutco,display_mode = 'ortho2',threshold = 1)
##plot_anat(display_mode='ortho2')
#h = stat("C:/Users/tinas/Desktop/Sync/Rec/abi_nii overlay/energy.nii.gz")
dis = plot_img(img)
dis.add_overlay(img,cmap=plt.cm.gist_yarg,colorbar=True)
dis.add_overlay(stat,threshold = 1,colorbar=True)
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







