#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _____    _____     _____
  /\| |/\  |  __ \  |  __ \   / ____|
  \ ` ' /  | |  | | | |__) | | |  __
 |_     _| | |  | | |  ___/  | | |_ |
  / , . \  | |__| | | |      | |__| |
  \/|_|\/  |_____/  |_|       \_____|

)









""" # __banner__


class LIB:  # { JavaScript Object Notation : words }

    """

    T{ ("Hello World") -> 'Hello ''World + }T

    """

    tag_next = 1000
    win_engine = None

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### DPG-TAG ###
    def word_DPG_m_TAG__R_n(e, t, c):
        return (LIB.tag_next,)

    @staticmethod  ### ++DPG-TAG ###
    def word_plus_plus_DPG_m_TAG__R_n(e, t, c):
        LIB.tag_next += 1
        return (LIB.tag_next,)

    @staticmethod  ### DPG. ###
    def sigil_DPG_dot(e, t, c, token, start=False):
        name = token[4:]
        import dearpygui.dearpygui as dpg
        t.stack.append(getattr(dpg,name))

    @staticmethod  ### )DPG ###
    def sigil_rparen_DPG(e, t, c, token, start=False):

        do_result = False
        if token[-1] == '?':
            do_result = True
            token = token[:-1]

        struct = c.stack.pop()
        assert struct["?"] == "()"

        args = t.stack[struct["d"]:]
        args.extend(tuple(struct.get("*",[])))
        t.stack = t.stack[:struct["d"]]

        if len(args) > 0 and isinstance(args[-1], dict):
            kwargs = args[-1]
            args = args[:-1]
        else:
            kwargs = {}

        if struct["."] == "":
            struct["."] = args[0]
            args = args[1:]

        parts = struct["."].split("_")

        if parts[0] == "add" and parts[-1] == "handler" and "callback" in kwargs:
            command = kwargs["callback"]
            def callback(sender, app_data, user_data):
                user_data.execute(command, include=True)
            kwargs["callback"] = callback

        import dearpygui.dearpygui as dpg
        code = getattr(dpg, struct["."])

        if "tag" in code.__annotations__:
            if not "tag" in kwargs:
                import ulid
                kwargs["tag"] = str(ulid.ULID())[:-4] + '0DPG'

        if "user_data" in code.__annotations__:
            kwargs["user_data"] = e

        result = code(*args, **kwargs)

        if do_result:
            t.stack.append(result)


    @staticmethod  ### )DPG: ###
    def sigil_rparen_DPG_colon(e, t, c, token, start=False):

        token = token[5:]

        return_result = False
        if token[-1] == '?':
            return_result = True
            token = token[:-1]

        struct = c.stack.pop()
        assert struct["?"] == "()"

        args = t.stack[struct["d"]:]
        args.extend(tuple(struct.get("*",[])))
        t.stack = t.stack[:struct["d"]]

        kwargs = {}
        if len(args) > 0 and isinstance(args[-1], dict):
            kwargs = args[-1]
            args = args[:-1]

        if struct["."] == "":
            struct["."] = args[0]
            args = args[1:]
        elif struct["."] == "-":
            struct["."] = t.stack.pop()

        import dearpygui.dearpygui as dpg
        code = getattr(dpg, token)

        if "tag" in code.__annotations__:
            if not "tag" in kwargs:
                import ulid
                kwargs["tag"] = str(ulid.ULID())[:-4] + '0DPG'

        if "user_data" in code.__annotations__:
            kwargs["user_data"] = e

        with code(*args, **kwargs) as result:
            e.execute_tokens(e, t, c, [struct["."]])

        if return_result:
            t.stack.append(result)


