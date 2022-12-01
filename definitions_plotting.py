import numpy as np 
import matplotlib.pyplot as plt

def plotter(kx, fy, fft_data, mesh):
	labels = ["Mx", "My", "Mz"]
	ext = [kx[0]*1e-6, kx[-1]*1e-6, fy[0]*1e-9, fy[-1]*1e-9]
	for comp in range(3):
		fig, ax = plt.subplots()
		pcm = ax.imshow(fft_data[comp], aspect = 'auto', interpolation='kaiser',extent=ext)
		ax.set_ylabel('Frequency (GHz)')
		ax.set_xlabel('Wavenumber (rad/'u'\u03BC''m)')
		ax.set_title('Dispersion relation, %s' %labels[comp])
	plt.show()


