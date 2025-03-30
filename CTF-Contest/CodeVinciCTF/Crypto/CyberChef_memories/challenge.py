#! /bin/python

import signal
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from os import urandom
from secret import NOTES

TIMEOUT = 300
BLOCK_SIZE = AES.block_size

# TODO: I need to find another way to save my passwords, but it's fine for now.
#       Well, I guess noone will ever have this file.
myPassword = '1234567890-A'

def banner():
    print('''                                                 *                                 
   (          )             (      )     (   (      (  `                                
   )\\ (    ( /(    (  (     )\\  ( /(   ( )\\ ))\\     )\\))(    (    )       (  (    (     
 (((_))\\ ) )\\())  ))\\ )(  (((_) )\\()) ))(()/((_|   ((_)()\\  ))\\  (     (  )( )\\  ))\\(   
 )\\__(()/(((_)\\  /((_|()\\ )\\___((_)\\ /((_)(_)) )\\  (_()((_)/((_) )\\  ' )\\(()((_)/((_)\\  
((/ __)(_)) |(_)(_))  ((_|(/ __| |(_|_))(_) _|((_) |  \\/  (_)) _((_)) ((_)((_|_|_))((_) 
 | (_| || | '_ \\/ -_)| '_|| (__| ' \\/ -_)|  _|(_-< | |\\/| / -_) '  \\() _ \\ '_| / -_|_-< 
  \\___\\_, |_.__/\\___||_|   \\___|_||_\\___||_|  /__/ |_|  |_\\___|_|_|_|\\___/_| |_\\___/__/ 
      |__/                                                                              
    ''')
    print('Welocome back chef CyberChef, what do you want to remember today?\n')

def menu() -> str:
    titles = [t for t in NOTES.keys()]
    print('Available notes:')
    print("0) Exit")
    for i, t in enumerate(titles): print(f'{i+1}) {t}')
    while True:
        try: choice = int(input('> '))
        except Exception:
            print('Something went wrong :(')
            exit(0)
        if choice == 0:
            print('Bye!')
            exit(0)
        elif 1 <= choice <= len(titles): return titles[choice-1]
        print("I'm afraid this note doesn't exist. Try again, please.")

def main():
    sessionSecret = urandom(BLOCK_SIZE)
    banner()
    while True:
        choice = menu()
        if choice == 'Flag':
            print('Warning, password protected note!!!')
            while True:
                try: password = bytes.fromhex(input('Please, enter the encrypted password (hex): '))
                except:
                    print("Error, the password has not been sent in hex.\nMaybe you're not the real CyberChef... stakko!")
                    exit(0)
                try: cipher = AES.new(key=sessionSecret, mode=AES.MODE_CBC, iv=password)
                except:
                    print("Error, the password doesn't have the correct lenght.\nMaybe you're not the real CyberChef... stakko!")
                    exit(0)
                try:
                    if unpad(cipher.decrypt(sessionSecret), BLOCK_SIZE) == myPassword.encode():
                        print('Succesully unlocked note.')
                        print('\n', NOTES['Flag'], '\n')
                        break
                    else: 
                        print('Wrong password, try again.')
                        continue
                except:
                    print("There are been issues decrypting the password, I guess it's the padding, try again.")
                    continue
        else: print('\n', NOTES[choice], '\n')

def handleTimeout(signum, frame):
    print('\nZzzzzz, Zzzzz, ...')
    exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handleTimeout)
    signal.alarm(TIMEOUT)
    main()
