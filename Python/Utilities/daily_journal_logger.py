import datetime

entry = input("What have u learned today: ").strip()
rating = input("Rate your productivity today (1-5) , oprional").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n {date_str}\n{entry}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
journal_entry += "\n" + "-" * 50

with open("learning_journal.txt" , "a" , encoding = "utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has been saved to 'learning_journal.txt' file ")
