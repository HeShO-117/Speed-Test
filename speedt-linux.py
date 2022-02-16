import speedtest ,os ,sys ,time

logo1 = """

     ██╗  ██╗███████╗███████╗    ██╗  ██╗
     ██║  ██║██╔════╝╚══███╔╝    ╚██╗██╔╝
     ███████║█████╗    ███╔╝█████╗╚███╔╝ 
     ██╔══██║██╔══╝   ███╔╝ ╚════╝██╔██╗ 
     ██║  ██║███████╗███████╗    ██╔╝ ██╗
     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝"""
os.system("clear")
print("\033[94m")

print(logo1)

m = ("\033[93m [+] MEMBER OF SL CYBER WARRIORS : 👑HEZ_X")
for x in m:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.03)
print()

os.system("clear")
time.sleep(0.2)

st = speedtest.Speedtest()

logo2 = """

     ███████╗██████╗ ███████╗███████╗██████╗
     ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
     ███████╗██████╔╝█████╗  █████╗  ██║  ██║
     ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║
     ███████║██║     ███████╗███████╗██████╔╝
     ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝"""
logo3 = """        ████████╗███████╗███████╗████████╗
        ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
           ██║   █████╗  ███████╗   ██║
           ██║   ██╔══╝  ╚════██║   ██║
           ██║   ███████╗███████║   ██║
           ╚═╝   ╚══════╝╚══════╝   ╚═╝"""
os.system("clear")

print('\033[94m' ,logo2)
time.sleep(0.2)

print('\033[0m')

print(logo3)
time.sleep(0.5)

h = ('\t\t\033[93m[+]CODDED BY : 👑HEZ_X')
for x in h:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.03)
print()

print("\n\033[92m\t\t[1] Download Speed\n\t\t[2] Upload Speed\n\t\t[3] Ping\n\t\t[4] Speedtest.net Test\n\t\t[5] Speedtest.net Full Report\n\t\t[6] Server Results\n\t\t[7] Exit")

option = int(input('\n\033[93m[+]Enter Your Choice: '))

print('\033[0m')

if option == 1:

        print("\033[96m[~]Testing Download Speed...")

        print('\n\033[0m\t' ,st.download())

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 2:

        print("\033[96m[~]Testing Upload Speed...")

        print('\n\033[0m\t' ,st.upload())

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 3:

        servernames =[]

        st.get_servers(servernames)

        print("\033[96m[~]Testing Ping...")

        print('\033[0m' ,st.results.ping)

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 4:

        print('\033[96m[~]Speedtest.net Test...\033[0m')

        os.system("speedtest-cli --simple")

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 5:

        print('\033[96m[~]Speedtest.net Full Report...\033[0m')

        os.system("speedtest-cli")

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 6:

        print('\033[96m[~]Server Results...\033[0m')

        best_server = st.get_best_server()

        for key, value in best_server.items():

                print(key, ' : ', value)

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')

elif option == 7:

        os.system("clear && exit")

else:

        print("\t\033[91mPlease enter the correct choice !")

        input('\n\033[93m[+]Enter Any Key to Continue :')

        os.system('python3 speedt-linux.py')
