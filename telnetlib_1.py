import telnetlib
import getpass

print ("Welcome to Network Automation on Cisco")
host = raw_input("Enter Device IP Address:")
user = raw_input("Enter  telnet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username:")
tn.write(user + "\n")
if password:
    tn.read_until("Password:")
    tn.write(password + "\n")
    tn.write("en\n")
    tn.read_until("Password:")
    tn.write("1234\n")
    tn.write("clock set 03:31:00 2 Mar 2021\n")
    tn.write("conf t\n")
    tn.write("hostname SW_1\n")
    tn.write("vlan 50\n")
    tn.write("name admin\n")
    tn.write("vlan 60\n")
    tn.write("name staf\n")
    tn.write("vlan 70\n")
    tn.write("name student\n")
    tn.write("end\n")
    tn.write("exit\n")
print("Successful Config")    
print tn.read_all()
