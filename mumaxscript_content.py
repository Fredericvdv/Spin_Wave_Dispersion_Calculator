import math

def build_script_content(sys, mesh):
	lines = []
	lines += ["// Authomatically generated script to determine dispersion relation"]
	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Material parameters"]
	lines += ["Msat = %.2E" %sys.Ms]
	lines += ["Aex = %.2E" %sys.Aex]
	lines += ["alpha0 := %.2E" %sys.alpha]
	lines += ["lex := %.2E" %sys.lex]
	lines += ["t_eq := %.2E" %sys.t_eq]
	lines += ["t_sim := %.2E" %sys.time]

	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Dimensional parameters and mesh"]
	lines += ["length := %.2E" %sys.length]
	lines += ["width := %.2E" %sys.width]
	lines += ["thick := %.2E" %sys.thick]
	lines += ["Nx := %s" %mesh.Nx]
	lines += ["Ny := %s" %mesh.Ny]
	lines += ["Nz := %s" %mesh.Nz]
	lines += ["dx := %.2E" %mesh.dx]
	lines += ["dy := %.2E" %mesh.dy]
	lines += ["dz := %.2E" %mesh.dz]
	lines += ["SetMesh(Nx, Ny, Nz, dx, dy, dz, 0, 0, 0)"]

	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Static field"]
	lines += ["B0 := %.2E" %sys.B0]
	lines += ["IP_angle := %.2E" %sys.IP_angle]
	lines += ["OP_angle := %.2E" %sys.OP_angle]
	lines += ["B_ext = vector(B0*cos(IP_angle)*cos(OP_angle), B0*sin(IP_angle)*cos(OP_angle), B0*sin(OP_angle))"]
	
	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Equilibrium"]
	lines += ["m=uniform(1,1,1)"]
	lines += ["alpha = 0.1"]
	lines += ["run(t_eq)"]
	lines += ["alpha = alpha0"]

	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Excitation"]
	lines += ["fmax := %.2E" %sys.fmax]
	lines += ["wmax := 2*pi*fmax"]
	lines += ["lambda_min := 10*dx"]
	lines += ["kmax := 2*pi/lambda_min"]
	lines += ["A := 2e-3"]
	lines += ["// Sinc spatial profile"]
	lines += ["mask := newVectorMask(Nx, Ny, Nz)"]
	lines += ["for i:=0; i<Nx; i++{"]
	lines += ["\tfor j:=0; j<Ny; j++{"]
	lines += ["\t\tfor k:=0; k<Nz; k++{"]
	lines += ["\t\t\tr := index2coord(i, j, k)"]
	lines += ["\t\t\tx := r.X()"]
	lines += ["\t\t\tBprof := sinc(kmax*x)"]
	lines += ["\t\t\tmask.setVector(i, j, k, vector(Bprof, Bprof, Bprof))"]
	lines += ["\t\t}"]
	lines += ["\t}"]
	lines += ["}"]
	lines += ["// Sinc temporal profile"]
	lines += ["t0 := t_sim/3"]
	lines += ["B_ext.add(mask, A*sinc(wmax*(t-t_eq-t0)))"]

	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Savings"]
	lines += ["OutputFormat = OVF2_BINARY"]
	lines += ["autosave(m, 1/(2*fmax))"]
	# lines += ["TableAdd(B_ext)"]
	# lines += ["TableAutoSave( 1/(2*%.2E))" %sys.fmax]

	lines += [""]
	lines += ["/////////////////////////////////"]
	lines += ["//Running"]
	lines += ["MaxErr=1e-8"]
	lines += ["run(t_sim)"]

	return lines