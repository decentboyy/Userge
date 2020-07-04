# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.

#

# This file is part of < https://github.com/UsergeTeam/Userge > project,

# and is released under the "GNU v3.0 License Agreement".

# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >

#

# All rights reserved.

import os

from userge import userge, Message

@userge.on_cmd("ppg", about={

    'header': "use this to get any user details",

    'usage': "just reply to any user message or add user_id or username",

    'examples': "{tr}whois [user_id | username]"}, allow_channels=False)

async def who_is(message: Message):

    await message.edit("`Collecting Picture Of Rendi.. Hang on!`")

    user_id = message.input_str

    if user_id:

        try:

            from_user = await userge.get_users(user_id)

            from_chat = await userge.get_chat(user_id)

        except Exception:

            await message.err(

                "no valid user_id or message specified, do .help whois for more info")

            return

    elif message.reply_to_message:

        from_user = await userge.get_users(message.reply_to_message.from_user.id)

        from_chat = await userge.get_chat(message.reply_to_message.from_user.id)

    else:

        await message.err("no valid user_id or message specified, do .help whois for more info")

        return

    if from_user or from_chat is not None:

        pp_c = await userge.get_profile_photos_count(from_user.id)

        cc_no = len(await userge.get_common_chats(from_user.id))

        message_out_str = "<b>PROFILE PIC GRABBED</b>\n\n"

        if from_user.photo:

            local_user_photo = await userge.download_media(message=from_user.photo.big_file_id)

            await userge.send_photo(chat_id=message.chat.id,

                                    photo=local_user_photo,

                                    caption=message_out_str,

                                    parse_mode="html",

                                    disable_notification=True)

            os.remove(local_user_photo)

            await message.delete()

        else:

            message_out_str = "<b>📷 NO DP Found 📷</b>\n\n" + message_out_str

            await message.edit(message_out_str)
