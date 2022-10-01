#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _____   _   _   _____    _    _   _______
  /\| |/\  |_   _| | \ | | |  __ \  | |  | | |__   __|
  \ ` ' /    | |   |  \| | | |__) | | |  | |    | |
 |_     _|   | |   | . ` | |  ___/  | |  | |    | |
  / , . \   _| |_  | |\  | | |      | |__| |    | |
  \/|_|\/  |_____| |_| \_| |_|       \____/     |_|



)







"""  # __banner__


class LIB:  # { Input / Output : words }

    """ """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod ### READ-LINES ###
    def word_READ_m_LINES__R_l(e, t, c, s):
        result = []
        with open(s, 'rt') as f:
            for l in f.readlines():
                l = l.strip()
                if not l == '':
                    result.append(l)
        return (result,)

    @staticmethod ### LOAD-FILE ###
    def word_LOAD_m_FILE__R(e, t, c, s):
        with open(s, 'rt') as f:
            lines = f.readlines()
            e.execute(lines)

