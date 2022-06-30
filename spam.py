from os import system as s
try:from colored import fore
except:s('pip install colored');from colored import fore
try:import AminoXZ
except:s('pip install AminoXZ');import AminoXZ
from threading import Thread
error_color = fore.RED
regular_color = fore.GREY_63  
successful_color = fore.GREEN
input_color = fore.ORANGE_3
s("cls")
client = AminoXZ.Client()
print(fore.MEDIUM_PURPLE_4,"""


░█████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░  ░██████╗██████╗░░█████╗░███╗░░░███╗
██╔══██╗████╗░████║██║████╗░██║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗░████║
███████║██╔████╔██║██║██╔██╗██║██║░░██║  ╚█████╗░██████╔╝███████║██╔████╔██║
██╔══██║██║╚██╔╝██║██║██║╚████║██║░░██║  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██║░░██║██║░╚═╝░██║██║██║░╚███║╚█████╔╝  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q
	Discord server: https://discord.gg/GtpUnsHHT4
	
""",regular_color)
def spam(comId, chatId, message, messageType):
	while True:
		client.send_message_web(chatId=chatId, comId=comId, message=message, messageType=messageType)

while True:
	try:client.login(email=input(f"{input_color}Email>> {regular_color}"), password=input(f"{input_color}Password>> {regular_color}")); print(successful_color,'Successful login.\n',regular_color);break
	except Exception as error:print(error_color, f'\nError:\n{error}\n', regular_color)

while True:
	url = input(f"{input_color}Link to chat>> {regular_color}")
	try:chat_info = client.get_from_link(url)['extensions']['linkInfo']; chatId=chat_info['objectId']; comId=chat_info['ndcId'];print(successful_color,"Successful retrieval of chat information.",regular_color);break
	except Exception as error:print(error_color, f'\nError:\n{error}\n', regular_color)

try:client.join_community(comId=comId); print(successful_color,"Successful join community.",regular_color)
except Exception as error:print(error_color, f'\nError join community:\n{error}\n', regular_color)

try:client.join_chat_web(chatId=chatId, comId=comId); print(successful_color,"Successful join chat.",regular_color)
except Exception as error:print(error_color, f'\nError join chat:\n{error}\n', regular_color)

message=input(f"{input_color}Spam message>> {regular_color}")
while True:
	mt = input("MessageType (0 or 109) >> ")
	if mt == '0':print(fore.GREEN, "\nOK.\n", fore.PURPLE_3); messageType = 0; break
	elif mt == '109':print(fore.GREEN, "\nOK.\n", fore.PURPLE_3); messageType = 109; break
	else: print("\nError type.\nRegular message - 0\nSystem message - 109\n")

while True:
	select = input(f"{input_color}Use antiban description (crash description) Y/N >> {regular_color}").lower()
	if select == 'y':client.change_profile(comId=comId, name='Free scripts -> @DXsarz | Бесплатные скрипты -> @DXsarz', content=open("antiban.txt", encoding='utf-8').read()); print(successful_color,'Profile changed successfully.\n',regular_color);break
	elif select == 'n':print('Ok, the profile has not been changed.\n'); break
	else: print(error_color, '\nGive the correct answer, Y or N.\n', regular_color)
print(successful_color,"\nStart spamming...",regular_color)
for i in range(10):Thread(target=spam, args=(comId, chatId, message, messageType)).start()
