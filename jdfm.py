import sys
import os
import json
import shutil
import filecmp

helpMenu = '''
--- jdfm help menu ---

--- commands ---
help: prints out this menu
init: create folder w/ json file that keeps track of links
uninit: remove jdfm folder, deletes all config and backup (current permissions error)
add (path): creates a jdfm copy of dotfile and adds filename and original path to config
remove (fileName): removes jdfm copy of dotfile and removes from config
update: writes all files from .jdfm folder to corresponding path
'''

jdfmDir = os.path.abspath(os.path.expanduser("~/jdfm"))
configFile = os.path.join(jdfmDir, ".jdfm.json")


def getConfig():
    with open(configFile, "r+") as file:
        return json.load(file)


def writeConfig(config):
    with open(configFile, "w+") as file:
        json.dump(config, file)

# --- cli commands ---


def help():
    print(helpMenu)


def init():
    os.mkdir(jdfmDir)
    config = {"dotfiles": {}}
    with open(configFile, "w") as file:
        json.dump(config, file)


def uninit():
    os.remove(jdfmDir)


def add(path):
    # create path for file
    if path.startswith("~"):
        path = os.path.abspath(os.path.expanduser(path))
    else:
        path = os.path.abspath(path)
    # check if path is a file
    if not os.path.isfile(path):
        print("{} is not a file".format(path))
        return

    # get base filename and create its destination in the jdfm directory
    fileName = os.path.basename(path)
    destination = os.path.join(jdfmDir, fileName)

    # copy the original file to jdfm directory
    shutil.copy(path, destination)

    # update the config with the new file and its path
    config = getConfig()
    config['dotfiles'][fileName] = path
    writeConfig(config)
    print("added {} to jdfm!".format(path))


def remove(fileName):
    # removes jdfm copy of dotfile
    # creates path for file in jdfm directory, checks if it exists
    path = os.path.abspath(os.path.join(jdfmDir, fileName))
    if not os.path.isfile(path):
        print("{} is not a file".format(path))
        return
    parent = os.path.split(os.path.dirname(path))[-1]
    if parent != "jdfm":
        print("{} is not in the jdfm directory".format(path))
        print("please just use the name of the file you would like to remove")
        return
    # remove file from jdfm dir
    os.remove(path)

    # remove from config
    config = getConfig()
    del config['dotfiles'][fileName]
    writeConfig(config)
    print("deleted {} from jdfm".format(fileName))


def update():
    # write all files to their corresponding location
    # make sure to check if file and location exists, notify user
    config = getConfig()
    dotfiles = config['dotfiles']
    for file in dotfiles:
        jdfmVersion = os.path.abspath(os.path.join(jdfmDir, file))
        sysVersion = os.path.abspath(dotfiles[file])
        filesAreSame = filecmp.cmp(jdfmVersion, sysVersion, shallow=False)
        if not filesAreSame:
            shutil.copy(jdfmVersion, sysVersion)
            print("updated {} at {}".format(file, sysVersion))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        help()
        quit()
    command = sys.argv[1]
    if command == "help":
        help()
    elif command == "init":
        init()
    elif command == "uninit":
        uninit()
    elif command == "add":
        path = sys.argv[2]
        add(path)
    elif command == "remove":
        fileName = sys.argv[2]
        remove(fileName)
    elif command == "update":
        update()
