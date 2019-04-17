import socket
hostandport=('127.0.0.1',12000)
mySocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


print("U ARRIT LIDHJA ME SERVERIN.NE PRITJE PER KERKESA...")
print("--------------------------------------------------------------------------------------------------")
print("Miresevini i/e nderuar.\nPer te vazhduar ju lutem perdorni njeren nga metodat e deshiruara duke shkruar ate me shkronja te medha!\n"
      "\nIPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, KONVERTO,  FIBONACCI, SHUMABIN, SHMVP\n--------------------------------------------------------------------------------------------------- ")
clientInput=input("Kerkesa juaj: ");
clientInput_S=str(clientInput)

mySocket.sendto(clientInput_S.encode(),hostandport)

if clientInput_S==str("CAP"):
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    string=input()
    mySocket.send(string.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("SHUMA"):
    msg = mySocket.recv(1024).decode()
    print(str(msg))
    no1 = input()
    no2= input()
    mySocket.send(no1.encode())
    mySocket.send(no2.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("BASHKETINGELLORE"):
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    textToSend=input()
    mySocket.send(textToSend.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("PRINTIMI"):
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    textToSend=input()
    mySocket.send(textToSend.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("EMRIIKOMPJUTERIT"):
    result=mySocket.recv(1024).decode()
    print((result))
elif clientInput_S==str("IPADRESA"):
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("NUMRIIPORTIT"):
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("KOHA"):
    result=mySocket.recv(128).decode()
    print(str('%.19s' % result))
elif clientInput_S==str("LOJA"):
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("FIBONACCI"):
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    no1=input()
    mySocket.send(no1.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))
elif clientInput_S==str("KONVERTO"):
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    optionselected=input()
    mySocket.send(optionselected.encode())
    msg=mySocket.recv(1024).decode()
    print(str(msg))
    valueforconversion=input()
    mySocket.send(valueforconversion.encode())
    result=mySocket.recv(1024).decode()
    print(str(result))

else:
    print("Nuk ekziston nje komande e tille")






