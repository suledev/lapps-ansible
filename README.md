# Lapps-Ansible

Package to automate installing of tools into a local Galaxy instance.

First:
Use ansible-playbook install_galaxy.yml -i localhost, to install the custom lapps galaxy files.

Then:
Set up your admin account in galaxy.ini and then use sh /galaxy/run.sh to startup galaxy. After get the 
admin API key associated with your new admin account. Put that API key in the install_lapps.yml file._

Lastly:
Use ansible-playbook install_lapps.yml to install the custom lapps tools.

