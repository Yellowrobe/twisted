
import string

from twisted.internet import protocol, defer, interfaces as iinternet
from twisted.python import components

class ITerminalProtocol(components.Interface):
    def makeConnection(self, transport):
        """Called with an ITerminalTransport when a connection is established.
        """

    def keystrokeReceived(self, keyID):
        """A keystroke was received.

        Each keystroke corresponds to one invocation of this method.
        keyID is a string identifier for that key.  Printable characters
        are represented by themselves.  Control keys, such as arrows and
        function keys, are represented with symbolic constants on
        C{ServerProtocol}.
        """

    def terminalSize(self, width, height):
        """Called to indicate the size of the terminal.

        A terminal of 80x24 should be assumed if this method is not
        called.  This method may not be called for real terminals.
        """

    def setMode(self, modes):
        pass

    def resetMode(self, modes):
        pass

    def unhandledControlSequence(self, seq):
        """Called when an unsupported control sequence is received.
        """

    def connectionLost(self, reason):
        pass

class TerminalProtocol(object):
    __implements__ = (ITerminalProtocol,)

    def makeConnection(self, transport):
        self.transport = transport
        self.connectionMade()

    def connectionMade(self):
        """Called after a connection has been established.
        """

    def keystrokeReceived(self, keyID):
        pass

    def terminalSize(self, width, height):
        pass

    def setMode(self, modes):
        pass

    def resetModes(self, modes):
        pass

    def unhandledControlSequence(self, seq):
        pass

    def connectionLost(self, reason):
        pass

class ITerminalTransport(iinternet.ITransport):
    def cursorUp(self, n=1):
        """Move the cursor up n lines.
        """

    def cursorDown(self, n=1):
        """Move the cursor down n lines.
        """

    def cursorForward(self, n=1):
        """Move the cursor right n columns.
        """

    def cursorBackward(self, n=1):
        """Move the cursor left n columns.
        """

    def cursorPosition(self, column, line):
        """Move the cursor to the given line and column.
        """

    def cursorHome(self):
        """Move the cursor home.
        """

    def index(self):
        """Move the cursor down one line, performing scrolling if necessary.
        """

    def reverseIndex(self):
        """Move the cursor up one line, performing scrolling if necessary.
        """

    def nextLine(self):
        """Move the cursor to the first position on the next line, performing scrolling if necessary.
        """

    def saveCursor(self):
        """Save the cursor position, character attribute, character set, and origin mode selection.
        """

    def restoreCursor(self):
        """Restore the previously saved cursor position, character attribute, character set, and origin mode selection.

        If no cursor state was previously saved, move the cursor to the home position.
        """

    def setMode(self, modes):
        """Set the given modes on the terminal.
        """

    def resetMode(self, mode):
        """Reset the given modes on the terminal.
        """

    def applicationKeypadMode(self):
        """Cause keypad to generate control functions.

        Cursor key mode selects the type of characters generated by cursor keys.
        """

    def numericKeypadMode(self):
        """Cause keypad to generate normal characters.
        """

    def selectCharacterSet(self, charSet, which):
        """Select a character set.

        charSet should be one of CS_US, CS_UK, CS_DRAWING, CS_ALTERNATE, or
        CS_ALTERNATE_SPECIAL.

        which should be one of G0 or G1.
        """

    def singleShift2(self):
        """Shift to the G2 character set for a single character.
        """

    def singleShift3(self):
        """Shift to the G3 character set for a single character.
        """

    def selectGraphicRendition(self, *attributes):
        """Enabled one or more character attributes.

        Arguments should be one or more of UNDERLINE, REVERSE_VIDEO, BLINK, or BOLD.
        NORMAL may also be specified to disable all character attributes.
        """

    def horizontalTabulationSet(self):
        """Set a tab stop at the current cursor position.
        """

    def tabulationClear(self):
        """Clear the tab stop at the current cursor position.
        """

    def tabulationClearAll(self):
        """Clear all tab stops.
        """

    def doubleHeightLine(self, top=True):
        """Make the current line the top or bottom half of a double-height, double-width line.

        If top is True, the current line is the top half.  Otherwise, it is the bottom half.
        """

    def singleWidthLine(self):
        """Make the current line a single-width, single-height line.
        """

    def doubleWidthLine(self):
        """Make the current line a double-width line.
        """

    def eraseToLineEnd(self):
        """Erase from the cursor to the end of line, including cursor position.
        """

    def eraseToLineBeginning(self):
        """Erase from the cursor to the beginning of the line, including the cursor position.
        """

    def eraseLine(self):
        """Erase the entire cursor line.
        """

    def eraseToDisplayEnd(self):
        """Erase from the cursor to the end of the display, including the cursor position.
        """

    def eraseToDisplayBeginning(self):
        """Erase from the cursor to the beginning of the display, including the cursor position.
        """

    def eraseDisplay(self):
        """Erase the entire display.
        """

    def deleteCharacter(self, n=1):
        """Delete n characters starting at the cursor position.

        Characters to the right of deleted characters are shifted to the left.
        """

    def insertLine(self, n=1):
        """Insert n lines at the cursor position.

        Lines below the cursor are shifted down.  Lines moved past the bottom margin are lost.
        This command is ignored when the cursor is outside the scroll region.
        """

    def deleteLine(self, n=1):
        """Delete n lines starting at the cursor position.

        Lines below the cursor are shifted up.  This command is ignored when the cursor is outside
        the scroll region.
        """

    def reportCursorPosition(self):
        """Return a Deferred that fires with a two-tuple of (x, y) indicating the cursor position.
        """

    def reset(self):
        """Reset the terminal to its initial state.
        """

