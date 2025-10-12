user_info = [
    "Name :  ",
    "Profession : ",
    "Passoion and goals :  ",
    "Emoji(optional) :  ",
    "webiste or handle(optional):  "
]

user_input = []

for i in user_info:
    ans = input(i)
    user_input.append(ans)

print(user_input)    

name = user_input[0].capitalize().strip()
profession = user_input[1].capitalize().strip()
passion_goals = user_input[2].capitalize().strip()
fav_emoji = user_input[3].capitalize().strip()
web_handle = user_input[4].capitalize().strip()

bio_info = (

)