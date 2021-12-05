#imports
from sys import platform
import os

#Variable Definitions
this_files_path =  os.path.abspath(__file__)
this_directory_path = os.path.dirname(os.path.abspath(__file__))
venv_path = os.path.join(this_directory_path,'venv')
main_path = os.path.join(this_directory_path,'main.py')
requirements = ['tweepy', 'python-dotenv', 'schedule']

#on linux systems:
if platform == "linux" or platform == "linux2":
    #create venv
    print(f"Log : Creating Virtual Environment @ {venv_path}...")
    os.system(f"python3 -m venv {venv_path}")
    print("-------------------")
    print()

    #cd into this directory
    print(f"Log : Changing Directory...")
    os.system(f"cd {this_directory_path}")
    print("-------------------")
    print()

    #pip installs
    print(f"Updating Pip...")
    print("+++++++++++++++++++")
    os.system(f"{venv_path}/bin/python -m pip install --upgrade pip")#make sure pip is up-to-date
    print("-------------------")
    print()

    for module in requirements:
        print(f"Log : pip installing {module}...")
        print("+++++++++++++++++++")
        os.system(f"./venv/bin/pip install {module}")
        print()
        print("-------------------")
        print()
    
    #run the files
    print()
    print("-------------------")
    print()
    print()
    print()
    print(f"Log : Run The Following command To Start Your Bot:")
    print(f"{venv_path}/bin/python {main_path}")
    

#on windows systems
elif platform == "win32":
    #create venv
    print(f"Log : Creating Virtual Environment @ {venv_path}...")
    os.system(f"python -m venv {venv_path}")
    print("-------------------")
    print()

    #cd this directory
    print(f"Log : Changing Directory...")
    os.system(f"cd {this_directory_path}")
    print("-------------------")
    print()

    #pip installs
    print(f"Updating Pip...")
    print("+++++++++++++++++++")
    os.system(f"{venv_path}\Scripts\python.exe -m pip install --upgrade pip")#make sure pip is up-to-date
    print("-------------------")
    print()

    for module in requirements:
        print(f"Log : pip instaling {module}...")
        print("+++++++++++++++++++")
        os.system(f"{venv_path}\Scripts\pip.exe install {module}")
        print()
        print("-------------------")
        print()

    #run the files
    print()
    print("-------------------")
    print()
    print()
    print()
    print(f"Log : Run The Following command To Start Your Bot:")
    print(f"{venv_path}\Scripts\python.exe {main_path}")

        