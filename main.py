from gui_design import system_update
from definitions_folders import *
from definitions_mumaxscript import *
from definitions_running import *
from definitions_mExtraction import *
from definitions_fft_calculation import *
from definitions_saver import *
from definitions_plotting import *
import class_system as c_sys
import class_mesh as c_mesh


## Update system parameters
sys = c_sys.System()
system_update(sys)
print("Parameters are updated.")

mesh = c_mesh.meshh(sys)

while True:
	## Create folder where data is stored
	simfolder = set_simfolder(sys)
	print("Simulation results can be found in")
	print(simfolder)

	## Build mumax script
	script_name = "mumax3_script"
	script_path = simfolder+"/"+script_name+".mx3"
	build_mumax_script(sys, mesh, script_path)

	## Run mumax
	stop = running(script_path, mesh)
	if stop:
		break

## Extract and convert the magnetization data
output_path = simfolder+"/"+script_name+".out"
m_data_tot = m_extraction(output_path)

## Do fft on the magnetization data
kx, fy, fft_data = fft_calculation(m_data_tot, sys, mesh)

## Save the data
data_saver(kx, fy, fft_data, simfolder)

## Plot the result
plotter(kx, fy, fft_data, mesh)

