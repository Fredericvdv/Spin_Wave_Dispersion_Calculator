import os
import shutil
from mumaxscript_content import *

def write_script_content(fille, lines):
	for i in lines:
		fille.write(i+"\n")

def build_mumax_script(sys, mesh, script_path):
	lines = build_script_content(sys,mesh)
	fille = open(script_path, "w")
	write_script_content(fille, lines)
	fille.close()

