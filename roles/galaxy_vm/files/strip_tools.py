import os


def main():
    os.system("mkdir ./galaxy/tools/tool_dependencies")
    os.system("cat ./roles/galaxy_vm/files/lapps_galaxy.ini > ./galaxy/config/galaxy.ini")
    os.system("rm ./galaxy/config/galaxy.ini.sample")
    os.system("cat ./roles/galaxy_vm/files/lapps_tool_conf.xml > ./galaxy/config/tool_conf.xml")

main()
