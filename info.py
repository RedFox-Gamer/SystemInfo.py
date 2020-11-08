import platform

#Dictionary
info = {}

#Defining the things we search for, then adding it to the "info" dictionary
platform_details = platform.platform()
info["Platform Details"] = platform_details

system_name = platform.system()
info["System Name"] = system_name

processor_name = platform.processor()
info["Processor Name"] = processor_name

architecture_details = platform.architecture()
info["Operating System"] = architecture_details

system_release = platform.release
info["Release"] = system_release

#Printing the information
for i, j, in info.items():
    print(i, " - ", j)