from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤲 Namoz vaqtlarini bilish 🤲")
        ],
        [
            KeyboardButton(text="📜 Hadislar 📜")
        ],
        [
            KeyboardButton(text="🧭 Qibla 🧭")
        ]
    ],
    resize_keyboard=True
)
menushahar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔘 Toshkent 🔘"),
            KeyboardButton(text="🔘 Namangan 🔘"),
            KeyboardButton(text="🔘 Andijon 🔘")
        ],
        [
            KeyboardButton(text="🔘 Buxoro 🔘"),
            KeyboardButton(text="🔘 Farg'ona 🔘"),
            KeyboardButton(text="🔘 Samarqand 🔘")
        ],
        [
            KeyboardButton(text="🔘 Navoiy 🔘"),
            KeyboardButton(text="🔘 Nukus 🔘"),
            KeyboardButton(text="🔘 Qarshi 🔘")
        ],
        [
            KeyboardButton(text="Menu")
        ]
    ],
    resize_keyboard=True
)