CSI = '\x1b'
CST = {'H': 'H',
       'f': 'f',
       'A': 'A',
       'B': 'B',
       'C': 'C',
       'D': 'D',
       's': 's',
       'u': 'u',
       'J': 'J',
       'K': 'K',
       'm': 'm',
       'h': 'h',
       'l': 'l',
       'p': 'p',
       'R': 'R',
       '~': 'tilde'}

# These are nominally public
# XXX - Put them in a namespace or something

# ANSI-Specified Modes
KEYBOARD_ACTION = KAM = 2
INSERTION_REPLACEMENT = IRM = 4
LINEFEED_NEWLINE = LNM = 20

# ANSI-Compatible Private Modes
ERROR = 0
CURSOR_KEY = 1
ANSI_VT52 = 2
COLUMN = 3
SCROLL = 4
SCREEN = 5
ORIGIN = 6
AUTO_WRAP = 7
AUTO_REPEAT = 8
PRINTER_FORM_FEED = 18
PRINTER_EXTENT = 19

# Character sets
CS_US = 'CS_US'
CS_UK = 'CS_UK'
CS_DRAWING = 'CS_DRAWING'
CS_ALTERNATE = 'CS_ALTERNATE'
CS_ALTERNATE_SPECIAL = 'CS_ALTERNATE_SPECIAL'

# Groupings (or something?? These are like variables that can be bound to character sets)
G0 = 'G0'
G1 = 'G1'

# G2 and G3 cannot be changed, but they can be shifted to.
G2 = 'G2'
G3 = 'G3'

# Character attributes
UNDERLINE = 'UNDERLINE'
REVERSE_VIDEO = 'REVERSE_VIDEO'
BLINK = 'BLINK'
BOLD = 'BOLD'
NORMAL = 'NORMAL'

