import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException, BadHostKeyException
 
try:
    client = paramiko.SSHClient()
    #client.load_system_host_keys()
    client.connect('192.168.5.186', username='Mani', password='nexii', timeout=5)
except AuthenticationException:
    print("Authentication failed, please verify your credentials: %s")
except SSHException as sshException:
    print("Unable to establish SSH connection: %s" % sshException)
except BadHostKeyException as badHostKeyException:
    print("Unable to verify server's host key: %s" % badHostKeyException)
except Exception as e:
    print("Operation error: %s" % e)
