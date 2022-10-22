import telnetlib
import getpass

host = input("Enter Device IP Address: ")
user = input("Enter  telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user + "\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password + "\n")
    tn.write("en\n")
    tn.read_until(b"Password: ")
    tn.write("1234\n")
    tn.write("clock set 17:00:00 22 Okt 2022\n")
    tn.write("conf t\n")
    tn.write("hostname RTR1\n")
    tn.write("vlan 50\n")
    tn.write("name admin\n")
    tn.write("vlan 60\n")
    tn.write("name staf\n")
    tn.write("vlan 70\n")
    tn.write("name student\n")
    tn.write("end\n")
    tn.write("exit\n")
print("Successful Config")    
print (tn.read_all())
