#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       ____    _    _   _______   _____    _    _   _______
  /\| |/\   / __ \  | |  | | |__   __| |  __ \  | |  | | |__   __|
  \ ` ' /  | |  | | | |  | |    | |    | |__) | | |  | |    | |
 |_     _| | |  | | | |  | |    | |    |  ___/  | |  | |    | |
  / , . \  | |__| | | |__| |    | |    | |      | |__| |    | |
  \/|_|\/   \____/   \____/     |_|    |_|       \____/     |_|



)







"""  # __banner__


class LIB:  # { Input / Output : words }

    """ """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### PRINT ###
    def word_PRINT__R(e, t, c, x):
        print(x, end="")

    @staticmethod  ### CR ###
    def word_CR__R(e, t, c):
        print()

    @staticmethod  ### EMIT ###
    def word_EMIT__R(e, t, c, x):
        print(chr(x), end="")
