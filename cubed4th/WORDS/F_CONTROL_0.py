#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       _____    ____    _   _   _______   _____     ____    _
  /\| |/\   / ____|  / __ \  | \ | | |__   __| |  __ \   / __ \  | |
  \ ` ' /  | |      | |  | | |  \| |    | |    | |__) | | |  | | | |
 |_     _| | |      | |  | | | . ` |    | |    |  _  /  | |  | | | |
  / , . \  | |____  | |__| | | |\  |    | |    | | \ \  | |__| | | |____
  \/|_|\/   \_____|  \____/  |_| \_|    |_|    |_|  \_\  \____/  |______|



)







"""  # __banner__


class LIB:  # { Control Flow : words }

    """

    T{  0 IF 123 THEN ->     }T
    T{ -1 IF 123 THEN -> 123 }T
    T{  1 IF 123 THEN -> 123 }T
    T{ -1 IF 123 THEN -> 123 }T
    T{  0 IF 123 ELSE 234 THEN -> 234 }T
    T{  1 IF 123 ELSE 234 THEN -> 123 }T

    : TEST1 IF 123 ELSE EXIT THEN 345 ;

    T{ 0 TEST1 -> }T
    T{ 1 TEST1 -> 123 345 }T

    # T{ : GD3 DO 1 0 DO J LOOP LOOP ; -> }T
    # T{          4        1 GD3 ->  1 2 3   }T

    : GD1 DO I LOOP ;

    T{ 5 1 GD1 -> 1 2 3 4 }T

    T{ 6 2 GD1 -> 2 3 4 5 }T

    """

    def __init__(self, e, t, **kwargs):
        pass

    #@staticmethod  ### EXIT ###
    #def word_EXIT__R(e, t, c):
    #    c.EXIT = True

    @staticmethod  ### STOP ###
    def word_STOP__R(e, t, c):
        c.EXIT = True
        p = c.parent
        while p:
            p.EXIT = True
            p = p.parent

    @staticmethod  ### V ###
    def word_V__2R_x(e, t, c):
        call = c
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "v" in call.stack[index]:
                    return (call.stack[index]["v"],)
            call = call.parent
        e.raise_RuntimeError("V: error (-0): Illegal Outside 'Object' DO")

    @staticmethod  ### V^ ###
    def word_V_carat__R_x(e, t, c):
        call = c
        outer = False
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "v" in call.stack[index]:
                    if not outer:
                        outer = True
                    else:
                        return (call.stack[index]["v"],)
            call = call.parent
        e.raise_RuntimeError("V^: error (-0): Illegal Outside 'Object' DO DO")

    @staticmethod  ### K ###
    def word_K__R_x(e, t, c):
        call = c
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "k" in call.stack[index]:
                    return (call.stack[index]["k"],)
            call = call.parent
        e.raise_RuntimeError("K: error (-0): Illegal Outside Object DO")

    @staticmethod  ### K^ ###
    def word_K_carat__R_x(e, t, c):
        call = c
        outer = False
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "k" in call.stack[index]:
                    if not outer:
                        outer = True
                    else:
                        return (call.stack[index]["k"],)
            call = call.parent
        e.raise_RuntimeError("K^: error (-0): Illegal Outside Object DO DO")

    @staticmethod  ### I ###
    def word_I__R_n(e, t, c):
        call = c
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "i2" in call.stack[index]:
                    return (call.stack[index]["i2"],)
            call = call.parent
        e.raise_RuntimeError("I: error (-0): Illegal Outside DO")

    @staticmethod  ### J ###
    def word_J__R_n(e, t, c):
        call = c
        outer = False
        while call:
            for index in range(-1, (len(call.stack) * -1) - 1, -1):
                if "i2" in call.stack[index]:
                    if not outer:
                        outer = True
                    else:
                        return (call.stack[index]["i2"],)
            call = call.parent
        e.raise_RuntimeError("J: error (-0): Illegal Outside DO DO")

    @staticmethod  ### DO ###
    def word_DO__R(e, t, c):
        struct = {"?": "DO", 0: 0, 1: [], "r": t.state}
        c.stack.append(struct)

        tos = t.stack.pop()
        if isinstance(tos, list) or isinstance(tos, dict):
            struct["iter"] = tos
        else:
            struct["i2"] = tos
            struct["i1"] = t.stack.pop()

        t.state = LIB.state_DO

    @staticmethod
    def state_DO(e, t, c, token):
        struct = c.stack[-1]
        assert struct["?"] == "DO"

        token_l = token.lower() if isinstance(token, str) else token

        if token_l == "loop" or token_l == "+loop":
            if struct[0] == 0:
                return LIB.impl_DO(e, t, c, token_l, struct)
            struct[0] -= 1

        if token_l == "do":
            struct[0] += 1

        is_number, value = e.to_number(e, t, c, token)
        if is_number:
            struct[1].append((value,))
        else:
            struct[1].append(token)

    @staticmethod
    def impl_DO(e, t, c, token_l, struct):

        t.state = e.state_INTERPRET

        if "iter" in struct:
            if token_l == "+loop":
                e.raise_RuntimeError("+loop: error(-0): Only Valid on Integer Loops")

            iter = struct["iter"]
            if isinstance(iter, list):
                for v in iter:
                    struct["v"] = v
                    e.execute_tokens(e, t, c, struct[1])

            if isinstance(iter, dict):
                for k in sorted(iter):
                    struct["k"] = k
                    struct["v"] = iter[k]
                    e.execute_tokens(e, t, c, struct[1])

        else:

            struct[0] = True

            if token_l == "loop":
                while struct[0] and struct["i2"] < struct["i1"]:
                    e.execute_tokens(e, t, c, struct[1])
                    struct["i2"] += 1

            elif token_l == "+loop":
                while struct[0]:
                    e.execute_tokens(e, t, c, struct[1])
                    struct["i2"] += t.stack.pop()
                    if struct["i2"] < struct["i1"]:
                        break

        c.stack.pop()
        t.state = struct["r"]

    @staticmethod  ### LEAVE ###
    def word_LEAVE(e, t, c):
        c.stack[-1][0] = False

    @staticmethod  ### BEGIN ###
    def word_BEGIN(e, t, c):
        c.stack.append({"?": "BEGIN", 0: 1, 1: [], "r": t.state})
        t.state = LIB.state_BEGIN

    @staticmethod
    def state_BEGIN(e, t, c, token):
        struct = c.stack[-1]
        assert struct["?"] == "BEGIN"

        token_l = token.lower() if isinstance(token, str) else token
        if token_l == "until" or token_l == "repeat":
            return LIB.impl_BEGIN(e, t, c)

        if token_l == "while":
            struct[0] = 2
            struct[2] = []
            return

        struct[struct[0]].append(token)

    @staticmethod
    def impl_BEGIN(e, t, c):
        struct = c.stack.pop()

        t.state = e.state_INTERPRET

        if struct[0] == 1:
            while True:
                e.execute_tokens(e, t, c, struct[1])
                b = t.stack.pop()
                if b:
                    break

        if struct[0] == 2:
            while True:
                e.execute_tokens(e, t, c, struct[1])
                b = t.stack.pop()
                if not b:
                    break
                e.execute_tokens(e, t, c, struct[2])

        t.state = struct["r"]

    @staticmethod  ### REPEAT ###
    def word_REPEAT__R(e, t, c):
        e.raise_SyntaxError("REPEAT: error(-0): No BEGIN")

    @staticmethod  ### UNTIL ###
    def word_UNTIL__R(e, t, c):
        e.raise_SyntaxError("UNTIL: error(-0): No BEGIN")

    @staticmethod  ### WHILE ###
    def word_WHILE__R(e, t, c):
        e.raise_SyntaxError("WHILE: error(-0): No BEGIN")

    @staticmethod
    def impl_IF(e, t, c):
        t.state = e.state_INTERPRET

        block = c.stack.pop()
        if block["b"]:
            e.execute_tokens(e, t, c, block[1])
        else:
            e.execute_tokens(e, t, c, block[0])

        t.state = block["r"]



    @staticmethod  ### IF ###
    def word_IF__R(e, t, c, b):
        c.stack.append({"?": "IF", "b": b, 0: [], 1: [], "r": t.state})
        t.state = LIB.state_IF_TRUE

    @staticmethod
    def state_IF_TRUE(e, t, c, token):
        token_l = token.lower() if isinstance(token, str) else token

        if token_l == "else":
            t.state = LIB.state_IF_FALSE
            return

        if token_l == "end_if" or token_l == "then":
            LIB.impl_IF(e, t, c)
            return

        c.stack[-1][1].append(token)

    @staticmethod  ### ELSE ###
    def word_ELSE__R(e, t, c, token):
        t.state = LIB.state_IF_FALSE

    @staticmethod
    def state_IF_FALSE(e, t, c, token):
        token_l = token.lower() if isinstance(token, str) else token

        if token_l == "else":
            t.state = LIB.IF_TRUE
            return

        if token_l == "end_if" or token_l == "then":
            LIB.impl_IF(e, t, c)
            return

        c.stack[-1][0].append(token)
