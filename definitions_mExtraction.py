import os
import glob
import numpy as np

def set_m_folder(output_path):
	magnetization_path = output_path+"/magnetization"
	os.makedirs(magnetization_path)
	all_m_files = glob.glob(output_path+"/m*.ovf")
	# all_m_files = glob.glob(output_path+"/B_ext*.ovf")
	for i in all_m_files:
		os.system("mv"+" "+ i +" "+magnetization_path)
	return magnetization_path

def convert_ovf_npy(magnetization_path):
	converter = "/imec/other/mumax/public/programs/go/bin/05_07_08/mumax3-convert"
	all_m_ovf = glob.glob(magnetization_path+"/*.ovf")
	for i in all_m_ovf:
		os.system(converter+" "+"-numpy"+" "+i)

def data_loading(magnetization_path):
	numpy_files = sorted(glob.glob(magnetization_path + "/*.npy"))
	all_data = []
	for i in numpy_files:
		all_data += [np.load(i)]
	return np.asarray(all_data)


def m_extraction(output_path):
	magnetization_path = set_m_folder(output_path)
	convert_ovf_npy(magnetization_path)
	return data_loading(magnetization_path)
	