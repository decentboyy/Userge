#By @PhycoNinja13b

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
import asyncio
import os
from userge import userge, Config, Message


thumb_image_path = Config.DOWN_PATH + "/thumb_image.jpg"


@userge.on_cmd("mnf", about={'header': "Lol"})
async def memify(message: Message):
    if not message.reply_to_message:
       await message.edit("**Bruh, Use correct Syntax**~ `.mnf 'text on top' ; 'text on bottom'`")
       return
    reply_message = message.reply_to_message
    if not reply_message.media:
       await message.edit("**Bruh** I can only memify sticker, gif and images. ")
       return

    file_ext_ns_ion = "@memetime.png"
    file = await userge.download_media(message=reply_message)
    uploaded_gif = None
    chat = "@MemeAutobot"
    await message.edit("Hhahaah... Memifying this... Wait Plox!! ")
    
    async with userge.conversation("MemeAutobot") as bot_conv:
          try:
            memeVar = message.input_str
            await silently_send_message(bot_conv, "/start")
            await asyncio.sleep(1)
            await silently_send_message(bot_conv, memeVar)
            await bot_conv.forward_message(reply_message)
            response = await bot_conv.get_response(mark_read=True)
          except YouBlockedUser: 
              await message.edit("**Please unblock @MemeAutobot and try again**")
              return
          if response.text.startswith("Forward"):
              await hmm.edit("```can you kindly disable your forward privacy settings for good nibba?```")
          if "Okay..." in response.text:
            await message.edit("Wait **Bruh** lemme convert this Non-Image nibba to an Image")
           
            thumb = None
            if os.path.exists(thumb_image_path):
                thumb = thumb_image_path
            input_str = message.input_str
            if not os.path.isdir(Config.DOWN_PATH):
                os.makedirs(Config.DOWN_PATH)
            if message.reply_to_message:
                file_name = "meme.png"
                reply_message = message.reply_to_message
                to_download_directory = Config.DOWN_PATH
                downloaded_file_name = os.path.join(to_download_directory, file_name)
                downloaded_file_name = await userge.download_media(
                    message=reply_message,
                    file_name=downloaded_file_name,
                    )
                if os.path.exists(downloaded_file_name):
                    await userge.send_photo(
                        chat_id=chat,
                        photo=downloaded_file_name
                        )
                    os.remove(downloaded_file_name)
                else:
                    await message.edit("File Not Found {}".format(input_str))
            response = await bot_conv.get_response(mark_read=True)
            the_download_directory = Config.DOWN_PATH
            files_name = "memes.webp"
            download_file_name = os.path.join(the_download_directory, files_name)
            await userge.download_media(
                message=response,
                file_name=download_file_name,
                )
            requires_file_name = Config.DOWN_PATH + "memes.webp"
            await userge.send_sticker(  # pylint:disable=E0602
                chat_id=message.chat.id,
                sticker=requires_file_name,
            )

          elif not reply_message.photo:
            await message.edit("Invalid message type. Plz choose right message type u NIBBA.")
            return

          else: 
            response = await bot_conv.get_response(mark_read=True)
            the_download_directory = Config.DOWN_PATH
            files_name = "memes.webp"
            download_file_name = os.path.join(the_download_directory, files_name)
            await userge.download_media(
                message=response,
                file_name=download_file_name,
                )
            requires_file_name = Config.DOWN_PATH + "memes.webp"
            await userge.send_sticker(  # pylint:disable=E0602
                chat_id=message.chat.id,
                sticker=requires_file_name,
            )
    await message.delete()
    
async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response(mark_read=True)
    return response