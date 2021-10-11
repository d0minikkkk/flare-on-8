import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
filepath = r'/root/Desktop/empty'

with open('dungeondescription_array.txt','r') as f:
    data = f.read()

arr = data.split('\n')

count = 0
class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(":", 1)[0]
        print(a)
        # print(a)
        # print(e.source.nick)
        # if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(
        #     self.connection.get_nickname()
        # ):
        #     self.do_command(e, a[1].strip())
        if 'Hello' in a:
            c.privmsg("#dungeon", f'{e.source.nick}, what is your quest?')
        elif 'My quest is' in a:
            cmd = f'{e.source.nick}, welcome to the party.'
            c.privmsg('#dungeon', cmd)
            with open('water.potion','r') as f2:
                potion = f2.read()
            cmd = f'{e.source.nick}, {potion}'
            num = len(cmd) // 480
            start = 0
            for i in range(num):
                c.privmsg('#dungeon', cmd[start:start+480])
                start += 480
            c.privmsg('#dungeon', cmd[start:])
        elif 'brew the Potion of Water' in a:
            cmd = f'{e.source.nick}, you enter the dungeon The Sunken Crypt. It is '
            for i,v in enumerate(filepath):
                index = ord(v)
                word = arr[index]
                if i == len(filepath) - 1:
                    cmd += f'and {word}.'
                else:
                    cmd += f'{word}, '

            print(cmd)
            c.privmsg('#dungeon', cmd)

        elif 'draw my sword' in a:
            cmd = f'{e.source.nick}, you encounter a Wyvern in the distance. It stares at you imposingly. The beast sits in the water, waiting for you to approach it. What do you do?'
            print(cmd)
            c.privmsg('#dungeon', cmd)
        else:
            pass
        return

    def on_dccmsg(self, c, e):
        # non-chat DCC messages are raw bytes; decode as text
        text = e.arguments[0].decode('utf-8')
        print(text)
        c.privmsg("You said: " + text)

    def on_dccchat(self, c, e):
        if len(e.arguments) != 2:
            return
        args = e.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        if cmd == "disconnect":
            self.disconnect()
        elif cmd == "die":
            self.die()
        elif cmd == "stats":
            for chname, chobj in self.channels.items():
                c.notice(nick, "--- Channel statistics ---")
                c.notice(nick, "Channel: " + chname)
                users = sorted(chobj.users())
                c.notice(nick, "Users: " + ", ".join(users))
                opers = sorted(chobj.opers())
                c.notice(nick, "Opers: " + ", ".join(opers))
                voiced = sorted(chobj.voiced())
                c.notice(nick, "Voiced: " + ", ".join(voiced))
        elif cmd == "dcc":
            dcc = self.dcc_listen()
            c.ctcp(
                "DCC",
                nick,
                "CHAT chat %s %d"
                % (ip_quad_to_numstr(dcc.localaddress), dcc.localport),
            )
        else:
            c.notice(nick, "Not understood: " + cmd)


def main():
    import sys

    if len(sys.argv) != 4:
        print("Usage: testbot <server[:port]> <channel> <nickname>")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    bot = TestBot(channel, nickname, server, port)
    bot.start()


if __name__ == "__main__":
    main()