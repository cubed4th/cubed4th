#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

       ______    ____    _____    _______   _    _     /\   ____
  _   |  ____|  / __ \  |  __ \  |__   __| | |  | |   |/\| |___ \    _
 (_)  | |__    | |  | | | |__) |    | |    | |__| |          __) |  (_)
      |  __|   | |  | | |  _  /     | |    |  __  |         |__ <
  _   | |      | |__| | | | \ \     | |    | |  | |         ___) |   _
 (_)  |_|       \____/  |_|  \_\    |_|    |_|  |_|        |____/   ( )
                                                                    |/


)







"""  # __banner__

class Engine:  # { The Reference Implementation of FORTH^3 : p-unity }

    def __init__(self, run=None, run_tests=1, **kwargs):

        self.root = TASK(self, root=True)
        self.call = CALL(self)

        self.sandbox = kwargs.get('sandbox', 0)

        self.guards = kwargs.get('guards', "")
        if not run == None:
            self.guards = "```"

        self.digits = {}
        for digit in "#$%-01234567890":
            self.digits[digit] = True

        vis = None if 'vis' not in kwargs else kwargs['vis']

        def load(self, vis, names):
            for name_level in names.split(" "):
                name, level = tuple(name_level.split(":"))
                if self.sandbox > 0 and self.sandbox < int(level): continue
                exec(f"from .WORDS import F_{name}")
                exec(f"self.{name} = F_{name}.LIB(self, self.root)")
                exec(f"if vis: vis.before_import('{name}', self.{name})")
                exec(f"self.import_lib(vis, self.{name})")
                exec(f"if vis: vis.after_import('{name}', self.{name})")

        if vis: vis.before_imports(self)

        # The :num indicates what level of sandbox applies to all words

        load(self, vis, "CORE:1 STACK:1 MATH:1 CONTROL:1")
        load(self, vis, "INPUT:3 OUTPUT:3 REPL:1")
        load(self, vis, "OBJECT:1 JSON:1")
        load(self, vis, "UNICODE:3 CURSES:6")

        load(self, vis, "HTTPS:6")

        load(self, vis, "ECDSA:1 HASHES:1 CHAINS:1")

        if vis: vis.after_imports(self)

        for level in [1, 2, 3]:
            if run_tests < level:
                break

            self.execute_tests(__tests__[level])
            self.execute_tests(self.root.tests[level])

        __banner__ = None
        if __banner__:
            self.execute(__banner__)

        if run:
            self.execute(run)

    def raise_SyntaxError(self, details):
        raise ForthSyntaxException(details)

    def raise_RuntimeError(self, details):
        raise ForthRuntimeException(details)

    symbol_map = {
        "bang": "!",
        "at": "@",
        "hash": "#",
        "dollar": "$",
        "tick": "'",
        "quote": '"',
        "btick": "`",
        "equal": "=",
        "under": "_",
        "tilde": "~",
        "minus": "-",
        "m": "-",
        "plus": "+",
        "pipe": "|",
        "slash": "\\",
        "divide": "/",
        "qmark": "?",
        "colon": ":",
        "semicolon": ";",
        "dot": ".",
        "comma": ",",
        "percent": "%",
        "carat": "^",
        "amper": "&",
        "times": "*",
        "lparen": "(",
        "rparen": ")",
        "langle": "<",
        "rangle": ">",
        "lbrack": "[",
        "rbrack": "]",
        "lbrace": "{",
        "rbrace": "}",
        "unicorn": "\u1F984",
        "rainbow": "\u1F308",
        "astonished": "\u1F632",
    }

    def add_word(self, name, code, where=None):
        parts = name.lower().split("_")
        name = []
        meta = None
        for part in parts:
            if meta is None:
                if part == "":
                    meta = []
                    continue
            else:
                meta.append(part)
                continue
            name.append(self.symbol_map.get(part, part))

        name = "".join(name)
        where = where if where else self.root

        #  if name in where:
        #      raise ForthException(f"{name}: error(-4): Word Already Defined")

        if name in where.word_immediate:
            del where.word_immediate[name]

        if not meta is None:
            if "i" in meta[0]:
                where.word_immediate[name] = True

        where.words[name] = code
        argc = code.__code__.co_argcount
        if argc > 3:
            where.word_argc[name] = argc - 3

        where.tests[1].append(code.__doc__)

        return name

    def add_sigil(self, name, code, where=None):
        parts = name.lower().split("_")

        name = []
        meta = None
        for part in parts:
            if meta is None:
                if part == "":
                    meta = []
                    continue
            else:
                meta.append(part)
                continue

            name.append(self.symbol_map.get(part, part))

        name = "".join(name)
        where = where if where else self.root

        if name in where.word_immediate:
            del where.sigil_immediate[name]

        if meta is not None:
            if "i" in meta[0]:
                where.sigil_immediate[name] = True

        #  if name in where:
        #      raise ForthException(f"{name}: error(-4): Sigil Already Defined")

        where.sigils[name] = code

        where.tests[1].append(code.__doc__)

        return name

    def import_lib(self, vis, source, where=None):
        word_names = []
        sigil_names = []
        for fname in dir(source):
            parts = fname.split("_")

            if len(parts) > 1 and parts[0][:4] == "word":
                word = getattr(source, fname)
                word_names.append((word.__code__.co_firstlineno, fname))

            if len(parts) > 1 and parts[0][:5] == "sigil":
                sigil = getattr(source, fname)
                sigil_names.append((sigil.__code__.co_firstlineno, fname))

        def full2short(fname):
            parts = fname.split("_")
            name = []
            meta = None
            for part in parts:
                if meta is None:
                    if part == "":
                        meta = []
                        continue
                else:
                    meta.append(part)
                    continue

                name.append(part)

            return "_".join(name)

        sigil_names.sort()
        for order, fname in sigil_names:
            code = getattr(source, fname)
            tname = self.add_sigil(fname[6:], code)
            if not vis: continue
            vis.visit_sigil(code, fname, full2short(fname)[6:], tname)

        word_names.sort()
        for order, fname in word_names:
            code = getattr(source, fname)
            tname = self.add_word(fname[5:], code)
            if not vis: continue
            vis.visit_word(code, fname, full2short(fname)[5:], tname)


        if not where:
            where = self.root

        where.tests[2].append(source.__doc__)

    @staticmethod
    def to_number(e, t, c, token):

        if not isinstance(token, str):
            return (True, token)

        if not token[0] in e.digits:
            return (False, None)

        if token in e.root.words or token in t.words:
            return (False, None)

        token = token.replace("_", "")
        if token in ["", "#", "$", "%"]:
            return (False, None)

        base = t.base
        if token[0] == "#":
            token = token[1:]
        elif token[0] == "$":
            base = 16
            token = token[1:]
        elif token[0] == "%":
            base = 2
            token = token[1:]

        if token[0] == "-":
            if len(token) == 1:
                return (False, None)
            if not token[1].isdigit():
                return (False, None)

        if "j" in token:
            return (True, complex(token))
        else:
            if "." in token:
                if base == 10:
                    return (True, Decimal(token))
                else:
                    return (True, Decimal(int(token, base)))
            else:
                return (True, int(token, base))

    @staticmethod
    def state_INTERPRET(e, t, c, token):

        if not isinstance(token, str):
            if not isinstance(token, tuple):
                t.stack.append(token)
                return

            if len(token) == 1:
                t.stack.extend(token)
            elif len(token) == 2:
                Engine.run(e, t, c, token, token_l=None)
            else:
                print(token)
                e.raise_RuntimeError("!: error(-1): Unknown XT")

            return

        if len(token) == 0: return

        token_l = token.lower() if isinstance(token, str) else token

        is_number, value = e.to_number(e, t, c, token_l)
        if is_number:
            t.stack.append(value)
            return

        Engine.run(e, t, c, token, token_l)

    @staticmethod
    def run(e, t, c, token, token_l=None):

        if isinstance(token, tuple):

            if len(token) == 1:
                t.stack.extend(token)
                return

            code, argc = token

        else:

            if not (token_l in t.words or token_l in e.root.words):

                for sigil_len in [5, 4, 3, 2, 1]:
                    sigil = token_l[:sigil_len]
                    if sigil in t.sigils:
                        t.sigils[sigil](e, t, c, token, start=True)
                        return
                    if sigil in e.root.sigils:
                        e.root.sigils[sigil](e, t, c, token, start=True)
                        return

                details = f"{token_l}: error(-13): word not found"
                raise ForthException(details)

            if token_l in t.words:
                code = t.words[token_l]
                argc = t.word_argc.get(token_l, 0)
            else:
                code = e.root.words[token_l]
                argc = e.root.word_argc.get(token_l, 0)

        if isinstance(code, list):
            t.last_call = token_l
            if c.depth == 0:
                c.depth += 1
                e.execute_tokens(e, t, c, code)
                c.depth -= 1
            else:
                e.execute_tokens(e, t, CALL(e, c), code)

            return

        if isinstance(code, tuple):
            if len(token) == 1:
                t.stack.extend(code)
                return
            elif len(code) == 2:
                code, argc = code
            else:
                e.raise_RuntimeError("!: error(-1): Unknown XT")

        if argc > len(t.stack):
            details = f"{token}: error(-4): Needs {argc} arg(s)"
            raise ForthException(details)

        args = []
        if argc > 0:
            t.stack, args = t.stack[:-argc], t.stack[-argc:]

        result = code(e, t, c, *args)
        if result is not None:
            if isinstance(result, tuple):
                t.stack.extend(result)
            else:
                t.stack.append(result)

    @staticmethod
    def execute_tokens(e, t, c, tokens):
        for token in tokens:
            if token in ["#"]:
                break
            t.state(e, t, c, token)
            if c.EXIT:
                break

    def execute_tests(self, tests):
        if not tests:
            return
        for test in tests:
            if not test:
                continue
            task = TASK(self)
            call = CALL(self, self.call)
            for line in test.split("\n"):
                line = line.strip()
                if line == "" or line[0] in ["#"]:
                    continue

                if line == "--END--":
                    break

                f_count = task.test["f"]
                if 1:  # try:

                    call.tokens = line.split()
                    while len(call.tokens):
                        token = call.tokens.pop(0)
                        if token in ["#"]:
                            break
                        state = task.state
                        state(self, task, call, token)
                        if call.EXIT:
                            break

                #    except Exception as ex:
                #        print(ex)
                #        task.test["f"] += 1

                if not f_count == task.test["f"]:
                    print("!!! ", line)

            self.root.test["p"] += task.test["p"]
            self.root.test["f"] += task.test["f"]

    def execute(self, lines, guards=""):
        guards = self.guards if guards == "" else guards
        include = True if guards == "" else False
        self.call.EXIT = False

        lines = lines.split("\n")
        while len(lines):

            line = lines.pop(0)

            self.root.line += 1
            self.root.lines[self.root.line] = line

            if not guards == "":
                if line.lstrip()[0:3] == guards[0:3]:
                    include = ~include
                    continue

            if not include: continue

            self.call.line = line
            self.call.lines = lines
            self.call.tokens = line.split()
            if len(self.call.tokens) == 0:
                self.call.tokens.append("")

            while len(self.call.tokens):
                token = self.call.tokens.pop(0)
                self.root.state(self, self.root, self.call, token)
                if self.call.EXIT:
                   return




class TASK:
    def __init__(self, engine, root=False):

        self.engine = engine
        self.is_root = root

        self.stack = []
        self.rstack = []

        self.memory = {}
        self.here = 1_000_000 if root else 1

        self.sigils = {}
        self.sigil_immediate = {}

        self.words = {}
        self.word_argc = {}
        self.word_does = {}
        self.word_immediate = {}

        self.last_call = ""
        self.last_create = ""
        self.last_compile = ""

        self.base = 10

        self.tick_space = "'"

        self.line = 0
        self.lines = {}

        self.test = {"p": 0, "f": 0, "e": 0}
        self.tests = {1: [], 2: [], 3: []}

        self.state = engine.state_INTERPRET


class CALL:
    def __init__(self, engine, parent=None):
        self.engine = engine
        self.parent = parent
        self.tokens = []
        self.depth = 0
        self.stack = []
        self.EXIT = False
        self.FAIL = False

    def find_struct(self, name, key="?"):
        call = self
        block = None
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if key:
                    if call.stack[index].get(key, "") == name:
                        block = call.stack[index]
                        call = None
                        break
                else:
                    if name in call.stack[index]:
                        block = call.stack[index]
                    call = None
                    break

            call = call.parent if call else None

        return block


class ForthException(Exception):
    pass


class ForthSyntaxException(ForthException):
    pass


class ForthRuntimeException(ForthException):
    pass


from decimal import Decimal

__tests__ = {1: [], 2: [], 3: []}

__tests__[1].append(
    """

T{ : GT1 123 ; -> }T
T{ ' GT1 EXECUTE -> 123 }T
T{ : GT2 ['] GT1 ; IMMEDIATE -> }T

# T{ 0.1 0.2 + -> 0.3 }T

# T{ 'FOO'BAR' -> (("FOO BAR")) }T

# T{ ''' (.__len__) -> (" ") #1 }T

# T{ ("--") (.__len__) -> ("--") #2 }T

# ( : IDE
# CURSES
# 0 0 20 20 WINDOW BORDER REFRESH
# GETKEY
# ; )

# : COUNTDOWN    ( n --)
#                BEGIN  CR   DUP  .  1 -   DUP   0  =   UNTIL  DROP  ;

# 5 COUNTDOWN

"""
)

__tests__[3].append(
    """

0 CONSTANT 0S
0 INVERT CONSTANT 1S

T{ <TRUE>  -> 0 INVERT }T
T{ <FALSE> -> 0 }T

: TEN I[ 5 5 + ]I LITERAL ; IM...

: FOO TEN ;

T{ ' FOO -> [ 10 , ] }T

"""
)
