from tkinter import *
import tkinter.ttk
import numpy as np


def system_update(sys):

	###################
	#Create GUI
	###################
	master = Tk()
	master.title("Numerical Dispersion Calculator - Frederic Vanderveken")

	#Geometry 
	l_geom=Label(master, text="Waveguide dimesnions:", bg="lightblue", font=(None,12), cursor="dot")
	l_geom.grid(row=0, column=0, sticky=W)

	l_width=Label(master, text="Waveguide width (nm)")
	l_width.grid(row=1, column=0, sticky=E)
	e_width=Entry(master)
	e_width.insert(0, str(sys.width*1e9))
	e_width.grid(row=1, column=1, sticky=W)

	l_thick=Label(master, text="Waveguide thickness (nm)")
	l_thick.grid(row=2, column=0, sticky=E)
	e_thick=Entry(master)
	e_thick.insert(0, str(sys.thick*1e9))
	e_thick.grid(row=2, column=1, sticky=W)

	#Material sysameters
	l_sysams=Label(master, text="Material pameters:", bg="lightblue", font=(None,12))
	l_sysams.grid(row=3, column=0, sticky=W)

	l_Ms=Label(master, text="Magnetization (kA/m)")
	l_Ms.grid(row=4, column=0, sticky=E)
	e_Ms=Entry(master)
	e_Ms.insert(0, str(sys.Ms/1000))
	e_Ms.grid(row=4, column=1, sticky=W)

	l_Aex=Label(master, text="Exchange constant (pJ/m)")
	l_Aex.grid(row=5, column=0, sticky=E)
	e_Aex=Entry(master)
	e_Aex.insert(0, str(sys.Aex*1e12))
	e_Aex.grid(row=5, column=1, sticky=W)

	l_alpha=Label(master, text="Damping constant")
	l_alpha.grid(row=6, column=0, sticky=E)
	e_alpha=Entry(master)
	e_alpha.insert(0, str(sys.alpha))
	e_alpha.grid(row=6, column=1, sticky=W)

	#Field 
	l_field=Label(master, text="External field:", bg="lightblue", font=(None,12))
	l_field.grid(row=7, column=0, sticky=W)

	l_B0=Label(master, text="External field (mT)")
	l_B0.grid(row=8, column=0, sticky=E)
	e_B0=Entry(master)
	e_B0.insert(0, str(sys.B0*1e3))
	e_B0.grid(row=8, column=1, sticky=W)

	l_IP_angle=Label(master, text="In-plane angle H0 (BVW=0 -- DE=90)")
	l_IP_angle.grid(row=9, column=0, sticky=E)
	e_IP_angle=Entry(master)
	e_IP_angle.insert(0, str(sys.IP_angle))
	e_IP_angle.grid(row=9, column=1, sticky=W)

	l_OP_angle=Label(master, text="Out-of-plane angle H0 (FVW=90)")
	l_OP_angle.grid(row=10, column=0, sticky=E)
	e_OP_angle=Entry(master)
	e_OP_angle.insert(0, str(sys.OP_angle))
	e_OP_angle.grid(row=10, column=1, sticky=W)

	#Data selection region 
	l_field=Label(master, text="Data selection:", bg="lightblue", font=(None,12))
	l_field.grid(row=11, column=0, sticky=W)

	l_y0=Label(master, text="y-position (y=0 is middle) (nm)")
	l_y0.grid(row=12, column=0, sticky=E)
	e_y0=Entry(master)
	e_y0.insert(0, str(sys.y0))
	e_y0.grid(row=12, column=1, sticky=W)

	l_z0=Label(master, text="z-position (z=0 is middle) (nm)")
	l_z0.grid(row=13, column=0, sticky=E)
	e_z0=Entry(master)
	e_z0.insert(0, str(sys.z0))
	e_z0.grid(row=13, column=1, sticky=W)

	master.rowconfigure(14,minsize=20)

	#Buttom to update sysams
	b_start=Button(master,text="Start the program!", bg="green", font=(None,12), command=lambda: update_sysams())
	b_start.grid(row=15,column=0, columnspan=2, sticky=W+E)

	############################
	# Functions necessary for the GUI
	############################
	def update_sysams():
		#Geometry sysams
		sys.width = float(e_width.get())*1e-9      #[m]
		sys.thick = float(e_thick.get())*1e-9      #[m]

		#Material sysams
		sys.Ms     = float(e_Ms.get())*1000    	#[A/m]
		sys.Aex    = float(e_Aex.get())*1e-12  	#[J/m]
		sys.alpha  = float(e_alpha.get())            

		#External field
		sys.B0        = float(e_B0.get())*1e-3   		#[T]
		sys.IP_angle  = float(e_IP_angle.get())*np.pi/180      #[rad] in-plane
		sys.OP_angle  = float(e_OP_angle.get())*np.pi/180    #[rad] out-plane

		#Region selection
		sys.y0 = float(e_y0.get())*1e-9
		sys.z0 = float(e_z0.get())*1e-9

		#Destroy gui
		master.destroy()

	master.mainloop()