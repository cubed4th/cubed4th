#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       _____   _______               _____   _  __
  /\| |/\   / ____| |__   __|     /\      / ____| | |/ /
  \ ` ' /  | (___      | |       /  \    | |      | ' /
 |_     _|  \___ \     | |      / /\ \   | |      |  <
  / , . \   ____) |    | |     / ____ \  | |____  | . \
  \/|_|\/  |_____/     |_|    /_/    \_\  \_____| |_|\_\



)







"""  # __banner__


class LIB:  # { DATA Stack Manipulation : words }
    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### >R ###
    def word_rangle_R__R(e, t, c, x):
        t.rstack.append(x)

    @staticmethod  ### R> ###
    def word_R_rangle__R_x(e, t, c):
        return (t.rstack.pop(),)

    @staticmethod  ### R@ ###
    def word_R_at__R_x(e, t, c):
        return (t.rstack[-1],)

    @staticmethod  ### DEPTH ###
    def word_DEPTH__R_n(e, t, c):
        """
        T{ DEPTH -> 0 }T
        T{ 0 DEPTH -> 0 1 }T
        T{ 0 1 DEPTH -> 0 1 2 }T
        """
        return (len(t.stack),)

    @staticmethod  ### ?DUP ###
    def word_qmark_DUP__R_x_ddd(e, t, c, x):
        """
        T{ 0 ?DUP -> 0 }T
        T{ 1 ?DUP -> 1 1 }T
        T{ -1 ?DUP -> -1 -1 }T
        """
        if x:
            return (x, x)

        return (x,)

    @staticmethod  ### DUP ###
    def word_DUP__R_x_x(e, t, c, x):
        "T{ 1 DUP -> 1 1 }T"
        return (x, x)

    @staticmethod  ### 2DUP ###
    def word_2DUP__R_x1_x2_x1_x2(e, t, c, x1, x2):
        "T{ 1 2 2DUP -> 1 2 1 2 }T"
        return (x1, x2, x1, x2)

    @staticmethod  ### NIP ###
    def word_NIP__R_x2(e, t, c, x1, x2):
        """"""
        return (x2,)

    @staticmethod  ### ROT ###
    def word_ROT__R_x2_x3_x1(e, t, c, x1, x2, x3):
        "T{ 1 2 3 ROT -> 2 3 1 }T"
        return (x2, x3, x1)

    @staticmethod  ### DROP ###
    def word_DROP__R(e, t, c, x):
        # "T{ 1 2 DROP -> 1 }T T{ 0 DROP -> }T"
        return None

    @staticmethod  ### 2DROP ###
    def word_2DROP__R(e, t, c, x1, x2):
        # "T{ 1 2 2DROP -> }T
        return None

    @staticmethod  ### DROP-ALL ###
    def word_DROP_m_ALL__R(e, t, c):
        # "T{ 1 2 DROP:ALL -> }T
        t.stack = []

    @staticmethod  ### OVER ###
    def word_OVER__R_x1_x2_x1(e, t, c, x1, x2):
        "T{ 1 2 OVER -> 1 2 1 }T"
        return (x1, x2, x1)

    @staticmethod  ### 2OVER ###
    def word_2OVER__R_x1_x2_x3_x4_x1_x2(e, t, c, x1, x2, x3, x4):
        "T{ 1 2 3 4 2OVER -> 1 2 3 4 1 2 }T"
        return (x1, x2, x3, x4, x1, x2)

    @staticmethod  ### SWAP ###
    def word_SWAP__R_x2_x1(e, t, c, x1, x2):
        "T{ 1 2 SWAP -> 2 1 }T"
        return (x2, x1)

    @staticmethod  ### 2SWAP ###
    def word_2SWAP__R_x3_x4_x1_x2(e, t, c, x1, x2, x3, x4):
        "T{ 1 2 3 4 2SWAP -> 3 4 1 2 }T"
        return (x3, x4, x1, x2)

    @staticmethod  ### TUCK ###
    def word_TUCK(e, t, c, x1, x2):
        """"""
        return (x2, x1, x2)
