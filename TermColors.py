import os, re, sys, termios, tty

class TermColors:
    prefix = ''
    suffix = ''

    # tmux and screen require a DCS sequence before sending commands:
    if os.environ['TERM'][:6] == 'screen':
        if 'TMUX' in os.environ:
            prefix = '\x1bPtmux;\x1b'
        else:
            prefix = '\x1bP'

        suffix = '\x1b\\'

    ttyname = os.ttyname(0)
    fd = open(ttyname, 'r+')

    def write(self, string):
        self.fd.write(self.prefix + string + self.suffix)

    def get(self, color):
        oldsettings = termios.tcgetattr(self.fd)
        tty.setraw(self.fd, termios.TCSANOW)

        self.write("\033]4;" + str(color) + ";?\a")

        response = ""
        char = ""
        while char != '\a':
            response += char
            char = self.fd.read(1)
            if char == "":
                break

        r = re.compile(r'rgb:(..).*/(..).*/(..).*')

        termios.tcsetattr(self.fd, termios.TCSADRAIN, oldsettings)

        return r.findall(response)[0]

    def set(self, color, rgb):
        self.write("\033]4;" + str(color) + ";rgb:" +
                rgb[0] + "/" + rgb[1] + "/" + rgb[2] + "\a")

    def close(self):
        self.fd.close()
