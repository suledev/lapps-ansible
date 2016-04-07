# Lapps-Ansible

Package to automate installing of tools into a local Galaxy instance.

# Usage

You're going to need to configure the playbook in main.yml and give the appropriate variables for your galaxy instance
then enter this line into the cli to set up the tools. 

ansible-playbook install_tools.yml -i 'localhost,' --extra-vars galaxy_tools_api_key=<Enter Key>


