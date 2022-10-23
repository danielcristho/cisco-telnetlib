import telnetlib
import getpass
print("======================================")
print("NetAutomation Using Telnetlib")
print("======================================")
loop = "x"
while(loop == "x"):
    if loop !="x":
        break
    host = input("masukan IP address:")
    user = input("masukan username:")
    password = getpass.getpass()

    # print list
    print("======================================")
    print("Silahkan Pilih konfigurasi")
    print("1. Change Hostname")
    print("2. Create Vlan")
    print("3. Show Vlan")
    print("4. Show Interface")
    print("======================================")

    tn = telnetlib.Telnet(host)
    tn.read_until("Username:")
    tn.write(user + "\n")
    if password: 
        tn.read_until("Password:")
        tn.write(password + "\n")
        opt = input("Enter the menu that you want: ")

    #option
    if opt=="1":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        tn.write("configure terminal\n")
        hostname = input("1. Enter the hostname : ")
        tn.write("hostname {}\n".format(hostname))
        tn.write("end\n")
        tn.write("exit\n")
        print (tn.read_all())

    elif opt=="2":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        tn.write("configure terminal\n")
        vlan = input("2. Add new Vlan : ")
        vlan_name = input("2. Add name : ")
        tn.write("vlan {}\n".format(vlan))
        tn.write("name {}\n".format(vlan_name))
        tn.write("end\n")
        tn.write("exit\n")
        print (tn.read_all())

    elif opt=="3":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        tn.write("show vlan brief\n")
        tn.write("exit\n")
        print (tn.read_all())
    else:
        print("Incorrect Option!!")

    print("======================================") 
    loop = input("Config again? (y,n) ")
    print("======================================")   
