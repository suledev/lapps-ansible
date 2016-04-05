import tools
import sys
import os


def run():
    command = "ansible-playbook "
    for arg in sys.argv:
        command += arg_grab(arg)
    begin_installation(command)


def arg_grab(arg):
    if arg == "-lapps":
        return "~/Dropbox/lapps-ansible/tasks/lapps-tools.yml"
    if arg == "-list":
        tools.list_tools()
        exit(0)
    if arg == "-help":
        send_help()
        exit(0)
    if arg == "lapps_installer.py":
        return " "
    else:
        print "No such toolset ~Sule"
        exit(0)

def begin_installation(command):
    print("Sule is beginning your installation :)")
    print command
    os.system(command)


def send_help():
    print "I guess you need help right now :$"
    print "Use the -list argument to list the available toolsets"
    print "Use -'name of toolset' in order to install the toolset"
    print "See README.md for more information ~Sule"


run()