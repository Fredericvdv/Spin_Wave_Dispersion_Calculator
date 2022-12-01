import numpy as np



def data_saver(kx, fy, fft_data, simfolder):
	lab = ["Mx","My", "Mz"]
	np.savetxt(simfolder+"/kx.dat", kx)
	np.savetxt(simfolder+"/fy.dat", fy)
	for comp in range(3):
		file_name = simfolder+"/data_%s.dat" %lab[comp]
		np.savetxt(file_name, np.flip(fft_data[comp], axis=0))
		# np.savetxt(file_name, fft_data[comp])np.flip(m,axis=0)

		# fille = open(file_name, "w")
		# write_data(kx, fy, fft_data, fille)
		# fille.close()