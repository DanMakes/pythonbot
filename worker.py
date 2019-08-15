from datetime import datetime
import time
import bot


def worker():
    bot_obj = bot.Bot("#random")
    while True:

        date_today = datetime.now().timetuple()

        print(f"{date_today.tm_hour, date_today.tm_min} Making a new check cause it's a 15 mins interval")
        # Check for Friday show and tell
        if (date_today.tm_wday, date_today.tm_hour, date_today.tm_min) == (4, 16, 0):
            bot_obj.remind_show_and_tell()
        elif (date_today.tm_wday, date_today.tm_hour, date_today.tm_min) == (0, 9, 0):
            bot_obj.remind_monday_meeting()
        elif date_today.tm_wday in range(0, 5) and (date_today.tm_hour, date_today.tm_min) == (9, 30):
            bot_obj.remind_stand_up()
        elif date_today.tm_wday in range(0, 5) and date_today.tm_hour in (11, 12):
            bot_obj.remind_break(date_today.tm_min, date_today.tm_hour)
        elif date_today.tm_wday in range(0, 5) and (date_today.tm_hour, date_today.tm_min) == (13, 15):
            bot_obj.post_tip()

        # Making sure the interval is 15 mins but sleep all weekend
        if date_today.tm_wday == 4 and date_today.tm_hour == 18:
            sleep_time = 194400
        elif date_today.tm_min == 0 or (15 % date_today.tm_min == 0 and date_today.tm_min > 1):
            sleep_time = 15 * 60
        else:
            sleep_time = (15 - (date_today.tm_min % 15)) * 60

        time.sleep(sleep_time)


worker()

