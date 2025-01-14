import os 
import sys
from colorama import Fore
from smalisca.core.smalisca_main import SmaliscaApp
from smalisca.modules.module_smali_parser import SmaliParser
from recons.smarser.patterns import pattern_receiver
from recons.smarser.patterns import search_ecb



def parser():

	printflag = 0

	print(Fore.YELLOW + "\n\n--------------------------------------------------")
	print(Fore.GREEN + "[INFO] " + Fore.BLUE + "SCANNING FOR VULNERABILITIES\n")

	filename =  None
	app = SmaliscaApp()
	app.setup()

	location = 'smali_analysis'

	suffix = 'smali'

	parser = SmaliParser(location, suffix)

	parser.run()

	results = parser.get_results()

	for i in results:
		for key, values in i.items():
			if key == "path":
				filename = values

			if key == "const-strings":
				search_ecb(filename, values)
					
			elif key == "methods":
				for j in values:
					for mkey, mvalue in j.items():
						if mkey == "calls":
							# print("\n2" + str(mvalue))
							pattern_receiver(filename, mvalue)
						else:
							pass