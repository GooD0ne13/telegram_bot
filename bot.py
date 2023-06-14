from telegram.ext import MessageHandler, Application, filters, CommandHandler

async def UAH(update, context):
    string_in = update.message.text
    if string_in == "/UAH":
       await update.message.reply_text("Щоб перевести гривні в інші валюти використай команду /UAH та через двокрапку впиши кількість гривень")
    else:
        info = string_in.split(':')
        USD = float(info[1]) / 36.94
        EUR = float(info[1]) / 39.78
        PLN = float(info[1]) / 8.95
        string_out = f"{USD} Доларів💰 \n{EUR} Євро💰 \n{PLN} Злотих💰"
        await update.message.reply_text(string_out)

async def PLN(update, context):
    string_in = update.message.text
    if string_in == "/PLN":
        await update.message.reply_text("Щоб перевести злоті в інші валюти використай команду /PLN та через двокрапку впиши кількість злотих")
    else:
        info = string_in.split(':')
        USD = float(info[1]) / 4.13
        EUR = float(info[1]) / 4.44
        UAH = float(info[1]) * 8.95
        string_out = f"{USD} Долар💰 \n{EUR} Євро💰 \n{UAH} Гривня💰"
        await update.message.reply_text(string_out)

async def USD(update, context):
    string_in = update.message.text
    if string_in == "/USD":
        await update.message.reply_text("Щоб перевести долари в інші валюти використай команду /USD та через двокрапку впиши кількість доларів")
    else:
        info = string_in.split(':')
        PLN = float(info[1]) * 4.13
        EUR = float(info[1]) / 1.1
        UAH = float(info[1]) * 36.94
        string_out = f"{PLN} Злоті💰 \n{EUR} Євро💰 \n{UAH} Гривня💰"
        await update.message.reply_text(string_out)

async def EUR(update, context):
    string_in = update.message.text
    if string_in == "/EUR":
        await update.message.reply_text("Щоб перевести євро в інші валюти використай команду /EUR та через двокрапку впиши кількість євро")
    else:
        info = string_in.split(':')
        PLN = float(info[1]) * 4.44
        USD = float(info[1]) * 1.1
        UAH = float(info[1]) * 39.78
        string_out = f"{PLN} Злоті💰 \n{USD} Долар💰 \n{UAH} Гривня💰"
        await update.message.reply_text(string_out)

async def echo(update, context):
    string_in = update.message.text
    if string_in == "/start":
        string_out = "Привіт, я бот який, може переводити гроші по нинішньому курсу💰.Для ознайомлення з командами нажми на /help"
    elif string_in == "/help":
        string_out = "Щоб поміняти гроші тобі потрібно натиснути на одну з команд /EUR (євро в гривні) /USD (долари в гривні) /PLN (злоті в гривні) /UAH (гривні в інші валюти)"
    elif string_in == "/RUB":
        string_out = "Я не хочу з тобою спілкуватися"
    else:
        string_out = "Вибач, але я не знаю цієї команди("
    await update.message.reply_text(string_out)

application = Application.builder().token("6092997901:AAGcBk3xANasOYyxUbeRJc-_nTl2CfgaYJs").build()
application.add_handler(CommandHandler("EUR", EUR))
application.add_handler(CommandHandler("USD", USD))
application.add_handler(CommandHandler("PLN", PLN))
application.add_handler(CommandHandler("UAH", UAH))
application.add_handler(MessageHandler(filters.TEXT, echo))
application.run_polling()