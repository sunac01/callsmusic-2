# Calls Music 2 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
         f"""Ben **{bn}** !!
Grubunuzun sesli sohbetinde müzik çalabilirim 🔮
Şu anda desteklediğim komutlar şunlardır:
🦎 /play - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
🦎 /pause - __Sesli Sohbet Müziğini Duraklat.__
🦎 /resume - __Sesli Sohbet Müziğine Devam Et.__
🦎 /skip - __Sesli Sohbette Çalan Geçerli Müziği Atlar.__
🦎 /stop - __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sahibi 📬", url="https://t.me/Azerbesk"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url="https://t.me/kaybedenlerorkestrasi"
                    ),
                ],
            ],
        ),
    )
