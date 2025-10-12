
# Basic version
"""
name = str(input("Enter your name: ")).capitalize()
age = int(input("Your age: "))
city = str(input("Your city: ")).capitalize()
profession = str(input("Your profession: ")).capitalize()
hobby = str(input("Your hobby:  ")).capitalize()

print(
    f"Hello My name is {name}. I'm {age} years old and i live in {city}.  I work as a {profession} and i absolutely enjoy {hobby} in my free time. Nice to meet you!"
)
"""

# little enhanced , when i thought of loops and list 

import datetime

ques = [
    "Enter your name: ",
    "Your age: ",
    "Your city: ",
    "Your profession: ",
    "Your hobby: "
]

answer = [] 

for questions in ques:
    ans = input(questions)
    answer.append(ans)

#print(answer) 

name = answer[0].capitalize().strip()
age = int(answer[1])
city = answer[2].capitalize().strip()
profession = answer[3].capitalize().strip()
hobby = answer[4].capitalize().strip()

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)