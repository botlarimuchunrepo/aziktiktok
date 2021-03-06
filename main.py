from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)
import requests
import os
import logging


# ◇─────────────────────────────────────────────────────────────────────────────────────◇


# TikTok Downloader API
API = 'https://single-developers.up.railway.app/tiktok?url='

# Your BOT Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# TikTok Video URL Types , You Can Add More to This :)
TikTok_Link_Types= ['https://m.tiktok.com','https://vm.tiktok.com','https://vt.tiktok.com','https://tiktok.com','https://www.tiktok.com']

# ParseMode Type For All Messages
_ParseMode=ParseMode.MARKDOWN

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def start_handler(update, context):
    update.message.reply_text('Salom! Men TikTokdan yuklovchi botman 🤖!\n\nSiz mendan foydalanib TikTokdan video yoki audio yuklab olishingiz mumkin!!! \n\n@azik_projects - 𝚃𝚘 𝚝𝚑𝚎 𝚏𝚞𝚝𝚞𝚛𝚎 𝚠𝚒𝚝𝚑 𝚞𝚜🦾')

def about_handler(update, context):
#    update.message.reply_sticker('CAACAgUAAxkBAAED9kZiDq_LFrib38c7DYu3jNz3ebsolgACJAUAAuTb4FdKtjtZGQ2ukiME')
    update.message.reply_text('[🦾 AziK ProJecTs](https://t.me/azik_projects)\n\n[🔥 Dasturchi </>🇺🇿 ](https://t.me/azik_developer)',parse_mode=_ParseMode)
    
# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Download Task
def Download_Video(Link,update, context):
    message=update.message
    req=None
    no_watermark=None
    watermark=None

    status_msg=message.reply_text('🚀 Serverimga yuklab olinmoqda ....')
#    status_sticker=message.reply_sticker('CAACAgUAAxkBAAED9jhiDqYeGjENlCjftByz0au6n4YAASEAAnUEAALpa8lXL9cvxeTK-2AjBA')

    # Getting Download Links Using API
    try:
       req=requests.get(API+Link).json()
       no_watermark=req['no_watermark']
       watermark= req['watermark']
       print('Yuklab olish havolalarini yaratish \n\n\n'+str(req)+'\n\n\n')
    except:
        print('Yuklab olish havolalarida xatolik !!!')
        status_msg.edit_text('⁉️ TikTok Downloader API xatosi !!! Dasturchiga xabar bering: @azik_developer')
        status_sticker.delete()
        return
    
    caption_text="""
@azik_tiktokbot orqali yuklangan {} video.
 """
    
    # Uploading Downloaded Videos to Telegram
    print('Uploading Videos')
    status_msg.edit_text('☘️ Telegramga yuklanmoqda....')
    message.reply_video(video=no_watermark,supports_streaming=True,caption=caption_text.format('Suv belgisiz'),parse_mode=_ParseMode)
#    message.reply_video(video=watermark,supports_streaming=True,caption=caption_text.format('Suv belgi bilan'),parse_mode=_ParseMode)

    # Task Done ! So, Deleteing Status Messages
    status_msg.delete()
#    status_sticker.delete()

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def incoming_message_action(update, context):
    message=update.message
    if any(word in str(message.text) for word in TikTok_Link_Types):
        context.dispatcher.run_async(Download_Video,str(message.text),update,context)

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

def main() -> None:
    """Run the bot."""
  
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher


    # Commands Listning
    dispatcher.add_handler(CommandHandler('start', start_handler, run_async=True))
    dispatcher.add_handler(CommandHandler('about', about_handler, run_async=True))

    # Message Incoming Action
    dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action,run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() # 😁 Start

# ◇─────────────────────────────────────────────────────────────────────────────────────◇

# Example For https://github.com/Single-Developers/API/blob/main/tiktok/Note.md

# https://t.me/SL_Developers
# https://t.me/SingleDevelopers

# ◇─────────────────────────────────────────────────────────────────────────────────────◇
#✅ Muvaffaqqiyatli yuklab olindi {} video 🔰

#👻 Ishlab chiqilgan:[🦾 AziK ProJecTs](https://t.me/azik_projects)tomonidan!🔰
#[🔥 Dasturchi </> ](https://t.me/azik_developer)
