import numpy as np 
import math 
import scipy.fftpack

## m_data = (Nt, Ncomp, Nz, Ny, Nx)

def extract_useful_m(m_data, sys, mesh):
	Ny0 = int(sys.y0/mesh.dy+mesh.Ny/2)
	Nz0 = int(sys.z0/mesh.dy+mesh.Nz/2)
	return m_data[:,:,Nz0,Ny0,mesh.Nxmin:mesh.Nxmax]

def interchange_rows(fft_out):
	for comp in range(3):
		for i in range(int(len(fft_out[0])/2)):
			fft_out[comp][[i,-1-i]] = fft_out[comp][[-1-i, i]]
	return fft_out

def calc_2Dfft(m_useful_data):
	fft_out = []
	for comp in range(3):
		fft_compl = scipy.fftpack.fft2(m_useful_data[:,comp,:])
		fft_compl = fft_compl[0:len(fft_compl)//2, 0:len(fft_compl[0])//2]
		fft_out += [np.abs(fft_compl)]
	fft_out=np.asarray(fft_out)
	return interchange_rows(fft_out)

def calc_axes(sys,mesh):
	freq_f = np.fft.fftfreq(mesh.Nt, d=mesh.dt)
	freq_f = freq_f[0:len(freq_f)//2]
	freq_k = np.fft.fftfreq(mesh.Nxmax-mesh.Nxmin, d=mesh.dx)
	freq_k = freq_k[0:len(freq_k)//2]*2*3.1415
	return freq_k, freq_f


def rm_statics(m_data, Nt):
	for i in range(Nt):
		m_data[i] = m_data[i] - m_data[0]
	return m_data

def ind_closed_val(array, value):
	#Find index corresponding to kxmax
    return (np.abs(array - value)).argmin()

def fft_calculation(m_data_tot,sys, mesh):
	mesh.Nt = len(m_data_tot)
	m_data = rm_statics(m_data_tot, mesh.Nt)

	## Take useful region
	m_useful_data = extract_useful_m(m_data, sys, mesh)

	##Take fft
	kx, fy = calc_axes(sys, mesh)
	fftt2 = calc_2Dfft(m_useful_data)

	##Only take wavenumber range that is excited by sinc
	idxx = ind_closed_val(kx, 2*np.pi/(10*mesh.dx))
	fft_data = fftt2[:, :, 0:idxx]
	kx = kx[0:idxx]

	return kx, fy, fft_data

	
