

# import os
# import scp
# client = scp.Client(host="137.221.149.141", username="zanserver", password="bcuserver2019")
# client.transfer("desktop/AD1.jpg", "~/innovationProject/frec/facrec")


# import subprocess

# filepath = "/Users/EKOTCE/Desktop/AD1.jpg"
# hostname = "zanserver@137.221.149.141"
# remote_path = "~/innovationProject/frec/facrec"

# subprocess.call(['scp', filepath, ':'.join([hostname,remote_path])])

from paramiko import SSHClient
from scp import SCPClient

# SSH/SCP Directory Recursively     
def ssh_scp_files(ssh_host, ssh_user, ssh_password, ssh_port, source_volume, destination_volume):
    #logging.info("In ssh_scp_files()method, to copy the files to the server")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(ssh_host, username=ssh_user, password=ssh_password, look_for_keys=False)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(source_volume, recursive=True, remote_path=destination_volume)

ssh_scp_files('137.221.149.141', 'zanserver', 'bcuserver2019', 22, "/Users/EKOTCE/Desktop/AD1.jpg", "~/innovationProject/frec/facrec")