class ServerProtocol(protocol.Protocol):
    __implements__ = (ITerminalTransport,)

    protocol = None

    for keyID in ('UP_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'LEFT_ARROW',
                  'HOME', 'INSERT', 'DELETE', 'END', 'PGUP', 'PGDN',
                  'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                  'F10', 'F11', 'F12'):
        exec '%s = object()' % (keyID,)

    _databuf = ''
    lastWrite = ''

    def __init__(self, protocolFactory, *a, **kw):
        self.protocolFactory = protocolFactory
        self.protocolArgs = a
        self.protocolKwArgs = kw

        self._cursorReports = []

    def connectionMade(self):
        self.protocol = self.protocolFactory(*self.protocolArgs, **self.protocolKwArgs)
        self.protocol.makeConnection(self)

    def dataReceived(self, data):
        data = self._databuf + data
        self._databuf = ''
        escBuf = []

        for ch in data:
            if escBuf:
                if ch in CST:
                    self._handleControlSequence(ch, escBuf)
                    escBuf = []
                else:
                    escBuf.append(ch)
            elif ch == CSI:
                escBuf.append(ch)
            else:
                self.protocol.keystrokeReceived(ch)
        if escBuf:
            self._databuf = ''.join(escBuf)

    def _handleControlSequence(self, terminal, buf):
        f = getattr(self.controlSequenceParser, CST[terminal], None)
        if f is None:
            self.protocol.unhandledControlSequence(''.join(buf) + terminal)
        else:
            f(self, self.protocol, ''.join(buf))

    class ControlSequenceParser:
        def h(self, proto, handler, buf):
            if buf.startswith('\x1b['):
                # XXX - Handle '?' to introduce ANSI-Compatible private modes.
                modes = buf[2:].split(';')
                handler.setMode(modes)
            else:
                handler.unhandledControlSequence(buf + 'h')

        def l(self, proto, handler, buf):
            if buf.startswith('\x1b['):
                # XXX - Handle '?' to introduce ANSI-Compatible private modes.
                modes = buf[2:].split(';')
                handler.resetMode(modes)
            else:
                handler.unhandledControlSequence(buf + 'l')

        def r(self, proto, handler, buf):
            if buf.startswith('\x1b['):
                parts = buf.split(';')
                if len(parts) != 2:
                    # XXX - Is this right?  Are they both required?  If one or both can
                    # be omitted, what does it look like?  "\x1b[;r"?  "\x1b[r"?  Something
                    # else?
                    handler.unhandledControlSequence(buf + 'r')
                else:
                    try:
                        pt, pb = int(parts[0]), int(parts[1])
                    except ValueError:
                        handler.unhandledControlSequence(buf + 'r')
                    else:
                        handler.selectScrollRegion(pt, pb)

        def A(self, proto, handler, buf):
            if buf == '\x1b[':
                handler.keystrokeReceived(proto.UP_ARROW)
            else:
                handler.unhandledControlSequence(buf + 'A')

        def B(self, proto, handler, buf):
            if buf == '\x1b[':
                handler.keystrokeReceived(proto.DOWN_ARROW)
            else:
                handler.unhandledControlSequence(buf + 'B')

        def C(self, proto, handler, buf):
            if buf == '\x1b[':
                handler.keystrokeReceived(proto.RIGHT_ARROW)
            else:
                handler.unhandledControlSequence(buf + 'C')

        def D(self, proto, handler, buf):
            if buf == '\x1b[':
                handler.keystrokeReceived(proto.LEFT_ARROW)
            else:
                handler.unhandledControlSequence(buf + 'D')

        def R(self, proto, handler, buf):
            if not proto._cursorReports:
                handler.unhandledControlSequence(buf + 'R')
            elif buf.startswith('\x1b['):
                report = buf[2:]
                parts = report.split(';')
                if len(parts) != 2:
                    handler.unhandledControlSequence(buf + 'R')
                else:
                    Pl, Pc = parts
                    try:
                        Pl, Pc = int(Pl), int(Pc)
                    except ValueError:
                        handler.unhandledControlSequence(buf + 'R')
                    else:
                        d = proto._cursorReports.pop(0)
                        d.callback((Pc - 1, Pl - 1))
            else:
                handler.unhandledControlSequence(buf + 'R')

        def tilde(self, proto, handler, buf):
            map = (proto.HOME, proto.INSERT, proto.DELETE,
                   proto.END, proto.PGUP, proto.PGDN)
            if buf.startswith('\x1b['):
                ch = buf[2:]
                try:
                    v = int(ch)
                except ValueError:
                    handler.unhandledControlSequence(buf + '~')
                else:
                    if v > 0 and v <= len(map):
                        handler.keystrokeReceived(map[v - 1])
                    else:
                        handler.unhandledControlSequence(buf + '~')
            else:
                handler.unhandledControlSequence(buf + '~')

    controlSequenceParser = ControlSequenceParser()

    # ITerminal
    def cursorUp(self, n=1):
        self.write('\x1b[%dA' % (n,))

    def cursorDown(self, n=1):
        self.write('\x1b[%dB' % (n,))

    def cursorForward(self, n=1):
        self.write('\x1b[%dC' % (n,))

    def cursorBackward(self, n=1):
        self.write('\x1b[%dD' % (n,))

    def cursorPosition(self, column, line):
        self.write('\x1b[%d;%dH' % (line + 1, column + 1))

    def cursorHome(self):
        self.write('\x1b[H')

    def index(self):
        self.write('\x1bD')

    def reverseIndex(self):
        self.write('\x1bM')

    def nextLine(self):
        self.write('\x1bE')

    def saveCursor(self):
        self.write('\x1b7')

    def restoreCursor(self):
        self.write('\x1b8')

    def setMode(self, modes):
        # XXX Support ANSI-Compatible private modes
        self.write('\x1b[%sh' % (';'.join(map(str, modes)),))

    def resetMode(self, modes):
        # XXX Support ANSI-Compatible private modes
        self.write('\x1b[%sl' % (';'.join(map(str, modes)),))

    def applicationKeypadMode(self):
        self.write('\x1b=')

    def numericKeypadMode(self):
        self.write('\x1b>')

    def selectCharacterSet(self, charSet, which):
        # XXX Rewrite these as dict lookups
        if which == G0:
            which = '('
        elif which == G1:
            which = ')'
        else:
            raise ValueError("`which' argument to selectCharacterSet must be G0 or G1")
        if charSet == CS_UK:
            charSet = 'A'
        elif charSet == CS_US:
            charSet = 'B'
        elif charSet == CS_DRAWING:
            charSet = '0'
        elif charSet == CS_ALTERNATE:
            charSet = '1'
        elif charSet == CS_ALTERNATE_SPECIAL:
            charSet = '2'
        else:
            raise ValueError("Invalid `charSet' argument to selectCharacterSet")
        self.write('\x1b' + which + charSet)

    def singleShift2(self):
        self.write('\x1bN')

    def singleShift3(self):
        self.write('\x1bO')

    def selectGraphicRendition(self, *attributes):
        # XXX Rewrite this as a dict lookup
        attrs = []
        for a in attributes:
            if a == UNDERLINE:
                attrs.append('4')
            elif a == REVERSE_VIDEO:
                attrs.append('7')
            elif a == BLINK:
                attrs.append('5')
            elif a == BOLD:
                attrs.append('1')
            elif a == NORMAL:
                attrs.append('0')
        self.write('\x1b[%sm' % (';'.join(attrs),))

    def horizontalTabulationSet(self):
        self.write('\x1bH')

    def tabulationClear(self):
        self.write('\x1b[q')

    def tabulationClearAll(self):
        self.write('\x1b[3q')

    def doubleHeightLine(self, top=True):
        if top:
            self.write('\x1b#3')
        else:
            self.write('\x1b#4')

    def singleWidthLine(self):
        self.write('\x1b#5')

    def doubleWidthLine(self):
        self.write('\x1b#6')

    def eraseToLineEnd(self):
        self.write('\x1b[K')

    def eraseToLineBeginning(self):
        self.write('\x1b[1K')

    def eraseLine(self):
        self.write('\x1b[2K')

    def eraseToDisplayEnd(self):
        self.write('\x1b[J')

    def eraseToDisplayBeginning(self):
        self.write('\x1b[1J')

    def eraseDisplay(self):
        self.write('\x1b[2J')

    def deleteCharacter(self, n=1):
        self.write('\x1b[%dP' % (n,))

    def insertLine(self, n=1):
        self.write('\x1b[%dL' % (n,))

    def deleteLine(self, n=1):
        self.write('\x1b[%dM' % (n,))

    def setScrollRegion(self, first=None, last=None):
        if first is not None:
            first = '%d' % (first,)
        else:
            first = ''
        if last is not None:
            last = '%d' % (last,)
        else:
            last = ''
        self.write('\x1b[%s;%sr' % (first, last))

    def resetScrollRegion(self):
        self.setScrollRegion()

    def reportCursorPosition(self):
        d = defer.Deferred()
        self._cursorReports.append(d)
        self.write('\x1b[6n')
        return d

    def reset(self):
        self.write('\x1bc')

    # ITransport
    def write(self, bytes):
        self.lastWrite = bytes
        self.transport.write(bytes)

    def writeSequence(self, bytes):
        self.write(''.join(bytes))

    def loseConnection(self):
        self.reset()
        self.transport.loseConnection()

    def connectionLost(self, reason):
        self.protocol.connectionLost(reason)
        self.protocol = None


