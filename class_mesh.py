import math

class meshh():

	SRF = 1 	#Spatial Resolution Factor
	SRFz = 2 	#Spatial Resolution Factor

	def __init__(self, sys):
		# Default System Parameters
		self.dt = 1/(2*sys.fmax)
		self.Nt = 0							#Needs to be updated from mumax simulation
		self.Nxx = math.ceil(sys.length/(self.SRF*sys.lex))
		if self.Nxx >= 2**12:				#Dipolar interaction absent if Nx>2**12... 
			self.Nx = 2**12-1
		else:
			self.Nx = self.Nxx
		self.Ny = math.ceil(sys.width/(self.SRF*sys.lex))
		self.Nz = math.ceil(sys.thick/(self.SRFz*sys.lex))
		self.dx = sys.length/self.Nx
		self.dy = sys.width/self.Ny
		self.dz = sys.thick/self.Nz
		self.Nxmin = int(sys.l_end/self.dx)
		self.Nxmax = int(self.Nx - self.Nxmin)

		