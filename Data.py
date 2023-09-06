from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدء استـخراج الجلسـة 🖥️", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝗿𝘂𝗻𝘁𝗵𝗼𝗻 - سـورس رنثـون 🌐", url="https://t.me/xLxLxLrr"
            )
        ],
        [
            InlineKeyboardButton("كيفيـة الاستـخدام   ⍰ ", callback_data="help"),
            InlineKeyboardButton("حـول البـوت ℹ️", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/F_P_l")],
    ]

    START = """
**مرحبـًا 🙋** {}
━━━━━━━━━━━━━━━━━━
**- فـي البـوت الرسمـي التابـع لـ 𝗯𝗲𝘁𝗵𝗼𝗻** ⚙️🤖
**- يمكـنك اسـتخـراج جلسـة تيرمكـس وبايروجـرام لتنـصيب سـورس بيثون
━━━━━━━━━━━━━━━━━━
**- قـم بالضغـط علـى بـدء استخـراج الجـلسـة ** 🛂
━━━━━━━━━━━━━━━━━━
**- ملاحظـات هامـة ** : -
**لا تقـم بطـرد الجلسـة التي اسمهـا Bit 64 لأنـك إذا طردتـها سيتوقـف تنصيبـك** 🚮
**احـذر مشاركـة الكود لأي شخـص لأنه يستطـيع اخـتراق حسابـك ** ⚠️
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/repo - لعرض معلومـات عـن السـورس 💡
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

**هـذا البوت تـم تشـغيله بواسطـة 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 و المـطور بيثون1**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗯𝗲𝘁𝗵𝗼𝗻](https://t.me/Bethon2)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @F_P_l
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس بيثون - 𝗯𝗲𝘁𝗵𝗼𝗻 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس رنثـون - 𝗿𝘂𝗻𝘁𝗵𝗼𝗻 . [اضـغط هـنا ❗](https://t.me/Bethon2)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/F_P_l)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/Bethon2)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗯𝗲𝘁𝗵𝗼𝗻 🌐**
   """
