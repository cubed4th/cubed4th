#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _           _    _____    ____    _   _
  /\| |/\       | |  / ____|  / __ \  | \ | |
  \ ` ' /       | | | (___   | |  | | |  \| |
 |_     _|  _   | |  \___ \  | |  | | | . ` |
  / , . \  | |__| |  ____) | | |__| | | |\  |
  \/|_|\/   \____/  |_____/   \____/  |_| \_|



)





"""  # __banner__


class LIB:  # { JavaScript Object Notation : words }

    """

    T{ ("Hello World") -> 'Hello ''World + }T

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### ARROW ###
    def word_ARROW__R_x(e, t, c):
        import arrow

        return (arrow.now(),)

    @staticmethod  ### ULID ###
    def word_ULID__R_x(e, t, c):
        import ulid

        return (ulid.ULID(),)

    @staticmethod  ### ([ ###
    def sigil_lparen_lbrack(e, t, c, token, *args, **kwargs):
        e.JSON.state_JSON(e, t, c, token, *args, **kwargs)

    @staticmethod  ### ({ ###
    def sigil_lparen_lbrace(e, t, c, token, *args, **kwargs):
        e.JSON.state_JSON(e, t, c, token, *args, **kwargs)

    @staticmethod  ### (( ###
    def sigil_lparen_lparen(e, t, c, token, *args, **kwargs):
        e.JSON.state_JSON(e, t, c, token, *args, **kwargs)

    @staticmethod  ### (" ###
    def sigil_lparen_quote(e, t, c, token, *args, **kwargs):
        e.JSON.state_JSON(e, t, c, token, *args, **kwargs)

    @staticmethod
    def state_JSON(e, t, c, token, start=False):
        end = token[-1] == ")"
        if end:
            token = token[:-1]
        if not t.state == e.JSON.state_JSON:
            mode = token[1]
            c.stack.append({"JSON": [], "MODE": mode})
            token = token[1:]
            if mode == "(":
                token = token[1:]

        block = c.stack[-1]

        if block["MODE"] == "(":
            if end:
                token = token[:-1]

        block["JSON"].append(token)

        if end:
            c.stack.pop()
            json = " ".join(block["JSON"])

            def h(values):
                if "__complex__" in values:
                    return complex(values["real"], values["imag"])
                return values

            import simplejson

            json = simplejson.loads(json, use_decimal=True, object_hook=h)
            t.stack.append(json)
            t.state = e.state_INTERPRET
            return

        t.state = e.JSON.state_JSON

    @staticmethod  ### JSON-SAVE ###
    def word_JSON_minus_SAVE__R_s(e, t, c, x):
        def encode(_):
            if isinstance(_, complex):
                return {"__complex__": True, "real": _.real, "imag": _.imag}
            raise TypeError(repr(_) + " is not JSON serializable")

        import simplejson

        return (
            x,
            simplejson.dumps(x, default=encode),
        )

    @staticmethod  ### JSON-LOAD ###
    def word_JSON_minus_LOAD__R_x(e, t, c, s):
        def h(_):
            if "__complex__" in _:
                return complex(_["real"], _["imag"])
            return _

        import simplejson

        return (simplejson.loads(s, use_decimal=True, object_hook=h),)
