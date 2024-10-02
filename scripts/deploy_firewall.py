import paramiko

def deploy_firewall_rule(ip, username, password, rule):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        command = f"firewall-cmd --permanent --add-rich-rule='{rule}'"
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.exec_command("firewall-cmd --reload")
        print(f"Firewall rule applied to {ip}")
        ssh.close()

    except Exception as e:
        print(f"Error applying firewall rule to {ip}: {str(e)}")

if __name__ == "__main__":
    ip = input("Enter device IP: ")
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    rule = input("Enter firewall rule (e.g., rule family='ipv4' source address='192.168.1.1' accept): ")
    deploy_firewall_rule(ip, username, password, rule)
