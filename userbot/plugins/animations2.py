import asyncio
from collections import deque

from userbot import *
from eaglebot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Eagle User"


@bot.on(admin_cmd(pattern=r"boxs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"boxs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`boxs...`")
    deq = deque(list("ð¥ð§ð¨ð©ð¦ðªð«â¬â¬"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"rain$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"rain$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Raining.......`")
    deq = deque(list("ð¬âï¸ð©ð¨ð§ð¦ð¥âð¤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"deploy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"deploy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "`Deploying...`")
    animation_chars = [
        "**Heroku Connecting To Latest [Github Build](KING-USER1/EAGLE_USERBOR)**",
        f"**Build started by user** {DEFAULTUSER}",
        f"**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m stdborg`",
        "**State changed from starting to up**",
        "__INFO:HÃªlláºÃ¸â :Logged in as 557667062__",
        "__INFO: EAGLEáºÃ¸â :Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"dump$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"dump$", allow_sudo=True))
async def _(message):
    if event.fwd_from:
        return
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "ð¥ ð ð«"
    event = await edit_or_reply(message, "`droping....`")
    u, t, g, o, s, n = inp.split(), "ð", "<(^_^ <)", "(> ^_^)>", "â  ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await event.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@bot.on(admin_cmd(pattern=r"fleaveme$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fleaveme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "â¬â¬â¬\nâ¬â¬â¬\nâ¬â¬â¬",
        "â¬â¬â¬\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸â¬\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬âï¸",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬ï¸âï¸",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâï¸â¬ï¸âï¸",
        "â¬â¬ï¸âï¸\nâ¬ï¸ðâ¡ï¸\nâï¸â¬ï¸âï¸",
        "âï¸â¬ï¸âï¸\nâ¬ï¸ðâ¡ï¸\nâï¸â¬ï¸âï¸",
    ]
    event = await edit_or_reply(event, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=r"loveu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"loveu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "loveu")
    animation_chars = [
        "ð",
        "ð©âð¨",
        "ð",
        "ð",
        "ð¤£",
        "ð",
        "ð",
        "ð",
        "ð",
        "âº",
        "ð",
        "ð¤",
        "ð¤¨",
        "ð",
        "ð",
        "ð¶",
        "ð£",
        "ð¥",
        "ð®",
        "ð¤",
        "ð¯",
        "ð´",
        "ð",
        "ð",
        "â¹",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð¢",
        "ð­",
        "ð¤¯",
        "ð",
        "â¤",
        "I Love Youâ¤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@bot.on(admin_cmd(pattern=r"plane$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"plane$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Wait for plane...")
    await event.edit("â-------------")
    await event.edit("-â------------")
    await event.edit("--â-----------")
    await event.edit("---â----------")
    await event.edit("----â---------")
    await event.edit("-----â--------")
    await event.edit("------â-------")
    await event.edit("-------â------")
    await event.edit("--------â-----")
    await event.edit("---------â----")
    await event.edit("----------â---")
    await event.edit("-----------â--")
    await event.edit("------------â-")
    await event.edit("-------------â")
    await asyncio.sleep(3)


@bot.on(admin_cmd(pattern=r"police$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"police$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Police")
    animation_chars = [
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
        
@bot.on(admin_cmd(pattern=f"hack$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(15)
    event = await edit_or_reply(event, "`Hacking this kid....`")
    animation_chars = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 0%\n[ââââââââââââââââââââ]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
            "Hacking... 11.07%\n[ââââââââââââââââââââ]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
            "Hacking... 20.63%\n[ââââââââââââââââââââ]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
            "Hacking... 34.42%\n[ââââââââââââââââââââ]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
            "Hacking... 42.17%\n[ââââââââââââââââââââ]\n`Searching for databases`\nETA: 0m, 12s",
            "Hacking... 55.30%\n[ââââââââââââââââââââ]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
            "Hacking... 64.86%\n[ââââââââââââââââââââ]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
            "Hacking... 74.02%\n[ââââââââââââââââââââ]\n`Trying to Decrypt...`\nETA: 0m, 06s",
            "Hacking... 86.21%\n[ââââââââââââââââââââ]\n`Trying to Decrypt...`\nETA: 0m, 04s",
            "Hacking... 93.50%\n[ââââââââââââââââââââ]\n`Decryption successful!`\nETA: 0m, 02s",
            "Hacking... 100%\n[ââââââââââââââââââââ]\n`Scanning file...`\nETA: 0m, 00s",
            "Hacking complete!\nUploading file...",
            "Targeted Account Hacked...!\n\n â File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])

@bot.on(admin_cmd(pattern=r"jio$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"jio$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(19)
    event = await edit_or_reply(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "*Optimising JIO NETWORK...*",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@bot.on(admin_cmd(pattern=r"solarsystem$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"solarsystem$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await edit_or_reply(event, "solarsystem")
    animation_chars = [
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nðâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nðâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸ðâ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸ââ¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸ðâ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ââ¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸ð\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nââ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nââ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸ð\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸ââ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸ðâ¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸ââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ðâ¼ï¸â¼ï¸â¼ï¸`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
        
        
@bot.on(admin_cmd(pattern="degi$"))
@bot.on(sudo_cmd(pattern="degi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "degi")
    await event.edit("WO")
    await asyncio.sleep(1.5)
    await event.edit("DegI")
    await asyncio.sleep(1.5)
    await event.edit("TuM")
    await asyncio.sleep(1.5)
    await event.edit("EkbaR")
    await asyncio.sleep(1.5)
    await event.edit("ManG")
    await asyncio.sleep(1.5)
    await event.edit("KaR")
    await asyncio.sleep(1.5)
    await event.edit("ToH")
    await asyncio.sleep(1.5)
    await event.edit("DekhO")
    await asyncio.sleep(1.5)
    await event.edit("Wo DeGi TuM eKbAr MaNg KaR tOh DeKhOð")


@bot.on(admin_cmd(pattern=f"nehi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"nehi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nehi")
    await event.edit(
        "`Wo PaKkA DeGi Tu ManG KaR ToH DekH\n AuR NaA De To UskI BheN Ko PakaDðð`"
    )
    await asyncio.sleep(999)


@bot.on(admin_cmd(pattern="hnd (.*)"))
@bot.on(sudo_cmd(pattern="hnd (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await edit_or_reply(event, "âï¸")
    animation_chars = [
        "ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿",
        "ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾",
        "ðð½ðð½ðð½ðð½ðð½ðð½ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½ðð½ðð½ðð½ðð½ðð½ðð½",
        "ðð¼ðð¼ðð¼ðð¼ðð¼\nðð¼              ðð¼\nðð¼              ðð¼\nðð¼              ðð¼\nðð¼ðð¼ðð¼ðð¼ðð¼",
        f"ðð»ðð»ðð»\n{name}\nðð»ðð»ðð»",
        f"ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿\nðð¿ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¿\nðð¿ðð¾ðð½ðð½ðð½ðð½ðð½ðð½ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð¼ðð¼ðð¼ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð»ðð»ðð»ðð¼ðð½ðð¾ðð¿\nðð¿  {name}  ðð¿\nðð¿ðð¾ðð½ðð¼ðð»ðð»ðð»ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð¼ðð¼ðð¼ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð½ðð½ðð½ðð½ðð½ðð½ðð¾ðð¿\nðð¿ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¿\nðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
        
        
CmdHelp("animations2").add_command(
  'boxs', None, 'Use and see'
).add_command(
  'rain', None, 'Use and see'
).add_command(
  'deploy', None, 'Use and see'
).add_command(
  'dump', None, 'Use and see'
).add_command(
  'fleaveme', None, 'Use and see'
).add_command(
  'loveu', None, 'Use and see'
).add_command(
  'plane', None, 'Use and see'
).add_command(
  'police', None, 'Use and see'
).add_command(
  'jio', None, 'Use and see'
).add_command(
  'solarsystem', None, 'Use and see'
).add_command(
  'degi', None, 'Use and see'
).add_command(
  'nehi', None, 'Use and see'
).add_command(
  'hack', None, 'Im a hacker bitch'
).add_command(
  'hnd', '<your text>', 'A handy animation with the text,'
).add_command(
  'owner', None, 'Use and see'
).add_command(
  'padmin', None, 'Prank promote a user'
).add()
