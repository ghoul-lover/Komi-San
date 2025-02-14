from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama.plugins.stats import col
from nksama.plugins.stats import users_db , grps
from nksama import help_message



@bot.on_message(filters.command('start') | filters.command('start@KomiSanRobot'))
def start(_,message):
    try:
        if message.chat.type == "private":
            users = col.find({})
            mfs = []
            for x in users:
                mfs.append(x['user_id'])
            if message.from_user.id not in mfs:
                user = {"type": "user" , "user_id": message.from_user.id}
                col.insert_one(user)
                
        else:
            users = grps.find({})
            mfs = []
            for x in users:
                mfs.append(x['chat_id'])
            if message.chat.id not in mfs:
                grp = {"type": "group" , "chat_id": message.chat.id}
                grps.insert_one(grp)
            
    except Exception as e:
        bot.send_message(-1001646296281  , f"error in adding stats:\n\n{e}")
        
   
    
    if message.chat.type == "private" and not "help" in message.text:

        bot.send_message(message.chat.id , "Hello there i'm [mikey](https://telegra.ph/file/c47701281dd74a8107475.jpg)\nI'll help you to manage your groups" , reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton('help' , callback_data="help")]
        ]))
    if "help" in message.text:
     bot.send_message(message.chat.id , "Help" , reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton('help' , callback_data="help")]
     ]))
    if not message.chat.type == "private":
         message.reply("Hello there i'm komi san")
