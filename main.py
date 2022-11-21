from aiogram import executor
import requests
from aiogram.types import Message, CallbackQuery
from config import *
from Inline import *
from ReplyKeyboard import *
from random import choice as choose
from hadislar import hadis


async def menu(msg: Message):
    await msg.answer(text="Menyuga qaytdingiz", reply_markup=menuStart)


@dp.message_handler(commands="start")
async def start(msg: Message):
    txt = f"Assalomu alaykum {msg.from_user.full_name}. Namoz vaqtlari botga xush kelibsiz!"
    await msg.answer_photo(open("Image/start.jpg", "rb"), caption=txt, reply_markup=menuStart)
    await msg.delete()


@dp.message_handler(text="Menu")
@dp.message_handler(commands="help")
async def help1(msg: Message):
    txt = f"Yordam uchun https://t.me/Hello_this_isAbdurrohman profiliga bog'laning."
    await msg.answer_photo(open("Image/help.jpg", "rb"), caption=txt, reply_markup=menuStart)
    await msg.delete()


@dp.message_handler(text="🤲 Namoz vaqtlarini bilish 🤲")
async def namoz(msg: Message):
    await msg.answer_photo(open("Image/shaxar.jpg", "rb"), caption="Shaxarni tanlang!", reply_markup=menushahar)
    await msg.delete()


@dp.message_handler(text="📜 Hadislar 📜")
async def namoz(msg: Message):
    await msg.answer(text=choose(hadis), parse_mode="HTML")
    

@dp.message_handler(text="🧭 Qibla 🧭")
async def qibla(msg: Message):
    await bot.send_location(msg.chat.id, latitude=21.422524, longitude=39.826187)


@dp.message_handler(text="🔘 Toshkent 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/tash1.jpg", "rb"), "Tanlang!", reply_markup=menuTosh)


@dp.message_handler(text="🔘 Namangan 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/namangan.jpg", "rb"), "Tanlang!", reply_markup=menuNam)


@dp.message_handler(text="🔘 Andijon 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/andijon.jpg", "rb"), "Tanlang!", reply_markup=menuAnd)


@dp.message_handler(text="🔘 Buxoro 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang!", reply_markup=menuBux)


@dp.message_handler(text="🔘 Farg'ona 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuFarg)


@dp.message_handler(text="🔘 Xiva 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuXiva)


@dp.message_handler(text="🔘 Guliston 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuGul)


@dp.message_handler(text="🔘 Samarqand 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuSam)


@dp.message_handler(text="🔘 Navoiy 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuNav)


@dp.message_handler(text="🔘 Jizzax 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuJizzakh)


@dp.message_handler(text="🔘 Nukus 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuNuk)


@dp.message_handler(text="🔘 Qarshi 🔘")
async def tosh(msg: Message):
    await msg.answer_photo(open("Image/bukhara.jpg", "rb"), "Tanlang", reply_markup=menuQar)


@dp.callback_query_handler(text_contains="b1")
async def namoz(call: CallbackQuery):
    await call.message.answer_photo(open("Image/shaxar.jpg", "rb"), caption="Shaxarni tanlang!",
                                    reply_markup=menushahar)
    await call.message.delete()


@dp.callback_query_handler(text_contains="menu")
async def start(call: CallbackQuery):
    txt = f"Assalomu alaykum. Namoz vaqtlari botga xush kelibsiz!"
    await call.message.answer_photo(open("Image/start.jpg", "rb"), caption=txt, reply_markup=menuStart)
    await call.message.delete()


@dp.callback_query_handler(text_contains="t1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="t2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="n1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="n2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="a1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="a2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="f1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="f2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="b2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="b3")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="s1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="s2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="m1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="m2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="o1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="o2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="q1")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/prayer.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/qarshi").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


@dp.callback_query_handler(text_contains="q2")
async def bugun(call: CallbackQuery):
    await call.answer(cache_time=60)
    p = open("Image/erta.jpg", "rb")
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/qarshi").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await bot.send_photo(call.message.chat.id, p,
                         caption=f"🕔 Bomdod:     {bomdod} \n"
                                 f"☀ Quyosh:      {quyosh_ch}\n"
                                 f"🕐 Peshin:        {peshin}\n"
                                 f"🕞 Asr:              {asr}\n"
                                 f"🕕 Shom:         {shom}\n"
                                 f"🕢 Xufton:       {xufton}")


if __name__ == '__main__':
    executor.start_polling(dp)
