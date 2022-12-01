import subprocess
import os

def running(script_path, mesh):
	mumi = "/imec/other/mumax/public/programs/go/bin/05_07_08/mumax3"
	# os.system(mumi + " " + script_path)

	try :
		subprocess.run([mumi, script_path], check = True)
		return 1
	except subprocess.CalledProcessError:
		mesh.Nx -= 1
		return 0
		