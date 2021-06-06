"""
 ██▓ ███▄ ▄███▓ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████ 
▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ 
▒██▒▓██    ▓██░▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   
░██░▒██    ▒██ ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒
░██░▒██▒   ░██▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒
░▓  ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░
 ▒ ░░  ░      ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░
 ▒ ░░      ░   ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  
 ░         ░                ░ ░     ░                    ░                                                             
"""
import os
import colorama
colorama.init()
from colorama import Fore,Back,Style
import hashlib
import ctypes
import sys
import subprocess
import pkg_resources
import time

"""
███▄ ▄███▓ ▄▄▄       ██▓ ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▓██▒ ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒░██░▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░
"""

#cmd configuration
os.system("cls")
os.system("mode con: cols=20000 lines=15000")
required = {'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))



#Drawing UI
def ui():
    print(Fore.GREEN+'''
---------------------------------------------------------------
---------------------------------------------------------------'''+Fore.RED+'''

██████╗  ██████╗ ███████╗███████╗██╗██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║
██████╔╝██║   ██║███████╗█████╗  ██║██║  ██║██║   ██║██╔██╗ ██║
██╔═══╝ ██║   ██║╚════██║██╔══╝  ██║██║  ██║██║   ██║██║╚██╗██║
██║     ╚██████╔╝███████║███████╗██║██████╔╝╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝'''+Fore.GREEN+'''
                                                               
---------------------------------------------------------------                                                         
----------------------------------------------------------------                                                                
        ''')
ui()
print(Fore.RED+"")

#Author info
def info():
    print(Fore.RED+"Author/Senior DEV :"+" "+Fore.CYAN+"H2O")
    print(" ")
    print(Fore.GREEN+"------------------------------------")
    print(" ")
    print(Fore.RED+"junior DEV        :"+" "+Fore.CYAN+"Jessica Miles")
    print(" ")
    print(Fore.GREEN+"------------------------------------")
    print(" ")
    print(Fore.RED+"Description       :"+" "+Fore.CYAN+"Coming soon")
    print(" ")
    print(Fore.GREEN+"------------------------------------")
    print(" ")
    print(Fore.RED+"Version           :"+" "+Fore.CYAN+"1.0.0")
#options provided
def choose():
        print('''
        (1)Poseidon'''+Fore.GREEN+'''
        ______________________'''+Fore.RED+'''

        (2)About the author'''+Fore.GREEN+'''

        ______________________
        ''')
choose()
print(Fore.RED+" ")
#Residual functions to be declared


def soon():
    print("soon")

#Poseidon Main function

def Poseidon():
    print(Fore.RED+'''        1)Cryptography''')
    print(Fore.GREEN +"        --------------")
    print(Fore.RED+'''        2)String-cracker''')
    print(Fore.GREEN +"        --------------")
    print(Fore.RED+'''        3)EXPL0ITS''')
    b = False
    try:
        while b is False:
            input2  = input("=>")
            if input2 == "1":
                print(" ")
                print(" ")
                Cryptography()
                b=True
            elif input2 == "2":
                print(" ")
                print(" ")
                string_cracker()
                b=True
            elif input2 =="3":
                print(" ")
                print(" ")
                Exploit()
            else:
                print("Please Enter a valid choice!")
    except Exception as e:
        print(f'Error{e}')
def Exploit():
    time.sleep(1)
    print(Fore.CYAN+"This list will include Exploits that i found and exploited")
    print(" ")
    print(" ")
    time.sleep(2)
    print("It will also include the methods to exploit each of em")
    print(" ")
    print(" ")
    time.sleep(2)
    print("However i'm keeping this private as of now")
    print(" ")
    print(" ")
    time.sleep(2)
    print("lemme know if you're interested")
    print(" ")
    print(" ")
def Cryptography():
    print(Fore.GREEN+"1)md5")
    print(" ")
    print(" ")
    print(Fore.GREEN+"2)sha224")
    print(" ")
    print(" ")
    print(Fore.GREEN+"3)sha256")
    print(" ")
    print(" ")
    print(Fore.GREEN+"4)sha384")
    print(" ")
    print(" ")
    print(Fore.GREEN+"5)sha512")
    print(" ")
    print(" ")
    print(Fore.GREEN+"6)back")

    try:
        while True:
            print(Fore.RED+"")
            input3 = input("=>")
            if input3 == "1":
                input4 = input("Enter your string to convert:")
                print(" ")
                print(" ")
                encoded_input4 = input4.encode('utf-8')
                digest1 = hashlib.md5(encoded_input4.strip()).hexdigest()
                print(" ")
                print(" ")
                print("Your md5 hash is:"+Fore.GREEN+digest1)
            elif input3 == "2":
                input4 = input("Enter your string to convert:")
                print(" ")
                print(" ")
                encoded_input4 = input4.encode('utf-8')
                digest1 = hashlib.sha224(encoded_input4.strip()).hexdigest()
                print(" ")
                print(" ")
                print("Your sha224 hash is:"+Fore.GREEN+digest1)
            elif input3 == "3":
                input4 = input("Enter your string to convert:")
                print(" ")
                print(" ")
                encoded_input4 = input4.encode('utf-8')
                digest1 = hashlib.sha256(encoded_input4.strip()).hexdigest()
                print(" ")
                print(" ")
                print("Your sha256 hash is:"+Fore.GREEN+digest1)
            elif input3 == "4":
                input4 = input("Enter your string to convert:")
                print(" ")
                print(" ")
                encoded_input4 = input4.encode('utf-8')
                digest1 = hashlib.sha384(encoded_input4.strip()).hexdigest()
                print(" ")
                print(" ")
                print("Your sha384 hash is:"+Fore.GREEN+digest1)
            elif input3 == "5":
                input4 = input("Enter your string to convert:")
                print(" ")
                print(" ")
                encoded_input4 = input4.encode('utf-8')
                digest1 = hashlib.sha512(encoded_input4.strip()).hexdigest()
                print(" ")
                print(" ")
                print("Your sha512 hash is:"+Fore.GREEN+digest1)
            elif input3 =="6":
                os.system("cls")
                ui()
                Poseidon()
            else:
                print("Please Enter a valid choice!")
            
    except Exception as e:
        print(f'Error{e}')

#cracker# 

def string_cracker():
    print(Fore.GREEN+"1)md5")
    print(" ")
    print(" ")
    print(Fore.GREEN+"2)sha224")
    print(" ")
    print(" ")
    print(Fore.GREEN+"3)sha256")
    print(" ")
    print(" ")
    print(Fore.GREEN+"4)sha384")
    print(" ")
    print(" ")
    print(Fore.GREEN+"5)sha512")
    print(" ")
    print(" ")
    print(Fore.GREEN+"6)back")
    
    try:
        print(Fore.RED+"")
        while True:
            crack = input("=>")
            if crack =="1":
                crack_hash = input("Enter the hash string : ")
                print(" ")
                print(" ")
                crack_file = input("Enter the file name (Wordlist must be on the same directory as this program)   : ")
                crack_openfile = open(crack_file,"r")

                for words in crack_openfile:
                    encoded_word = words.encode('utf-8')
                    hash_word = hashlib.md5(encoded_word.strip()).hexdigest()
                    if hash_word == crack_hash:
                        print("The required password should be:"+Fore.GREEN+words )
                        ui()
                        pass_cracker()
                        break
                    else:
                        print(hash_word)
                        print("Password Not found,yet")
            elif crack =="2":
                crack_hash = input("Enter the hash string : ")
                print(" ")
                print(" ")
                crack_file = input("Enter the file name (Wordlist must be on the same directory as this program)   : ")
                crack_openfile = open(crack_file,"r")

                for words in crack_openfile:
                    encoded_word = words.encode('utf-8')
                    hash_word = hashlib.sha224(encoded_word.strip()).hexdigest()
                    if hash_word == crack_hash:
                        print("The required password should be:"+Fore.GREEN+words )
                        ui()
                        pass_cracker()
                        break
                    else:
                        print(hash_word)
                        print("Password Not found,yet")
            elif crack == "3":
                crack_hash = input("Enter the hash string : ")
                print(" ")
                print(" ")
                crack_file = input("Enter the file name (Wordlist must be on the same directory as this program)   : ")
                crack_openfile = open(crack_file,"r")

                for words in crack_openfile:
                    encoded_word = words.encode('utf-8')
                    hash_word = hashlib.sha256(encoded_word.strip()).hexdigest()
                    if hash_word == crack_hash:
                        print("The required password should be:"+Fore.GREEN+words )
                        ui()
                        pass_cracker()
                        break
                    else:
                        print(hash_word)
                        print("Password Not found,yet")
            elif crack == "4":
                crack_hash = input("Enter the hash string : ")
                print(" ")
                print(" ")
                crack_file = input("Enter the file name (Wordlist must be on the same directory as this program)   : ")
                crack_openfile = open(crack_file,"r")

                for words in crack_openfile:
                    encoded_word = words.encode('utf-8')
                    hash_word = hashlib.sha384(encoded_word.strip()).hexdigest()
                    if hash_word == crack_hash:
                        print("The required password should be:"+Fore.GREEN+words )
                        ui()
                        pass_cracker()
                        break
                    else:
                        print(hash_word)
                        print("Password Not found,yet")
            elif crack =="5":
                crack_hash = input("Enter the hash string : ")
                print(" ")
                print(" ")
                crack_file = input("Enter the file name (Wordlist must be on the same directory as this program)   : ")
                crack_openfile = open(crack_file,"r")

                for words in crack_openfile:
                    encoded_word = words.encode('utf-8')
                    hash_word = hashlib.sha512(encoded_word.strip()).hexdigest()
                    if hash_word == crack_hash:
                        print("The required password should be:"+Fore.GREEN+words )
                        ui()
                        pass_cracker()
                        break
                    else:
                        print(hash_word)
                        print("Password Not found,yet")
            elif crack == "6":
                os.system("cls")
                ui()
                Poseidon()
            else:
                print("Please Enter a valid choice : ")

    except Exception as e:
        print(f'Error{e}')   
        
#Choosing options(start)

a = False

try:
    while a is False:
        decision = input( "Enter your choice =>"+" ")
        if decision == "1":
            def func_obhriqjs():
                return print
            func_obhriqjs()(" ")
            def func_ksxxcnaj():
                return print
            func_ksxxcnaj()(" ")
            Poseidon()
            a = True
        elif decision == "2":
            def func_eqdmrarx():
                return " "
            print(func_eqdmrarx())
            def func_yxrfrihl():
                return print
            func_yxrfrihl()(" ")
            info()
        else:
            print("Please Enter a valid choice!")
except Exception as e:
    print(f'Error{e}')

    


