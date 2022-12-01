import os
import glob
import shutil

def get_user_code():
	cwd = os.getcwd()
	count = 0
	usercode = ""
	for i in cwd:
		if i == "/":
			count += 1
			continue
		if count == 4:
			break
		if count == 3:
			usercode += i
	return usercode

def get_userfolder():
	users = {"vdveke41": "frederic", "ciubot43": "florin", "narduc82": "daniele"}
	userfolder = "/imec/other/magwaves/users/" + users[get_user_code()] + "/"
	return userfolder

def get_rootfolder():
	userfolder = get_userfolder()
	rootfolder = userfolder + "numerical_dispersion_calculator"
	if not os.path.exists(rootfolder):
		print("Hello there, this is the first time that you execute me.")
		print("Welcome to the numerical dispersion calculator!")
		print("Hope to see you soon again! :)")
		print("-------------------------------------------------")
		print('Press enter to continue...')
		x = input()
		os.makedirs(rootfolder)
	return rootfolder

def set_simfolder(sys):
	simfoldername = str(int(sys.Ms*1e-3))+"Ms_"+str(int(sys.Aex*1e12))+"Aex_" + str(int(sys.alpha*1e5))+"a_" + str(int(sys.B0*1e3))+"Bext_" + str(int(sys.width*1e9)) +"W_"+ str(int(sys.thick*1e9))+"t_" + str(int(sys.y0*1e9))+"y_"+ str(int(sys.z0*1e9))+"z"
	simfolder = get_rootfolder() + "/" + simfoldername
	if os.path.exists(simfolder):
		shutil.rmtree(simfolder)
	os.makedirs(simfolder)
	return simfolder




