#pip install [requests, bs4, shutil, nekos.py, sqlite3, colorama, tqdm]
import requests, shutil, bs4, time, string, re, os, sys, nekos, sqlite3
from colorama import Fore, init
from bs4 import BeautifulSoup
from tqdm import tqdm
# Ejemplo de URL que da la API: 'https://cdn.nekos.life/lewd/lewd_neko488.jpeg'

init()

print(Fore.GREEN + '\n ###################################################')
print(Fore.GREEN + ' #                                                 #')
print(Fore.GREEN + ' #                   Created by:                   #')
print(Fore.GREEN + ' #                   '+Fore.LIGHTGREEN_EX+'Nekoraru22'+Fore.GREEN+'                    #')
print(Fore.GREEN + ' #                                                 #')
print(Fore.GREEN + ' #              Discord: Neko-san#4592             #')
print(Fore.GREEN + ' #                                                 #')
print(Fore.GREEN + ' ###################################################' + Fore.RESET + '\n')

# ------------------------------------ Lists -------------------------------------- #
mylist = ['tickle', 'classic', 'ngif', 'erofeet', 'erok', 'poke', 'les', 'hololewd', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo'] # Api nekos.life
mylist2 = ['neko', 'futa', 'kawaii', 'lewd', 'slave', 'pat', 'monster'] # Api lolis.life
mylist.sort()
# ------------------------------------ /Lists -------------------------------------- #

# ------------------------------------ Create folders -------------------------------------- #
os.makedirs('Downloader/nekos_life/Guest', mode=0o777, exist_ok=True)

def lewdfolder():
    for names in mylist:
        os.makedirs('Downloader/nekos_life/' + names, mode=0o777, exist_ok=True)
    
    for names in mylist2:
        os.makedirs('Downloader/lolis_life/' + names, mode=0o777, exist_ok=True)

    print(Fore.LIGHTGREEN_EX + '[-] Folders created succesfully' + Fore.RESET)
# ------------------------------------ /Create folders -------------------------------------- #

# ------------------------------------ Word Remove -------------------------------------- #
def remove_char(string):
    string = list(string)
    string.remove('/')
    return ''.join(string)
# ------------------------------------ /Word Remove -------------------------------------- #

# -------- Rute ----------- #
rute = 'Downloader/'
# -------- /Rute ----------- #

# ------------------------------------ Loop as lewd mode -------------------------------------- #
def download():
    global tag, rute, foldername, link, apianswer
    
    if apianswer == '1':
        link = nekos.img(tag)

    elif apianswer == '2':

        if tag == "random":
            r = requests.get("https://api.lolis.life/random")
            link = BeautifulSoup(r.content,"html.parser")
            link = re.sub(r"[^a-zA-Z0-9/.:\"]"," ",str(link))
            link = re.search(r"url\":\"([a-zA-Z0-9-_./:]+)", link)
            link = link.group(1)

        else:
            r = requests.get("https://api.lolis.life/" + tag)
            link = BeautifulSoup(r.content,"html.parser")
            link = re.sub(r"[^a-zA-Z0-9/.:\"]"," ",str(link))
            link = re.search(r"url\":\"([a-zA-Z0-9-_./:]+)", link)
            link = link.group(1)
    
    print(Fore.LIGHTMAGENTA_EX + "URL Image: " + Fore.LIGHTCYAN_EX + link + Fore.RESET)

    if apianswer == '1':
        image_name = re.search(r"life/(.+[a-zA-Z0-9-_])", link)
        image_name = image_name.group(1)
        image_name = remove_char(image_name)
    elif apianswer == '2':
        image_name = re.search(r"life/([a-zA-Z0-9-_.]+)", link)
        image_name = image_name.group(1)

    print (Fore.LIGHTMAGENTA_EX + 'Image name: ' + Fore.LIGHTCYAN_EX + image_name + Fore.RESET)

    resp = requests.get(link, stream=True)
    try:
        # Dowload image file
        local_file = open(rute + foldername + '/' + image_name, 'xb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        # Animation
        for i in tqdm(range(100), unit=" bits", desc= "Getting File"):
            print('', end='\r')
    except:
        errors()
# ------------------------------------ /Loop as lewd mode -------------------------------------- #

# ------------------------------------ Loop as guest mode -------------------------------------- #
def download2():
    global tag, rute, foldername
    link = nekos.cat()
    print(Fore.LIGHTMAGENTA_EX + "URL Image: " + Fore.LIGHTCYAN_EX + link + Fore.RESET)

    image_name = re.search(r"life/(.+[a-zA-Z0-9-_])", link)
    image_name = image_name.group(1)
    image_name = remove_char(image_name)
    print (Fore.LIGHTMAGENTA_EX + 'Image name: ' + Fore.LIGHTCYAN_EX + image_name + Fore.RESET)

    resp = requests.get(link, stream=True)
    try:
        # Dowload image file
        local_file = open(rute + foldername + '/' + image_name, 'xb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        # Animation
        for i in tqdm(range(100), unit=" bits", desc= "Getting File"):
            print('', end='\r')
    except:
        errors()
# ------------------------------------ /Loop as guest mode -------------------------------------- #

# ------------------------------------ Nekos.Life -------------------------------------- #
def nekoslife():
    global link, tag, foldername
    while True:
        print(Fore.BLUE + '# --------------------------------------- #' + Fore.RESET)
        for elem in mylist:
            print('[·] '+ Fore.LIGHTBLACK_EX + elem + Fore.RESET)
        print(Fore.BLUE + '# --------------------------------------- #\n' + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + '\n[-] Select tag of image library' +Fore.CYAN + ' (Enter = predeterminate(neko)): ' + Fore.RESET)
        tag = input('\n==> ')
        foldername = 'nekos_life/' + tag
            
        if tag in mylist:
            link = nekos.img(tag)
            break
        elif tag == "":
            link = nekos.img('neko')
            tag = 'neko'
            foldername = 'nekos_life/neko'
            break
        else:
            print(Fore.LIGHTRED_EX +'[-] The tag not exists. Select another: ' + Fore.RESET)
            time.sleep(2)
# ------------------------------------ /Nekos.Life -------------------------------------- #

# ------------------------------------ Lolis.Life -------------------------------------- #
def lolislife():
    global link, tag, foldername
    while True:
        print(Fore.BLUE + '# --------------------------------------- #' + Fore.RESET)
        for elem in mylist2:
            print('[·] '+ Fore.LIGHTBLACK_EX + elem + Fore.RESET)
        print(Fore.BLUE + '# --------------------------------------- #\n' + Fore.RESET)
        print(Fore.LIGHTCYAN_EX + '\n[-] Select tag of image library' + Fore.CYAN + ' (Enter = predeterminate(random)): ' + Fore.RESET)
        tag = input('\n==> ')
        foldername = 'lolis_life/' + tag
            
        if tag in mylist2:
            r = requests.get("https://api.lolis.life/" + tag)
            link = BeautifulSoup(r.content,"html.parser")
            link = re.sub(r"[^a-zA-Z0-9/.:\"]"," ",str(link))
            link = re.search(r"url\":\"([a-zA-Z0-9-_./:]+)", link)
            link = link.group(1)
            break
        elif tag == "":
            os.makedirs('Downloader/lolis_life/random', mode=0o777, exist_ok=True)

            r = requests.get("https://api.lolis.life/random")
            link = BeautifulSoup(r.content,"html.parser")
            link = re.sub(r"[^a-zA-Z0-9/.:\"]"," ",str(link))
            link = re.search(r"url\":\"([a-zA-Z0-9-_./:]+)", link)
            link = link.group(1)

            tag = 'random'
            foldername = 'lolis_life/random'
            break
        else:
            print(Fore.LIGHTRED_EX +'[-] The tag not exists. Select another: ' + Fore.RESET)
            time.sleep(2)
# ------------------------------------ /Lolis.Life -------------------------------------- #

# --------- Errors --------- #
n = 0
def errors():
  global n
  global number
  n = n + 1
  print(Fore.LIGHTRED_EX + '\n REPEATED\n' + Fore.RESET)
# --------- /Errors --------- #

while True:
    print(Fore.LIGHTCYAN_EX + '[-] Enter a password for' + Fore.LIGHTMAGENTA_EX +' lewd mode ' + Fore.LIGHTCYAN_EX + 'or press "Enter" to enter as a' + Fore.LIGHTYELLOW_EX + ' Guest' + Fore.RESET)
    passwd = input('\n==> ')

    if passwd == 'meow':
        print(Fore.LIGHTGREEN_EX + '[-] Password correct!!')
        time.sleep(0.5)
        lewdfolder()

        print(Fore.LIGHTCYAN_EX + "\n[-] what API do you want to use?" + Fore.LIGHTWHITE_EX + "\n   1) Nekos.life\n   2) Lolis.life")
        apianswer = input('\n==> ')
        print(Fore.LIGHTYELLOW_EX + '[-] Loading List...\n' + Fore.RESET)
        time.sleep(0.5)

        if apianswer == '1':
            nekoslife()
            break
        elif apianswer == '2':
            lolislife()
            break
        else:
            print("That's not an option")

    elif passwd == "":
        apianswer = "1"
        link = nekos.cat()
        print(Fore.LIGHTGREEN_EX + 'Logged as a Guest' + Fore.RESET)
        tag = 'Guest'
        foldername = 'nekos_life/' + tag
        break
        
    else:
        print(Fore.LIGHTRED_EX + '[-] Error... Retrying...' + Fore.RESET)
        time.sleep(2)

number = int(input('\nEnter the number of files to download ==> '))

print(Fore.BLUE + '\n# --- ' + '1' + ' --- #' + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "URL Image: " + Fore.LIGHTCYAN_EX + link + Fore.RESET)

# Name of image.
if apianswer == '1':
    image_name = re.search(r"life/(.+[a-zA-Z0-9-_])", link)
    image_name = image_name.group(1)
    image_name = remove_char(image_name)
elif apianswer == '2':
    image_name = re.search(r"life/([a-zA-Z0-9-_.]+)", link)
    image_name = image_name.group(1)


print (Fore.LIGHTMAGENTA_EX + 'Image name: ' + Fore.LIGHTCYAN_EX + image_name + Fore.RESET)

# Open the url image, set stream to True, this will return the stream content.
resp = requests.get(link, stream=True)

# Copy the response stream raw data to local image file.
try:
    # Open a local file with wb ( write binary ) permission.
    local_file = open(rute + foldername + '/' + image_name, 'xb')
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    # Remove the image url response object.
    del resp
    # Dowload image file
    for i in tqdm(range(100), unit=" bits", desc= "Getting File"):
        print('', end='\r')
except:
    errors()

# ------------------------------------ Repeat -------------------------------------- #
def repeat():
    b = 1
    global number
    if passwd == 'meow': 
        for ejecucion in range(number - 1):
            b = b + 1
            print(Fore.BLUE + '# --- ' + str(b) + ' --- #' + Fore.RESET)
            download()
    elif passwd == "":
        for ejecucion in range(number - 1):
            b = b + 1
            print(Fore.BLUE + '# --- ' + str(b) + ' --- #' + Fore.RESET)
            download2()
repeat()
# ------------------------------------ /Repeat -------------------------------------- #

# Close script
systemrute = os.getcwd()
systemrute = systemrute.replace("\\", "/")
total = number - n
print(Fore.LIGHTGREEN_EX + "\n" + str(total) + ' files downloaded succesfully at "' + systemrute + '/' + rute + foldername + '\"' + Fore.RESET)
print(Fore.LIGHTRED_EX + 'Files repeated: ' + Fore.LIGHTRED_EX + str(n) + Fore.RESET )
close = input('\nPress enter to close...')
print(Fore.LIGHTYELLOW_EX + 'Closing...' + Fore.RESET)
time.sleep(0.5)
