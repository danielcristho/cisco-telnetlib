import telnetlib
import getpass

host = raw_input("masukan IP telnet:")
user = raw_input("masukan   username:")
password = getpass.getpass()

hostname = raw_input("masukan hostname switch : ")
vlan2 = raw_input("masukan vlan : ")
vlan_name2 = raw_input("masukan nama vlan :")
vlan3 = raw_input("masukan vlan : ")
vlan_name3 = raw_input("masukan nama vlan :")
vlan4 = raw_input("masukan vlan : ")
vlan_name4 = raw_input("masukan nama vlan :")

tn = telnetlib.Telnet(host)

tn.read_until("Username:")
tn.write(user + "\n") 
if password:
#run cisco command
    tn.read_until("Password:")
    tn.write(password + "\n")
    tn.write("en\n")
    tn.read_until("Password:")
    tn.write("1234\n")
    tn.write("clock set 01:57:00 20 Mar 2021\n")
    tn.write("conf t\n")
    tn.write("hostname {}\n".format(hostname))
    tn.write("vlan  {}\n".format(vlan2))
    tn.write("name  {}\n".format(vlan_name2))
    tn.write("vlan  {}\n".format(vlan3))
    tn.write("name  {}\n".format(vlan_name3))
    tn.write("vlan  {}\n".format(vlan4))
    tn.write("name  {}\n".format(vlan_name4))
   

#exit   
    tn.write("end\n")
    tn.write("exit\n")
print("Successful Config")    
print tn.read_all()
