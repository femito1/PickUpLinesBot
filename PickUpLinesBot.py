from telepot import Bot

messages = ["your pick up lines here"]

import random
import time
import schedule

# Your bot token from BotFather
TOKEN = 'Your Token Here'
bot = Bot(token=TOKEN)
chat_id = 'CHAT ID'  # Replace with the chat ID you want to send messages to

def send_random_message():
    """Selects a random message from the list and sends it to the user."""
    message = messages.pop()
    bot.send_message(chat_id=chat_id, text=message)


def schedule_random_time():
    """Schedules send_random_message to run at a random time every day."""
    # Generate a random time in HH:MM format
    random_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
    schedule.clear()  # Clear existing schedule
    schedule.every().day.at("17:08").do(send_random_message)
    print(f"Message scheduled for {random_time}")


def main():
    # Initial scheduling
    schedule_random_time()

    # Reschedule at midnight to pick a new random time for the next day
    schedule.every().day.at("00:00").do(schedule_random_time)

    # Keep the bot running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

