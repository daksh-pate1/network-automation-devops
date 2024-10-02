import paramiko
from datetime import datetime

def backup_device(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('show running-config')
        config = stdout.read().decode()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"backup_{ip}_{timestamp}.txt", 'w') as f:
            f.write(config)

        print(f"Backup completed for {ip}")
        ssh.close()

    except Exception as e:
        print(f"Error backing up device {ip}: {str(e)}")

if __name__ == "__main__":
    ip = input("Enter device IP: ")
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    backup_device(ip, username, password)
