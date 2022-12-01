import numpy as np

class System:

	#Physical constants
	MU0 = 1.257*10**(-6)        # [N/A^2] = [Tm/A]
	GAMMA = 1.76*10**(11)       # [rad/(sT)]
	fmax = 30e9 
	t_eq = 10e-9 

	def __init__(self):
		# Default System Parameters
		self.width = 200e-9
		self.thick = 18e-9

		self.Ms = 1200e3
		self.Aex = 18e-12
		self.alpha = 4e-3

		self.B0 = 200e-3
		self.IP_angle = 0   #[rad - BVW=0]
		self.OP_angle = 0   #[rad - FVW = pi/2]

		self.l_end = 500e-9	#Waveguide ends are neglected
		self.y0 = 0 		#[-w/2, w/2]
		self.z0 = 0  		#[-t/2, t/2]

	## Derived parameters
	@property
	def wm(self):
		return self.GAMMA*self.MU0*self.Ms

	@property
	def w0(self):
		return self.GAMMA*self.B0
	
	@property
	def wres(self):
		#Approximation for resonance frequency
		return np.sqrt(self.w0*(self.w0+self.wm))

	@property
	def lex(self):
		# Exchange length
		return np.sqrt(self.Aex*2/(self.MU0 * self.Ms**2)) 

	@property
	def sus(self):
		#Approximation for susceptibility [thesis Claus Blitzer]
		return self.wm/(self.alpha*self.wres)

	@property
	def tau(self):
		#Approximation for lifetime
		return 1/(self.alpha*(self.w0+0.5*self.wm))

	@property
	def time(self):
		#Simulation time
		if 10*self.tau < 3e-9:
			return 3e-9
		else:
			return 10*self.tau

	@property
	def vg(self):
		#Approximation for group velocity
		return self.wm*self.thick/4

	@property
	def length(self):
		#Waveguide length 
		if 15*self.tau*self.vg < 5e-6:
			return 5e-6
		else:
			return 15*self.tau*self.vg



