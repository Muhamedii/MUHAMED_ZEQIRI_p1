
import socket
from _thread import *
import threading
import datetime
import random


def Main():
    print("Shenoni te dhenat e serverit me te cilin deshironi te lidheni")

    serverIP = input("\nIP e serverit: ")
    serverIP_S = str(serverIP)

    serverPORT = input("PORT-i i serverit: ")
    serverPORT_S = str(serverPORT)

    serverIP_B = serverIP_S.encode()
    serverPORT_I = int(serverPORT)




    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((serverIP_B, serverPORT_I))


    print("U ARRIT LIDHJA ME SERVERIN.NE PRITJE PER KERKESA...")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        "\nMiresevini i/e nderuar.\nPer te vazhduar ju lutem perdorni njeren nga metodat e deshiruara duke shkruar ate me shkronja te medha!\n"
        "\nIPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, KONVERTO, FIBONACCI, SHUMA, SHUMABIN, CAP, SHUMEZUESIMEIVOGELIPERBASHKET(SHMVP)\n------------------------------------------------------------------------------------------------------------------------------------------------ ")


    while True:

        clientInput = input("Kerkesa juaj: ");
        clientInput_S = str(clientInput)

        mySocket.send(clientInput_S.encode())
        if clientInput_S == str("CAP"):
            msg = mySocket.recv(128).decode()
            print(str(msg))
            string = input()
            mySocket.send(string.encode())
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "SHUMA" or clientInput_S=="SHUMABIN":
            msg = mySocket.recv(128).decode()
            print(str(msg))
            no1 = input()
            no2 = input()
            mySocket.send(no1.encode())
            mySocket.send(no2.encode())
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "BASHKETINGELLORE":
            msg = mySocket.recv(128).decode()
            print(str(msg))
            textToSend = input()
            mySocket.send(textToSend.encode())
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "PRINTIMI":
            msg = mySocket.recv(128).decode()
            print(str(msg))
            textToSend = input()
            mySocket.send(textToSend.encode())
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "EMRIIKOMPJUTERIT":
            result = mySocket.recv(128).decode()
            print((result))
        elif clientInput_S == "IPADRESA":
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "NUMRIIPORTIT":
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "KOHA":
            result = mySocket.recv(128).decode()
            print(str('%.19s' % result))
        elif clientInput_S == "LOJA":
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "FIBONACCI":
            msg = mySocket.recv(128).decode()
            print(str(msg))
            no1 = input()
            mySocket.send(no1.encode())
            result = mySocket.recv(128).decode()
            print(str(result))
        elif clientInput_S == "KONVERTO":
            msg = mySocket.recv(1024).decode()
            print(str(msg))
            optionselected = input()
            mySocket.send(optionselected.encode())
            msg = mySocket.recv(1024).decode()
            print(str(msg))
            valueforconversion = input()
            mySocket.send(valueforconversion.encode())
            result = mySocket.recv(1024).decode()
            print(str(result))
        elif clientInput_S=="SHMVP":
            msg = mySocket.recv(128).decode()
            print(str(msg))
            no1 = input()
            no2 = input()
            mySocket.send(no1.encode())
            mySocket.send(no2.encode())
            result = mySocket.recv(128).decode()
            print(str(result))


        msg = input('\nA deshironi ti pararshtroni kerkesa tjera serverit. Shtyp "JO" per te nderprere lidhjen: ')
        if msg == 'JO':
            print("Ju zgjodhet te shkeputni lidhjen me serverin.")

            break
        else:

            continue

    mySocket.close()


if __name__ == '__main__':
    Main()