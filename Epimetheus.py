import email
import imaplib
import base64
import time
import discord
#imports
r=0
import os
import time
from datetime import datetime
import asyncio
import datetime as dt
from discord.ext import commands, tasks
intents = discord.Intents(members =True,messages=True, guilds=True)

TOKEN = ('OTA4NTA1MzAwOTgwNjA5MDY0.YY2tfg.S8-oAUAC456KsJ5M9pA-SWoaJdM')
GUILD = ('771776651503075398')
client = discord.Client()
bot = commands.Bot(command_prefix='$')#Sets prefix for commands(!Command)



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "epimetheus.lrd" + ORG_EMAIL
FROM_PWD    = "p5z1WE1uf*JM"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


#@tasks.loop(minutes=1)
#async def send():
#  read_email_from_gmail()
#  f1 = open("some_output_file.txt", "r") 
#  text = f1.read()
#
#
#
#@send.before_loop
#async def before():
#    await bot.wait_until_ready()
#
#send.start()
@bot.command()
async def task(ctx):
    while 1==1:
        read_email_from_gmail()
        f1 = open("some_output_file.txt", "r") 
        text = f1.read()
        textlines=f1.readline()
        if not text:
          print("Debig code 2")
        else:
            await ctx.channel.send(text)
            print("Debug code 3")
        time.sleep(60)          
        print("Debug code 4")
        ou = open("some_output_file.txt", "w").close()  







@bot.command(pass_context=True)
async def checkupdates(ctx):
  read_email_from_gmail()
  f1 = open("some_output_file.txt", "r") 
  text = f1.read()
  await ctx.channel.send(text)

def read_email_from_gmail():
  EMAIL = 'epimetheus.lrd@mail.com'
  PASSWORD = 'p5z1WE1uf*JM'
  SERVER = 'imap.gmail.com'
  mail = imaplib.IMAP4_SSL(SMTP_SERVER)
  mail.login(FROM_EMAIL,FROM_PWD)
  mail.select('inbox')
  status, data = mail.search(None, 'ALL')
  mail_ids = []
  for block in data:
      mail_ids += block.split()

  for i in mail_ids:
      status, data = mail.fetch(i, '(RFC822)')
      for response_part in data:
          if isinstance(response_part, tuple):
              message = email.message_from_bytes(response_part  [1])
              mail_from = message['from']
              mail_subject = message['subject']
              if message.is_multipart():
                  mail_content = ''

                  for part in message.get_payload():
                      if part.get_content_type() ==   'text/plain':
                          mail_content += part.get_payload()
              else:
                  mail_content = message.get_payload()
              print(f'From: {mail_from}')
              f1 = open("test.txt", "a") 
              f1.write(f'Subject: {mail_subject}\n')      
              f2 = open("test2.txt", "r")    
              f1.close
              f1 = open("test.txt", "r")                     

              same = set(f1).difference(f2)


              
              
              with open('some_output_file.txt', 'a') as  file_out:
                  for line in same:
                      file_out.write(line)
                      print(same)
              f2 = open("test2.txt", "a")  
              f2.write(f'Subject: {mail_subject}\n')          




bot.run(TOKEN)



#with open('some_file_1.txt', 'r') as file1:
#    with open('some_file_2.txt', 'r') as file2:
#        same = set(file1).intersection(file2)
#
#same.discard('\n')
#
#with open('some_output_file.txt', 'w') as file_out:
#    for line in same:
#        file_out.write(line)
#
#while True:
#    read_email_from_gmail()
#    time.sleep(6)
#  f1 = open("test.txt", "r")  
#  f2 = open("test2.txt", "r")  
#  i = 0
#
#  for line1 in f1:
#      i += 1
#
#      for line2 in f2:
#
#          # matching line1 from both files
#          if line1 == line2:  
#              # print IDENTICAL if similar
#              print("Line ", i, ": IDENTICAL")
#
#          else:
#              # else print that line from both files
#              print("\tFile 1:", line1, end='')
#              print("\tFile 2:", line2, end='')              
#          break
#
#
#