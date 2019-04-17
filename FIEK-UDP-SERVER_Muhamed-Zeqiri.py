import socket
import datetime
import random

host = "127.0.0.1"
port = 12000
mySocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mySocket.bind((host, port))





class MetodatServerit:
    def Shuma(self,x,y):
        z = x + y
        return z

    def ShumaENrBinar(self,x,y):
        z=x+y
        rezultati=bin(z)[2:]
        return rezultati

    def NrBashketingelloreve(self,fjalia):
        nrzanoreve = 0
        fjalia_L = fjalia.replace(" ","").lower()
        for char in fjalia_L:
            if char in 'aeiouy':
                nrzanoreve += 1
        return (len(fjalia_L) - nrzanoreve)

    def Printimi(self,teksti):
        tekstiPaHapesira = teksti.strip()
        return tekstiPaHapesira


    def GjeneratoriINumrave(self):
        varguiNumrave=[]
        gjatesiavargut=7
        for i in range(gjatesiavargut):
            numri=random.randint(7,49)
            varguiNumrave.append(numri)
        return varguiNumrave

    def Fibonacci(self,n):
        a = 0
        b = 1
        if n < 0:
            x="Duhet numer i plote pozitiv!"
            return x
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2, n):
                c = a + b
                a = b
                b = c
            return b

    def KilovatneKuajfuqi(self,vlerakilovat):
        vlerakuajfuqi = vlerakilovat * 1.34102
        return round(vlerakuajfuqi,2)
    def KuajfuqineKilovat(self,vlerakuajfuqi):
        vlerakilovat=vlerakuajfuqi/1.34102
        return round(vlerakilovat,2)

    def ShkalleneRadian(self,vlerashkalle):
        vleraradian=vlerashkalle*(3.14/180)
        return round(vleraradian,3)
    def RadianneShkalle(self,vleraradian):
        vlerashkalle=vleraradian*(180/3.14)
        return round(vlerashkalle,3)

    def GallonneLitra(self,vleragallon):
        vleraliter=vleragallon* 3.785412
        return round(vleraliter,2)
    def LitraneGallon(self,vleraliter):
        vleragallon=vleraliter/3.785412
        return round(vleragallon,2)






obj=MetodatServerit()


udpspecial = mySocket.recvfrom(128)
inputFromClient=udpspecial[0]
ipExtracted=inputFromClient[1]
print(ipExtracted)


inputFromClient_S=str(inputFromClient).strip("b'")

if inputFromClient_S==str("CAP"):
    conn.send("Ju lutem shkruani nje fjali".encode())
    s1Recv=conn.recv(1024).decode()
    s1Recv_S=str(s1Recv.upper())
    conn.send(s1Recv_S.encode())
elif inputFromClient_S==str("SHUMA"):
    conn.send("Ju lutem shtypni dy numra".encode())
    no1=conn.recv(1024).decode()
    no2=conn.recv(1024).decode()
    no1_I=int(no1,2)
    no2_I=int(no2,2)

    tosend=str(obj.ShumaENrBinar(no1_I,no2_I))
    conn.send(tosend.encode())
elif inputFromClient_S==str("BASHKETINGELLORE"):
    conn.send("Ju lutem shkruani ca tekst".encode())
    text = conn.recv(1024).decode()
    text_S=str(text)
    tosend=str("Teksti i pranuar permban {} bashketingellore".format(obj.NrBashketingelloreve(text_S)))
    conn.send(tosend.encode())
elif inputFromClient_S==str("PRINTIMI"):
    conn.send("Ju lutem shkruani dicka".encode())
    text=conn.recv(1024).decode()
    text_S=str(text)
    tosend=str(obj.Printimi(text_S))
    conn.send(tosend.encode())
elif inputFromClient_S==str("EMRIIKOMPJUTERIT"):
    tosend=str(socket.gethostname())
    conn.send(tosend.encode())
elif inputFromClient_S==str("IPADRESA"):
    tosend="IP adresa juaj eshte: "+str(ipExtracted)
    mySocket.sendto(tosend.encode(),udpspecial[1])
elif inputFromClient_S==str("NUMRIIPORTIT"):
    tosend="Ju jeni lidhur ne portin: "+str(addr[1])
    conn.send(tosend.encode())
elif inputFromClient_S==str("KOHA"):
    currentServerTime=str(datetime.datetime.now())
    currentServerTime_S=str(currentServerTime)
    mySocket.sendto(currentServerTime_S.encode(),udpspecial[1])   #Mmenyra e dergimit dallon nga udp ngase nuk ka ne udp connection per kete qellim per shkaqe testimi praktik te dallimit
                                                                   #metodat tjera nuk i kam lene me koneksion e ne fakt duhet te dergohen me objektin e soketes.



elif inputFromClient_S==str("LOJA"):
    tosend=str(obj.GjeneratoriINumrave())
    conn.send(tosend.encode())
elif inputFromClient_S==str("FIBONACCI"):
    conn.send("Shtypni numrin per te cilen deshironi te llogaritni sekuencen e Fibonacci-t".encode())
    text=conn.recv(1024).decode()
    text_I=int(text)+1
    tosend=str(obj.Fibonacci(text_I))
    conn.send(tosend.encode())
elif inputFromClient_S==str("KONVERTO"):
    conn.send("Zgjedh sipas numrit njeren nga opsionet: \n\n1.KilowattToHorsepower\n2.HorsepowerToKilowatt\n3.DegreesToRadians\n4.RadiansToDegrees\n5.GallonsToLiters\n6.LitersToGallons ".encode())
    clientOption=conn.recv(1024).decode()
    msg=conn.send("Ju lutem shtypni nje vlere per te konvertuar".encode())
    valuetoconvert=conn.recv(1024).decode()
    if clientOption=="1":
       valuetoconvert_F=float(valuetoconvert)
       tosend=str(obj.KilovatneKuajfuqi(valuetoconvert_F))+"hp"
       conn.send(tosend.encode())
    elif clientOption=="2":
        valuetoconvert_F=float(valuetoconvert)
        tosend=str(obj.KuajfuqineKilovat(valuetoconvert_F))+"kW"
        conn.send(tosend.encode())
    elif clientOption=="3":
        valuetoconvert_F=float(valuetoconvert)
        tosend=str(obj.ShkalleneRadian(valuetoconvert_F))+"rad"
        conn.send(tosend.encode())
    elif clientOption=="4":
        valuetoconvert_F=float(valuetoconvert)
        tosend=str(obj.RadianneShkalle(valuetoconvert_F))+"°"
        conn.send(tosend.encode())
    elif clientOption=="5":
        valuetoconvert_F=float(valuetoconvert)
        tosend=str(obj.GallonneLitra(valuetoconvert_F))+"L"
        conn.send(tosend.encode())
    elif clientOption=="6":
        valuetoconvert_F=float(valuetoconvert)
        tosend=str(obj.LitraneGallon(valuetoconvert_F))+"gal"
        conn.send(tosend.encode())



else:
    print("Nuk ekziston nje komande e tille")

