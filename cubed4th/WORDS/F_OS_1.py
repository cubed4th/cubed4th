#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (








)









""" # __banner__

from ..FORTH import RING_CHANGE

class LIB:  # { Operating System : words }

    """

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### RING ###
    def word_RING__R_s(e, t, c):
        return (e.this_ring_var.get(),)

    @staticmethod  ### )CPU: ###
    def sigil_rparen_CPU_colon(e, t, c, token, start=False):

        struct = c.stack.pop()
        assert struct["?"] == "()"

        args = t.stack[struct["d"]:]
        t.stack = t.stack[:struct["d"]]

        program = struct["."]
        if program == "":
            struct["."] = t.stack.pop()
        if isinstance(program, str):
            program = [program]

        command = token[5:].lower()
        if command == "ring":
            with RING_CHANGE(int(args[0])):
                e.execute_tokens(e, t, c, program)
            return

        if len(args) > 0:
            kwargs = args[-1]
            args = args[:-1]
        else:
            kwargs = {}


