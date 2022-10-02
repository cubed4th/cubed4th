#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (








)









""" # __banner__

from ..FORTH import PRIV

class LIB:  # { Operating System : words }

    """

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### PRIV ###
    def word_PRIV__R_s(e, t, c):
        return (e.priv_level_var.get(),)

    @staticmethod  ### )ACL: ###
    def sigil_rparen_ACL_colon(e, t, c, token, start=False):

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

        if struct["."] in ["ring"]:
            with PRIV(args[0]):
                e.execute_tokens(e, t, c, [token[5:]])

