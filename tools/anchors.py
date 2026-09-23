"""Context anchors for string literals.

A literal is identified by its value plus the few code tokens right before it
(e.g. `ISButton : new (` or `label =`). That survives line shifts in upstream
updates, while keeping keys that share a display word untouched."""
from lualex import code_tokens

CTX_TOKENS = 4


def _ctx_text(tok):
    if tok.kind in ('string', 'longstring'):
        return '"' + tok.value.replace('\n', '\\n')[:40] + '"'
    return tok.text


def literals_with_context(src):
    """Yield (token, context string) for every string literal in the source."""
    toks = code_tokens(src)
    for i, t in enumerate(toks):
        if t.kind not in ('string', 'longstring'):
            continue
        prev = toks[max(0, i - CTX_TOKENS):i]
        yield t, ' '.join(_ctx_text(p) for p in prev)
