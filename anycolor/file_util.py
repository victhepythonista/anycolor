import os

OPENING_FILE_POSSIBLE_ERRORS = IOError

# this script mostlyFile manipulation related functions

Output = lambda data:print(f"dircheck : [ {data} ]")

def CheckFolders(list_of_folders):
	print('\n\n---------------------------------------------')
	Output(f"\checking {len(list_of_folders)}  folder(s)....")
	for path in list_of_folders:
		if os.path.isdir(path):
			print(path,'OK')
			continue
		Output(f"folder {path} could not be found..restoring,,,, ")
		os.makedirs(path)
		if False == os.path.isdir(path):
			Output(f" {path} could not be restored")


		Output(f" Folder -{path}- restored successfully !")
	print('\---------------------------------------------')

def CheckFiles(files_list):
	# check the files in a directory
	print('\n\n---------------------------------------------')
	Output(f"checking {len(files_list)}  file(s)....")
	for file in files_list:
		Output(f'checking file  {file}....')
		if os.path.isfile(file):
			Output(f'file  {file}  ok..')
			continue
		Output(f"file {file} could not be found..restoring,,,, ")
		try:
			with open(file, 'w') as f:
				f.close()
			Output(f" Folder -{file}- restored successfully !")
		except OPENING_FILE_POSSIBLE_ERRORS:
			Output(f" {file} could not be restored")
			raise
	print('\---------------------------------------------')
