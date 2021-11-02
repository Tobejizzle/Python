# AUTO-CHROME-EXTENSION
# WRITTEN BY TOBY G IN 2021

import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
        	os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def data_collect(): 
	print('--FILL OUT YOUR PROJECT SETTINGS--\n')
	manifest_version = input(bcolors.WARNING + 'MANIFEST VERSION (1-3) > ')
	name = input('PACKAGE NAME > ')
	description = input('DESCRIPTION > ')
	version = input('PACKAGE VERSION (default is 1) > ')
	author = input('AUTHOR > ')
	background_scripts = input('BACKGROUND SCRIPTS (.js) > ')
	matches = input('MATCHES (empty for all urls) >')
	content_scripts = input('CONTENT SCRIPTS (.js) >')
	popup_ask = input('POPUP HTML FILE (y/n) > ')
	print('\n' + bcolors.ENDC)

	try:
		createFolder('./extension/')
		print(bcolors.OKCYAN +'FOLDER CREATED...')
		time.sleep(0.5)
	except:
		print(bcolors.FAIL + 'FOLDER FAILED TO CREATE.')

	try:	
		with open('./extension/manifest.json', 'w') as manifest:	
			
			manifest.write('{ \n')

			manifest.write('	"manifest_version": ' + manifest_version + ',\n')
			manifest.write('	"name": "' + name + '",\n')
			manifest.write('	"description": "' + description + '",\n')
			manifest.write('	"version": "' + version + '",\n')
			manifest.write('	"author": "' + author + '",\n')
			manifest.write('\n')
			
			manifest.write('	"background": {\n')
			manifest.write('		"scipts": ["' + background_scripts + '.js"]\n')
			manifest.write('	}, \n')
		
			manifest.write('	"content_scripts": [ \n')
			manifest.write('		{ \n')
			
			if matches is None:
				manifest.write('			"matches": ["' + matches + '"],\n')
			else:
				manifest.write('			"matches": ["http://*/*", "https://*/*"],\n')
			manifest.write('			"js": ["' + content_scripts + '.js"] \n')
			manifest.write('		} \n')
			manifest.write('	], \n')
			manifest.write('	"browser_action": {\n')
			manifest.write('		"default_popup": "./popup/popup.html"\n')	
			manifest.write('	}\n')
			manifest.write('}')

			print(bcolors.OKCYAN + 'MANIFEST FILE CREATED...')
			time.sleep(0.2)
	except:
		print(bcolors.FAIL + 'MANIFEST FILE FAILED TO CREATE.')
	
	try:
		with open('./extension/' + background_scripts + '.js', 'w') as background:
			background.write('console.log("bg")')
			print(bcolors.OKCYAN + 'BACKGROUND SCRIPT CREATED...')
			time.sleep(0.2)
	except:
		print(bcolors.FAIL + 'BACKGROUND SCRIPT FAILED TO CREATE.')

	if popup_ask == 'y':
		try:
			createFolder('./extension/popup/')
			print(bcolors.OKCYAN + 'POPUP FOLDER CREATED...' + bcolors.ENDC)
		except:
			print(bcolors.FAIL + 'POPUP FOLDER FAILED TO CREATE.' + bcolors.ENDC)

		try: 
			with open('./extension/popup/popup.html', 'w') as popup:
				popup.write('<!DOCTYPE html>\n')
				popup.write('<html>\n')
				popup.write('	<head>\n')
				popup.write('		<link rel="stylesheet" href="popup.css"></link>\n')
				popup.write('	</head>\n')
				popup.write('	<body>\n')
				popup.write('		<h1>Hello World! From ' + author + '</h1>\n')
				popup.write('	</body>\n')
				popup.write('</html>\n')

			with open('./extension/popup/popup.css', 'w') as popupc:
				popupc.write('body {\n')
				popupc.write('	width: max-content;')
				popupc.write('	height: max-content;')
				popupc.write('')
				popupc.write('	background-color: #1c1c1c;\n')
				popupc.write('	color: white;\n')
				popupc.write('}\n')

				print(bcolors.OKCYAN + 'POPUP FILES CREATED...' + bcolors.ENDC)
		except:
			print(bcolors.FAIL + 'POPUP HTML FAILED TO CREATE.' + bcolors.ENDC)	


	try: 	
		with open('./extension/' + content_scripts + '.js', 'w') as content:
			content.write('console.log("Hello world!")')
			print(bcolors.OKCYAN + 'CONTENT SCRIPT CREATED.\n' + bcolors.ENDC)
			print(bcolors.HEADER + 'PROGRAM MADE BY Toby | ' + bcolors.UNDERLINE + 'https://github.com/Tobejizzle/Python/tree/main/manic' + bcolors.ENDC)
	except:
		print(bcolors.FAIL + 'CONTENT SCRIPT FAILED TO CREATE.' + bcolors.ENDC)	

os.system('clear')

print('--THIS SCRIPT WILL HELP YOU CREATE A FOLDER FOR YOUR CHROME EXTENSION-- \n')
x = input(bcolors.OKGREEN + 'CONTINUE? y/n > ' + bcolors.ENDC)
print('')

if (x == "y"):
	os.system('clear')
	data_collect()
else:	
	print(bcolors.FAIL + 'CANCELED' + bcolors.ENDC)