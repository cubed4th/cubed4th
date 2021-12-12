#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       _____    ____    _____    ______
  /\| |/\   / ____|  / __ \  |  __ \  |  ____|
  \ ` ' /  | |      | |  | | | |__) | | |__
 |_     _| | |      | |  | | |  _  /  |  __|
  / , . \  | |____  | |__| | | | \ \  | |____
  \/|_|\/   \_____|  \____/  |_|  \_\ |______|



)
# : ; ' ." ! @ @NONE CREATE HERE ALLOT
# VARIABLE CONSTANT VALUE TO LOCALS| |
# 1+ 1- 2+ 2- <TRUE> <FALSE>
# .>> <<.




"""  # __banner__


class LIB:  # { CORE : words }
    def __init__(self, e, t, **kwargs):
        # t.tests[1].append(__tests_1__)
        pass

    @staticmethod  ### ( ###
    def sigil_lparen(e, t, c, token, start=False):

        if isinstance(token, str) and len(token) and token[-1] == ")":
            t.state = e.state_INTERPRET
            return

        t.state = LIB.sigil_lparen


    @staticmethod  ### ((( ###
    def sigil_lparen_lparen_lparen(e, t, c, token, start=False):

        if isinstance(token, str) and len(token) and token[-3:] == ")))":
            t.state = e.state_INTERPRET
            return

        t.state = LIB.sigil_lparen_lparen_lparen


    @staticmethod  ### \ ###
    def sigil_slash(e, t, c, token, start=False):
        c.tokens = []

    @staticmethod  ### # ###
    def word_hash(e, t, c):
        c.tokens = []

    @staticmethod  ### A{ ###
    def word_A_lbrace(e, t, c):
        stack = copy.deepcopy(t.stack)
        c.stack.append({"?": "TEST", "STACK": t.stack, "ASSERT": True})
        t.stack = stack

    @staticmethod  ### T{ ###
    def word_T_lbrace(e, t, c):
        stack = copy.deepcopy(t.stack)
        c.stack.append({"?": "TEST", "STACK": t.stack})
        t.stack = stack

    @staticmethod  ### T{! ###
    def word_T_lbrace_bang(e, t, c):
        stack = copy.deepcopy(t.stack)
        c.stack.append({"?": "TEST!", "STACK": t.stack})
        t.stack = stack

    @staticmethod  ### -> ###
    def word_m_rangle(e, t, c):
        block = c.stack[-1]
        block["HAVE"] = t.stack[len(block["STACK"]) :]
        t.stack = copy.deepcopy(block["STACK"])

    @staticmethod  ### --END-- ###
    def word_m_minus_END_m_minus__R(e, t, c):
        #block = c.stack[-1]
        #block["END"] = True
        pass

    @staticmethod  ### }A ###
    def word_rbrace_A(e, t, c):
        LIB.word_rbrace_T(e, t, c)

    @staticmethod  ### }T ###
    def word_rbrace_T(e, t, c):
        block = c.stack.pop()
        assert block["?"] == "TEST"

        have = block["HAVE"]
        need = t.stack[len(block["STACK"]) :]
        t.stack = block["STACK"]

        if need == have:
            t.test["p"] += 1
            return

        line = t.lines.get(t.line, "")

        if not len(need) == len(have):
            t.test["f"] += 1
            print(f"WRONG NUMBER OF RESULTS: {have} ~= {need} {line}")
            return

        equal = True
        for i in range(0, len(need)):
            if isinstance(have[i], bool) or isinstance(need[i], bool):
                equal = (not have[i]) == (not need[i])
            else:
                equal = have[i] == need[i]
            if not equal:
                break

        if not equal:
            t.test["f"] += 1
            if block.get("ASSERT", False):
                if isinstance(have[i], bool) or isinstance(need[i], bool):
                    assert (not have[i]) == (not need[i])
                else:
                    assert have[i] == need[i]
            else:
                print(f"INCORRECT RESULT: {have} ~= {need} {line}")

    @staticmethod  ### TESTING ###
    def word_TESTING__R(e, t, c):
        c.stack.append({"?": "TESTING", "LINE": t.line, "r": t.state})
        t.state = LIB.state_TESTING

    @staticmethod
    def state_TESTING(e, t, c, token):
        struct = c.stack[-1]
        if t.line == struct["LINE"]:
            print(token, end=" ")
            return

        c.stack.pop()
        t.state = struct["r"]
        t.state(e, t, c, token)

    @staticmethod  ### <TRUE> ###
    def word_langle_TRUE_rangle__R_b(e, t, c):
        return (True,)

    @staticmethod  ### <FALSE> ###
    def word_langle_FALSE_rangle__R_b(e, t, c):
        "T{ <FALSE> -> <FALSE> }T"
        return (False,)

    @staticmethod  ### <NONE> ###
    def word_langle_NONE_rangle__R_b(e, t, c):
        return (None,)

    @staticmethod  ### <NULL> ###
    def word_langle_NULL_rangle__R_b(e, t, c):
        return (None,)

    @staticmethod  ### <NIL> ###
    def word_langle_NIL_rangle__R_b(e, t, c):
        return (None,)

    @staticmethod  ### DECIMAL ###
    def word_DECIMAL__R(e, t, c):
        t.base = 10

    @staticmethod  ### HEX ###
    def word_HEX__R(e, t, c):
        t.base = 16

    @staticmethod  ### = ###
    def word_equal__R_b(e, t, c, x1, x2):
        """



        T{  0  0 = -> <TRUE>  }T
        T{  1  1 = -> <TRUE>  }T
        T{ -1 -1 = -> <TRUE>  }T
        T{  1  0 = -> <FALSE> }T
        T{ -1  0 = -> <FALSE> }T
        T{  0  1 = -> <FALSE> }T
        T{  0 -1 = -> <FALSE> }T
        """
        return (x1 == x2,)

    @staticmethod  ### < ###
    def word_langle__R_b(e, t, c, x1, x2):
        return (x1 < x2,)

    @staticmethod  ### U< ###
    def word_U_langle__R_b(e, t, c, u1, u2):
        return (u1 < u2,)

    @staticmethod  ### <= ###
    def word_langle_equal__R_b(e, t, c, x1, x2):
        return (x1 <= x2,)

    @staticmethod  ### > ###
    def word_rangle__R_b(e, t, c, x1, x2):
        return (x1 > x2,)

    @staticmethod  ### U> ###
    def word_rangle__R_b(e, t, c, u1, u2):
        return (u1 > u2,)

    @staticmethod  ### >= ###
    def word_rangle_equal__R_b(e, t, c, x1, x2):
        return (x1 >= x2,)

    @staticmethod  ### <> ###
    def word_langle_rangle__R_b(e, t, c, x1, x2):
        return (x1 != x2,)

    @staticmethod  ### ~= ###
    def word_tilde_equal__R_b(e, t, c, x1, x2):
        return (x1 != x2,)

    @staticmethod  ### != ###
    def word_bang_equal__R_b(e, t, c, x1, x2):
        return (x1 != x2,)

    @staticmethod  ### 0= ###
    def word_0_equal__R_b(e, t, c, x):
        """
        T{ 0 0= -> <true> }T
        T{ 0.0 0= -> <true> }T
        T{ 0.0j 0= -> <true> }T
        """
        return (x == 0,)

    @staticmethod  ### 0< ###
    def word_0_langle__R_b(e, t, c, x):
        return (x < 0,)

    @staticmethod  ### 0> ###
    def word_0_rangle__R_b(e, t, c, x):
        return (x > 0,)

    @staticmethod  ### ." ###
    def word_dot_quote(e, t, c):
        c.stack.append({"m": "DOT_QUOTE", 0: t.line, 1: []})
        t.state = LIB.state_dot_quote

    @staticmethod
    def state_dot_quote(e, t, c, token):
        end = token[-1] == '"'
        token = token[:-1] if end else token

        block = c.stack[-1]
        block[1].append("\n" * (t.line - block[0]) + token)
        block[0] = t.line

        if end:
            c.stack.pop()
            print(" ".join(block[1]), end="")
            t.state = e.state_INTERPRET


    @staticmethod  ### S"" ###
    def word_S_quote_quote(e, t, c):
        """
S""
Hello
World
""S

        """
        c.stack.append({"m": "S_QUOTE_QUOTE", 1: []})
        c.tokens = []
        t.state = LIB.state_multi_line_string


    @staticmethod
    def state_multi_line_string(e, t, c, token):
        end = token == "\"\"S"
        block = c.stack[-1]
        if end:
            c.stack.pop()
            t.stack.append("\n".join(block[1]))
            t.state = e.state_INTERPRET
            return

        # append the line verbatim and absorb all the tokens
        block[1].append(c.line)
        c.tokens = []


    @staticmethod  ### S" ###
    def word_S_quote(e, t, c):
        c.stack.append({"m": "S_QUOTE", 0: t.line, 1: []})
        t.state = LIB.state_S_quote

    @staticmethod
    def state_S_quote(e, t, c, token):
        end = token[-1] == '"'
        token = token[:-1] if end else token

        block = c.stack[-1]
        block[1].append("\n" * (t.line - block[0]) + token)
        block[0] = t.line

        if end:
            c.stack.pop()
            t.stack.append(" ".join(block[1]))
            t.state = e.state_INTERPRET

    @staticmethod  ### : ###
    def word_colon(e, t, c):
        struct = c.find_struct(" : ")
        if struct:
            struct[" : "](e, t, c)
            return

        c.stack.append({"?": ":", 0: 0})
        t.state = LIB.state_COMPILE

    @staticmethod  ### :NONAME ###
    def word_colon_NONAME__R(e, t, c):
        c.stack.append({"?": ":", 0: 1, 1: [], "=": ""})
        t.state = LIB.state_COMPILE

    @staticmethod  ### IM... ###
    def word_IM_dot_dot_dot__R(e, t, c):
        LIB.word_IMMEDIATE__R(e, t, c)

    @staticmethod  ### IMMEDIATE ###
    def word_IMMEDIATE__R(e, t, c):
        t.word_immediate[t.last_compile] = True

    @staticmethod  ### LITERAL ###
    def word_LITERAL__IR(e, t, c):
        """
        : TEN I[ 5 5 + ]I LITERAL ;
        T{ TEN -> 10 }T
        """
        struct = c.find_struct(":")
        if not struct:
            e.raise_RuntimeError("literal: error (-0): Only Valid During Compile")

        struct[struct[0]].append(t.stack.pop())

    @staticmethod  ### STATE ###
    def word_STATE__R_b(e, t, c):
        return (t.state == e.state_INTERPRET,)

    @staticmethod  ### I[ ###
    def word_I_lbrack__IR(e, t, c):
        t.state = e.state_INTERPRET

    @staticmethod  ### ]I ###
    def word_rbrack_I__R(e, t, c):
        t.state = LIB.state_COMPILE

    @staticmethod  ### CREATE ###
    def word_CREATE__R(e, t, c):
        """
        T{ CREATE CR1 -> }T
        T{ CR1   -> HERE }T

        T{ : FOO CREATE ; -> }T
        T{ FOO BAR -> }T
        T{ BAR -> HERE }T

        """
        name = c.tokens.pop(0).lower()
        t.last_create = name

        does = []
        if t.last_call in t.word_does:
            does = t.word_does[t.last_call]
        elif t.last_call in e.root.word_does:
            does = e.root.word_does[t.last_call]

        if len(does):
            t.words[name] = [(t.here,)] + does
        else:
            t.words[name] = [(t.here,)]

    @staticmethod  ### DOES> ###
    def word_DOES_rangle__IR(e, t, c):
        struct = c.stack[-1]
        # if not t.state == LIB.state_COMPILE:
        #    e.raise_SyntaxError("DOES>: error (-0): Not Valid Outside :")
        if struct[0] == 2:
            e.raise_SyntaxError("DOES>: error (-0): Only 1 DOES> Allowed")
        if struct["="] == "":
            e.raise_SyntaxError("DOES>: error (-0): Not Valid in :NONAME")

        struct[0] = 2
        struct[2] = []

    @staticmethod  ### ; ###
    def word_semicolon__IR(e, t, c):
        block = c.stack.pop()
        if "=" in block:
            if block["="] == "":
                t.stack.append(block[1])
            else:
                t.words[block["="]] = block[1]
                if 2 in block:
                    t.word_does[block["="]] = block[2]

        t.state = e.state_INTERPRET

    @staticmethod
    def state_COMPILE_INTERPRET(e, t, c, token):
        return e.state_INTERPRET(e, t, c, token)

    @staticmethod
    def state_COMPILE(e, t, c, token):
        block = c.stack[-1]
        if block[0] == 0:
            block[0] = 1
            block[1] = []
            t.last_compile = token.lower()
            block["="] = t.last_compile
            return

        if not isinstance(token, str):
            if isinstance(token, tuple):
                block[block[0]].extend(token)
            else:
                block[block[0]].append(token)
            return

        token_l = token.lower()

        if token_l in t.word_immediate or token_l in e.root.word_immediate:
            t.state = LIB.state_COMPILE_INTERPRET
            e.run(e, t, c, token, token_l)
            if t.state == LIB.state_COMPILE_INTERPRET:
                t.state = LIB.state_COMPILE
            return

        if token == "#" or token == "\\":
            block["#"] = t.line
            return

        if "#" in block:
            if block["#"] == t.line:
                return
            del block["#"]

        block[block[0]].append(token)

    @staticmethod  ### BL ###
    def word_BL__R_c(e, t, c):
        t.stack.append(32)

    @staticmethod  ### COUNT ###
    def word_COUNT__R_n(e, t, c, a):
        return (a + 1, t.memory.get(a, 0))

    @staticmethod  ### CHAR ###
    def word_CHAR__R_n(e, t, c):
        t.state = LIB.state_CHAR

    def state_CHAR(e, t, c, token):
        t.stack.append(ord(token[0]))
        t.state = e.state_INTERPRET

    @staticmethod  ### CHAR+ ###
    def word_CHAR_plus__R_a2(e, t, c, a1):
        return (a1 + 1,)

    @staticmethod  ### ! ###
    def word_bang__R(e, t, c, x, a):
        """"""
        if isinstance(a, int) and a >= 1_000_000:
            if not t.is_root:
                e.raise_RuntimeError("!: error(-1): Illegal Memory Access")

        t.memory[a] = x

    @staticmethod  ### *! ###
    def word_times_bang__R(e, t, c, x, a, s):
        """"""
        if isinstance(a, int) and a >= 1_000_000:
            if not t.is_root:
                e.raise_RuntimeError("!: error(-1): Illegal Memory Access")

        t.memory[a][s] = x


    @staticmethod  ### C! ###
    def word_C_bang__M__R(e, t, c, x, a):
        """"""
        if isinstance(a, int) and a >= 1_000_000:
            if not t.is_root:
                e.raise_RuntimeError("!: error(-1): Illegal Memory Access")

        t.memory[a] = x

    @staticmethod  ### 2! ###
    def word_2_bang__M__R(e, t, c, x1, x2, a):
        """"""
        if isinstance(a, int) and a >= 1_000_000:
            if not t.is_root:
                e.raise_RuntimeError("!: error(-1): Illegal Memory Access")

        t.memory[a] = x1
        t.memory[a + 1] = x2


    @staticmethod  ### *IN ###
    def word_times_IN__R_b(e, t, c, a, s):
        return (s in t.memory[a],)

    @staticmethod  ### @ ###
    def word_at__R_x(e, t, c, a):
        if isinstance(a, str):
            return (t.memory[a],)
        t.stack.append(t.memory.get(a, 0))


    @staticmethod  ### ?@ ###
    def word_qmark_at__R_b(e, t, c, a):
        return (True if a in t.memory else False,)


    @staticmethod  ### @NONE ###
    def word_at_NONE__R_x(e, t, c, a):
        t.stack.append(t.memory.get(a, None))

    @staticmethod  ### @0 ###
    def word_at_0__R_x(e, t, c, a):
        t.stack.append(t.memory.get(a, 0))

    @staticmethod  ### @"" ###
    def word_at_quote_quote__R_x(e, t, c, a):
        t.stack.append(t.memory.get(a, ""))

    @staticmethod  ### *@ ###
    def word_times_at__R_x(e, t, c, a, s):
        if isinstance(a, str):
            return (t.memory[a][s],)
        t.stack.append(t.memory.get(a, 0))

    @staticmethod  ### *@NONE ###
    def word_times_at_NONE__R_x(e, t, c, a, s):
        t.stack.append(t.memory[a].get(s, None))

    @staticmethod  ### *@0 ###
    def word_at_0__R_x(e, t, c, a, s):
        t.stack.append(t.memory[a].get(s, 0))

    @staticmethod  ### *@"" ###
    def word_at_quote_quote__R_x(e, t, c, a):
        t.stack.append(t.memory[a].get(a, ""))


    @staticmethod  ### C@ ###
    def word_C_at__R_x(e, t, c, a):
        t.stack.append(t.memory.get(a, 0))

    @staticmethod  ### 2@ ###
    def word_2_at__R_x_x(e, t, c, a):
        t.stack.append(t.memory.get(a, 0))
        t.stack.append(t.memory.get(a + 1, 0))

    @staticmethod  ### VALUE ### ( x "<spaces>name" -- )
    def word_VALUE__R(e, t, c, x):
        """
        T{  111 VALUE v1 -> }T
        T{ -999 VALUE v2 -> }T
        T{ v1 ->  111 }T
        T{ v2 -> -999 }T
        """
        c.stack.append({"?": "VALUE", "x": (x,)})
        t.state = LIB.state_VALUE

    @staticmethod
    def state_VALUE(e, t, c, token):
        struct = c.stack.pop()
        assert struct["?"] == "VALUE"
        t.words[token.lower()] = [struct["x"]]
        t.state = e.state_INTERPRET

    @staticmethod  ### LOCALS| ###
    def word_LOCALS_pipe__R(e, t, c):
        """ """
        c.stack.append({"?": "LOCALS|"})
        t.state = LIB.state_LOCALS_pipe

    @staticmethod
    def state_LOCALS_pipe(e, t, c, token):
        if token == "|":
            struct = c.stack.pop()
            assert struct["?"] == "LOCALS|"
            t.state = e.state_INTERPRET
            return

        t.words[token.lower()] = (t.stack.pop(),)
        t.state = LIB.state_LOCALS_pipe

    @staticmethod  ### TO ### ( x "<spaces>name" -- )
    def word_TO__R(e, t, c, x):
        """
        T{ 111 VALUE v1 ->     }T
        T{ 222 TO v1    ->     }T
        T{ v1           -> 222 }T
        T{ : vd1 v1 ;   ->     }T
        T{ vd1          -> 222 }T
        """
        c.stack.append({"?": "TO", "x": (x,)})
        t.state = LIB.state_TO

    @staticmethod
    def state_TO(e, t, c, token):
        struct = c.stack.pop()
        assert struct["?"] == "TO"
        t.words[token.lower()] = [struct["x"]]
        t.state = e.state_INTERPRET

    @staticmethod  ### CONSTANT ###
    def word_CONSTANT__R(e, t, c, x):
        """
        T{ 123 CONSTANT X123 ->     }T
        T{ X123              -> 123 }T
        T{ : EQU CONSTANT ;  ->     }T
        T{ X123 EQU Y123     ->     }T
        T{ Y123              -> 123 }T
        """
        c.stack.append(x)
        t.state = LIB.state_CONSTANT

    @staticmethod
    def state_CONSTANT(e, t, c, token):
        t.words[token.lower()] = [c.stack.pop()]
        t.state = e.state_INTERPRET

    @staticmethod  ### VARIABLE ###
    def word_VARIABLE__R_a(e, t, c):
        """
        T{ VARIABLE V1 ->     }T
        T{    123 V1 ! ->     }T
        T{        V1 @ -> 123 }T
        """
        t.state = LIB.state_VARIABLE

    @staticmethod
    def state_VARIABLE(e, t, c, token):
        t.words[token.lower()] = [t.here]
        t.here += 1
        t.state = e.state_INTERPRET

    @staticmethod  ### ' ###
    def sigil_tick(e, t, c, token, start=False):

        end = token[-1] == "'"
        if end:
            token = token[:-1]
        if start:
            token = token[1:]

        t.stack.append(" ".join(token.split(t.tick_space)))
        t.state = e.state_INTERPRET

    @staticmethod  ### 1+ ###
    def word_1_plus__R_n2(e, t, c, n1):
        return (n1 + 1,)

    @staticmethod  ### 1- ###
    def word_1_m__R_n2(e, t, c, n1):
        return (n1 - 1,)

    @staticmethod  ### 2+ ###
    def word_2_plus__R_n2(e, t, c, n1):
        return (n1 + 2,)

    @staticmethod  ### 2- ###
    def word_2_m__R_n2(e, t, c, n1):
        return (n1 - 2,)

    @staticmethod  ### CELL+ ###
    def word_CELL_plus__R_a2(e, t, c, a1):
        """ """
        return (a1 + 1,)

    @staticmethod  ### ALIGNED ###
    def word_ALIGNED__R_a2(e, t, c, a1):
        """ """
        return (a1,)

    @staticmethod  ### ALIGN ###
    def word_ALIGN__R_a2(e, t, c):
        """ """
        pass

    @staticmethod  ### HERE ###
    def word_HERE__R_a(e, t, c):
        """ """
        return (t.here,)

    @staticmethod  ### CELLS ###
    def word_CELLS__R_n2(e, t, c, n1):
        """
        T{ 1 CELLS 1 <         -> <FALSE> }T
        """
        return (n1,)

    @staticmethod  ### CHARS ###
    def word_CHARS__R_n2(e, t, c, n1):
        """ """
        return (n1,)

    @staticmethod  ### FILL ###
    def word_FILL__R(e, t, c, a, u, ch):
        if u <= 0:
            return

        for i in range(a, a + u):
            t.memory[i] = ch

    @staticmethod  ### MOVE ###
    def word_MOVE__R(e, t, c, a1, a2, u):
        if u <= 0:
            return

        for i in range(a2, a2 + u):
            t.memory[i] = t.memory.get(a1 + i - a2, 0)

    @staticmethod  ### ALLOT ###
    def word_ALLOT__R(e, t, c, n):
        t.here = t.here + n

    @staticmethod  ### C, ###
    def word_C_comma__R(e, t, c, n):
        t.memory[t.here] = n
        t.here += 1

    @staticmethod  ### , ###
    def word_comma__VR(e, t, c):

        struct = c.find_struct(" , ", key=None)
        if struct:
            struct[" , "](e, t, c)
            return

        t.memory[t.here] = t.stack.pop()
        t.here += 1

    @staticmethod  ### ,, ###
    def word_comma_comma__R(e, t, c, x):
        t.memory[t.here] = x
        t.here += 1

    @staticmethod  ### ['] ###
    def word_lbrack_tick_rbrack__IR(e, t, c):
        t.state = LIB.state_lbrack_tick_rbrack

    @staticmethod
    def state_lbrack_tick_rbrack(e, t, c, token):
        token_l = token.lower() if isinstance(token, str) else str
        if token_l in t.words:
            xt = t.words[token_l]
        elif token_l in e.root.words:
            xt = e.root.words[token_l]
        else:
            e.raise_RuntimeError("{token_l}: error (-0): Word Not Found By [']")

        block = c.stack[-1]
        block[block[0]].append(xt)

        t.state = e.state_INTERPRET

    @staticmethod  ### POSTPONE ###
    def word_POSTPONE__IR(e, t, c):
        t.state = LIB.state_POSTPONE

    @staticmethod
    def state_POSTPONE(e, t, c, token):
        token_l = token.lower() if isinstance(token, str) else str

        if token_l in t.words:
            code = t.words[token_l]
            argc = t.word_argc.get(token_l, 0)
        elif token_l in e.root.words:
            code = e.root.words[token_l]
            argc = e.root.word_argc.get(token_l, 0)
        else:
            e.raise_RuntimeError("{token_l}: error (-0): Word Not Found By [']")

        block = c.stack[-1]
        block[block[0]].append((code, argc))

        t.state = LIB.state_COMPILE

    @staticmethod  ### >BODY ###
    def word_rangle_BODY__R_x(e, t, c, x):
        t.stack.append(x[0][0])

    @staticmethod  ### ' ###
    def word_tick__R_x(e, t, c):
        t.state = LIB.state_tick

    @staticmethod
    def state_tick(e, t, c, token):
        token_l = token.lower() if isinstance(token, str) else str

        if token_l in t.words:
            code = t.words[token_l]
            argc = t.word_argc.get(token_l, 0)
        elif token_l in e.root.words:
            code = e.root.words[token_l]
            argc = e.root.word_argc.get(token_l, 0)
        else:
            e.raise_RuntimeError("{token_l}: error (-0): Word Not Found By [']")

        if callable(code):
            t.stack.append((code, argc))
        else:
            t.stack.append(code)

        t.state = e.state_INTERPRET

    @staticmethod  ### FIND ###
    def word_FIND(e, t, c, word):

        if isinstance(word, int):
            parts = []
            for i in range(1, t.memory[word] + 1):
                parts.append(chr(t.memory[word + i]))
            word_l = "".join(parts).lower()
        else:
            word_l = word.lower()

        code = None
        if word_l in t.words:
            code = t.words[word_l]
            argc = t.word_argc.get(word_l, 0)
            immediate = t.word_immediate.get(word_l, False)

        elif word_l in e.root.words:
            code = e.root.words[word_l]
            argc = e.root.word_argc.get(word_l, 0)
            immediate = e.root.word_immediate.get(word_l, False)

        if code:
            flag = 1 if immediate else -1
            if callable(code):
                t.stack.extend([(code, argc), flag])
            else:
                t.stack.extend([code, flag])
            return

        t.stack.extend([word, 0])

    @staticmethod  ### EXECUTE ###
    def word_EXECUTE__R(e, t, c, xt):

        if not isinstance(xt, tuple):
            e.execute_tokens(e, t, c, xt)
            return

        code, argc = xt

        if argc > len(t.stack):
            details = f"{token}: error(-4): Needs {argc} arg(s)"
            raise ForthException(details)

        if argc > 0:
            t.stack, args = t.stack[:-argc], t.stack[-argc:]

        result = code(e, t, c, *args)
        if not result == None:
            if isinstance(result, tuple):
                t.stack.extend(result)
            else:
                t.stack.append(result)

    @staticmethod  ### EX... ###
    def word_EX_dot_dot_dot__R(e, t, c, xt):
        LIB.word_EXECUTE__R(e, t, c, xt)

import copy

__tests_1__ = """

: TEN 10 ;

T{ TEN -> 10 }T

T{ TEN 1 + -> 11 }T

T{ ' TEN execute -> 10 }T

T{ : DOES1 DOES> @ 1 + ; -> }T
T{ : DOES2 DOES> @ 2 + ; -> }T
T{ CREATE CR1 -> }T
T{ CR1   -> HERE }T
T{ 1 ,   ->   }T
T{ CR1 @ -> 1 }T

    """
