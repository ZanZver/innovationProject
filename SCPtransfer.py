from paramiko import SSHClient
from scp import SCPClient

# SSH/SCP Directory Recursively     
def ssh_scp_files(ssh_host, ssh_user, ssh_password, ssh_port, source_volume, destination_volume):
    logging.info("In ssh_scp_files()method, to copy the files to the server")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('137.221.149.141', username='zanserver', password='bcuserver2019', look_for_keys=False)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(source_volume, recursive=True, remote_path=destination_volume)
