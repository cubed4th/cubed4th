#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (








)









""" # __banner__


class LIB:  # { Operating System : words }

    """

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### Q-NEW ###
    def word_Q_m_NEW__R_x(e, t, c):
        from queue import Queue
        return (Queue(),)

    @staticmethod  ### }Q-NEW ###
    def word_rbrace_Q_m_NEW__R_x(e, t, c, d):
        from queue import Queue
        return (Queue(**d),)

    @staticmethod  ### Q-PUT ###
    def word_Q_m_PUT__R(e, t, c, x1, x2):
        x1.put(x2)

    @staticmethod  ### Q-PUT-NOBLOCK ###
    def word_Q_m_PUT_m_NOBLOCK__R_b(e, t, c, x1, x2):
        full = False
        try:
            entry = x1.put(x2, block=False)
        except queue.Full:
            full = True
        return (full,)

    @staticmethod  ### Q-GET ###
    def word_Q_m_GET__R_x2(e, t, c, x1):
        return (x1.get(),)

    @staticmethod  ### Q-GET-NOBLOCK ###
    def word_Q_m_GET_m_NOBLOCK__R_x2_b(e, t, c, x1):
        empty = False
        entry = None
        try:
            entry = x1.get(block=False)
        except queue.Empty:
            empty = True
        return (entry,empty)

    @staticmethod  ### Q-GET-TIMEOUT ###
    def word_Q_m_GET_m_TIMEOUT__R_x2_b(e, t, c, x1, n1):
        empty = False
        entry = None
        try:
            entry = x1.get(timeout=n1)
        except queue.Empty:
            empty = True
        return (entry,empty)





