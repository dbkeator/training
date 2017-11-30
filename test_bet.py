import sys, getopt, os
from os.path import basename,join,isfile
import nipype.interfaces.fsl as fsl

filename="sub-0001_T1w.nii.gz"
filestem=os.path.splitext(os.path.splitext(filename)[0])[0]

#fslreorient = fsl.Reorient2Std()
#fslreorient.run(in_file=filename, out_file=filestem+"ro.nii.gz")

#extract brain
bet = fsl.BET()
bet.run(in_file=filename, out_file=filestem+"_brain.nii.gz", frac=0.8, mask=True)
