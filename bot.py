from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from profile import profil  # Pastikan modul profile ada dan berisi fungsi profil
from hotspot import ttl  # Pastikan modul hotspot ada dan berisi fungsi ttl
from hotspot_user import hUser
from hotspot_profile import hProfile
from hotspot_active import hActive
from hotspot_host import host
from hotspot_cookie import hCookie
from ppp_profile import profil_ppp
from ppp_user import user_ppp
from ppp_active import active_ppp

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Bot command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo master!")

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    await update.message.reply_text(f"Chat ID mu adalah : {user_id}")

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = profil()  # Call the function from profile module
    await update.message.reply_text(info_message)

async def hotspot_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = ttl()  # Call the function from hotspot module
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot status information is not available.")
    
async def hotspot_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = hUser()  # Call the function from hotspot module
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def hotspot_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = hProfile()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def hotspot_active(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = hActive()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def hotspot_host(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = host()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def hotspot_cookie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = hCookie()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def hotspot_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = "Hotspot report data is not implemented yet."  # Replace with actual function
    await update.message.reply_text(info_message)

async def ppp_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = profil_ppp()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def ppp_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = user_ppp()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def ppp_active(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = active_ppp()
    if info_message:  # Check if message is not empty or None
        await update.message.reply_text(info_message)
    else:
        await update.message.reply_text("Hotspot information is not available.")

async def ppp_host(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = "PPP host data is not implemented yet."  # Replace with actual function
    await update.message.reply_text(info_message)

async def ppp_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = "PPP report data is not implemented yet."  # Replace with actual function
    await update.message.reply_text(info_message)

# Bot command handler for /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif dan siap menerima perintah!")

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Maaf saya tidak mengerti, mohon berikan perintah yang benar.")

def main():
    # Create the bot application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("chat_id", chat_id))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CommandHandler("hotspot_status", hotspot_status))
    application.add_handler(CommandHandler("hotspot_user", hotspot_user))  # Uncomment if implemented
    application.add_handler(CommandHandler("hotspot_profile", hotspot_profile))  # Uncomment if implemented
    application.add_handler(CommandHandler("hotspot_active", hotspot_active))  # Uncomment if implemented
    application.add_handler(CommandHandler("hotspot_host", hotspot_host))  # Uncomment if implemented
    application.add_handler(CommandHandler("hotspot_cookie", hotspot_cookie))  # Uncomment if implemented
    application.add_handler(CommandHandler("hotspot_report", hotspot_report))  # Uncomment if implemented
    application.add_handler(CommandHandler("ppp_profile", ppp_profile))  # Uncomment if implemented
    application.add_handler(CommandHandler("ppp_user", ppp_user))  # Uncomment if implemented
    application.add_handler(CommandHandler("ppp_active", ppp_active))  # Uncomment if implemented
    application.add_handler(CommandHandler("ppp_host", ppp_host))  # Uncomment if implemented
    application.add_handler(CommandHandler("ppp_report", ppp_report))  # Uncomment if implemented
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # Print a message to the console indicating the bot is running
    print("Bot is running...")

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()

#start - Mulai
#status - Menampilkan status bot
#chat_id - Mengambil data chat id
#profile - Menampilkan ama ISP dan Informasi sistem mikrotik
#hotspot_status - Menampilkan jumlah hotspot tersedia dan aktif
#hotspot_user - Menampilkan daftar pengguna hotspot
#hotspot_profile - Menampilkan profil hotspot
#hotspot_active - Menampilkan pengguna hotspot aktif
#hotspot_host - Menampilkan host hotspot
#hotspot_cookie - Menampilkan cookie pengguna
#ppp_profile - Menampilkan profil PPPoE
#ppp_user - Menampilkan daftar pengguna PPPoE
#ppp_active - Menampilkan PPPoE Aktif
