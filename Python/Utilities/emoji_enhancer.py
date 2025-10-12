Emoji_map = {
      "love": "❤️",
    "code": "👨‍💻",
    "tea": "🍵",
    "coffee": "☕",
    "happy": "😊",
    "sad": "😢",
    "food": "🍕",
    "book": "📚",
    "music": "🎶",
    "great": "🌟",
    "win": "🏆",
    "yes": "👍",
    "no": "👎",
    "sun": "☀️",
    "rain": "🌧️",
}

msg = input("Enter your message: ")

updated_words = []

for word in msg.split():
    no_caps = word.lower().strip(".,!?") 
    emoji = Emoji_map.get(no_caps,"")
    if emoji:
        updated_words.append(f"{word}{emoji}")
    else:
        updated_words.append(word)
            
updated_msg =" ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_msg)            
