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

        if len(args) > 0:
            kwargs = args[-1]
            args = args[:-1]
        else:
            kwargs = {}
            args = ()

        kwargs["user_data"] = e

        import ulid
        kwargs["tag"] = str(ulid.ULID())[:-4] + '0DPG'

        import dearpygui.dearpygui as dpg
        code = getattr(dpg, struct["."])
        result = code(*args, **kwargs)
        if do_result:
            t.stack.append(result)


    @staticmethod  ### )DPG: ###
    def sigil_rparen_DPG_colon(e, t, c, token, start=False):

        struct = c.stack.pop()
        assert struct["?"] == "()"

        args = t.stack[struct["d"]:]
        args.extend(tuple(struct.get("*",[])))
        t.stack = t.stack[:struct["d"]]

        if len(args) > 0:
            kwargs = args[-1]
            args = args[:-1]
        else:
            kwargs = {}
            args = ()

        import ulid
        kwargs["tag"] = str(ulid.ULID())[:-4] + '0DPG'

        if struct["."] in ["window"]:
            kwargs["user_data"] = e
            e.root.memory["window_tag"] = kwargs["tag"]

        import dearpygui.dearpygui as dpg
        code = getattr(dpg, struct["."])
        with code(*args, **kwargs) as obj:
            e.execute_tokens(e, t, c, [token[5:]])

