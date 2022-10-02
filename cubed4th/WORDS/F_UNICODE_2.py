#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _    _   _   _   _____    _____    ____    _____    ______
  /\| |/\  | |  | | | \ | | |_   _|  / ____|  / __ \  |  __ \  |  ____|
  \ ` ' /  | |  | | |  \| |   | |   | |      | |  | | | |  | | | |__
 |_     _| | |  | | | . ` |   | |   | |      | |  | | | |  | | |  __|
  / , . \  | |__| | | |\  |  _| |_  | |____  | |__| | | |__| | | |____
  \/|_|\/   \____/  |_| \_| |_____|  \_____|  \____/  |_____/  |______|



)







"""  # __banner__


class LIB:  # { UNICODE Support : words }

    """

    T{ 'Hello'World -> 'Hello'World }T
    T{ 'Goodbye ''World + -> 'Goodbye ''World + }T

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### . ###
    def word_FORMAT__R_s2(e, t, c, x, s1):
        if isinstance(x, dict):
            return (s1.format(**x),)

        if isinstance(x, list):
            return (s1.format(*tuple(x)),)

        args = []
        argc = int(x)
        while argc:
            args.append(t.stack.pop())
            argc -= 1
        args.reverse()
        return (s1.format(*tuple(args)),)

    @staticmethod  ### . ###
    def word_FIGLET__R_s2(e, t, c, s1):
        from pyfiglet import Figlet

        f = Figlet(font="big")

        lines = []
        for line in f.renderText(s1).split("\n"):
            lines.append(" " + line)

        s2 = "\n".join(lines)

        print(f"{s2}")

    @staticmethod  ### FIGLET1 ###
    def word_FIGLET1__R_s2(e, t, c, s1):
        return LIB.word_FIGLET__R_s2(e, t, c, " ".join(list(s1)))

    @staticmethod  ### FIGLET2 ###
    def word_FIGLET2__R_s2(e, t, c, s1):
        return LIB.word_FIGLET__R_s2(e, t, c, "  ".join(list(s1)))
