"""Minimal Lua 5.1 lexer: enough to locate string literals and comments by offset."""
import re

_LONG_OPEN = re.compile(r'\[(=*)\[')
_NAME = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
_NUMBER = re.compile(r'0[xX][0-9a-fA-F]+|(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?')
_OPS = ['...', '..', '==', '~=', '<=', '>=']


class Token:
    __slots__ = ('kind', 'text', 'start', 'end', 'value')

    def __init__(self, kind, text, start, end, value=None):
        self.kind, self.text, self.start, self.end, self.value = kind, text, start, end, value

    def __repr__(self):
        return f'Token({self.kind},{self.text!r}@{self.start})'


def decode_string(body):
    """Decode a quoted Lua string body (without quotes) to a Python str.

    Decimal escapes like \\195\\161 are UTF-8 bytes, so decode via a byte buffer."""
    out = bytearray()
    i = 0
    simple = {'n': 10, 't': 9, 'r': 13, 'a': 7, 'b': 8, 'f': 12, 'v': 11,
              '\\': 92, '"': 34, "'": 39, '\n': 10}
    while i < len(body):
        c = body[i]
        if c == '\\' and i + 1 < len(body):
            n = body[i + 1]
            if n.isdigit():
                m = re.match(r'\d{1,3}', body[i + 1:])
                out.append(int(m.group(0)) & 0xFF)
                i += 1 + len(m.group(0))
                continue
            if n in simple:
                out.append(simple[n])
                i += 2
                continue
            out.extend(n.encode('utf-8'))
            i += 2
            continue
        out.extend(c.encode('utf-8'))
        i += 1
    return out.decode('utf-8', errors='replace')


def encode_string(text, quote='"'):
    """Encode a Python str as a Lua quoted literal body, non-ASCII as decimal byte escapes
    (the convention the other A-Life translations use and that Kahlua renders correctly)."""
    out = []
    for ch in text:
        if ch == '\\':
            out.append('\\\\')
        elif ch == quote:
            out.append('\\' + quote)
        elif ch == '\n':
            out.append('\\n')
        elif ch == '\t':
            out.append('\\t')
        elif ord(ch) < 128:
            out.append(ch)
        else:
            out.extend('\\%d' % b for b in ch.encode('utf-8'))
    return ''.join(out)


def tokenize(src):
    toks = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if c in ' \t\r\n':
            i += 1
            continue
        if src.startswith('--', i):
            m = _LONG_OPEN.match(src, i + 2)
            if m:
                close = ']' + m.group(1) + ']'
                j = src.find(close, m.end())
                j = n if j < 0 else j + len(close)
            else:
                j = src.find('\n', i)
                j = n if j < 0 else j
            toks.append(Token('comment', src[i:j], i, j))
            i = j
            continue
        if c in '"\'':
            j = i + 1
            while j < n and src[j] != c:
                if src[j] == '\\':
                    j += 1
                elif src[j] == '\n':
                    break
                j += 1
            j += 1
            body = src[i + 1:j - 1]
            toks.append(Token('string', src[i:j], i, j, decode_string(body)))
            i = j
            continue
        if c == '[':
            m = _LONG_OPEN.match(src, i)
            if m:
                close = ']' + m.group(1) + ']'
                j = src.find(close, m.end())
                j = n if j < 0 else j + len(close)
                body = src[m.end():j - len(close)]
                if body.startswith('\n'):
                    body = body[1:]
                toks.append(Token('longstring', src[i:j], i, j, body))
                i = j
                continue
        m = _NAME.match(src, i)
        if m:
            toks.append(Token('name', m.group(0), i, m.end()))
            i = m.end()
            continue
        m = _NUMBER.match(src, i)
        if m and m.group(0):
            toks.append(Token('number', m.group(0), i, m.end()))
            i = m.end()
            continue
        for op in _OPS:
            if src.startswith(op, i):
                toks.append(Token('op', op, i, i + len(op)))
                i += len(op)
                break
        else:
            toks.append(Token('op', c, i, i + 1))
            i += 1
    return toks


def code_tokens(src):
    return [t for t in tokenize(src) if t.kind != 'comment']


def line_of(src, offset):
    return src.count('\n', 0, offset) + 1
