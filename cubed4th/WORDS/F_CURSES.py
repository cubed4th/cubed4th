#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       _____   _    _   _____     _____   ______    _____
  /\| |/\   / ____| | |  | | |  __ \   / ____| |  ____|  / ____|
  \ ` ' /  | |      | |  | | | |__) | | (___   | |__    | (___
 |_     _| | |      | |  | | |  _  /   \___ \  |  __|    \___ \
  / , . \  | |____  | |__| | | | \ \   ____) | | |____   ____) |
  \/|_|\/   \_____|  \____/  |_|  \_\ |_____/  |______| |_____/



)







"""  # __banner__


class LIB:  # { CURSES Text Interface : words }

    """

    ( in F_CURSES )

    # T{ -> }T

    """

    def __init__(self, e, t, **kwargs):
        self.stdscr = None
        if "stdscr" in kwargs:
            self.stdscr = kwargs["stdscr"]

    @staticmethod  ### CURSES ###
    def word_CURSES(e, t, c):
        import curses

    @staticmethod  ### KEY-MAP ###
    def word_KEY_m_MAP__R_x(e, t, c):
        return (KEY_MAP,)

    @staticmethod  ### WINDOW ###
    def word_WINDOW__R_x(e, t, c, n1, n2, n3, n4):
        global scr
        x = scr.newwin(n3, n4, n1, n2)
        return (x,)

    @staticmethod  ### BORDER ###
    def word_BORDER__R_x(e, t, c, x):
        x.border()
        return (x,)

    @staticmethod  ### REFRESH ###
    def word_REFRESH__R_x(e, t, c, x):
        x.refresh()
        return (x,)

    @staticmethod  ### BACKGROUND ###
    def word_BACKGROUND__R_x1(e, t, c, x1, s, x2):
        if not isinstance(x2, string):
            x2 = tuple(x2)
        x1.background(s, x2)
        return (x1,)

    @staticmethod  ### GETKEY ###
    def word_GETKEY__R_x_s(e, t, c, x):
        k = x.getch()
        return (x, k)

    @staticmethod  ### WRITE ###
    def word_WRITE__R_x(e, t, c, x, s, n1, n2):
        x.write(s, (n1, n2))
        return x

    @staticmethod  ### WRITEC ###
    def word_WRITEC__R_x1(e, t, c, x1, s, n1, n2, x2):
        if not isinstance(x2, str):
            x2 = tuple(x)
        x1.write(s, (n1, n2), color=x2)
        return (x1, win1.getkey())

    @staticmethod  ### Z ###
    def word_Z(e, t, c):

        from ezcurses import Cursed

        with Cursed() as scr:
            win1 = scr.new_win(orig=(0, 0), size=(80, 20))
            win2 = scr.new_win(orig=(0, 20), size=(80, 4))
            win3 = scr.new_win(orig=(0, 24), size=(80, 1))
            win1.border()
            win2.border()
            win1.background("+", color="red")
            win2.background(".", color=("green", "blue"))
            win3.background(" ", color=("green", "red"))
            win1.refresh()
            win2.refresh()
            win3.refresh()
            s = win3.getstr((0, 0), echo=True)
            win2.write(s, (1, 1), color=("red", "black"))
            win2.refresh()
            win1.write("Press q to quit", (1, 1), color=("black", "red"))
            while win1.getkey() != "q":
                pass


#
# Linage:
#
#   https://github.com/richrd/suplemon/blob/master/suplemon/key_mappings.py
#


def get_KEY_MAP(curse):
    return {
        # Single keys
        curses.KEY_F1: "f1",  # 265
        curses.KEY_F2: "f2",  # 266
        curses.KEY_F3: "f3",  # 267
        curses.KEY_F4: "f4",  # 268
        curses.KEY_F5: "f5",  # 269
        curses.KEY_F6: "f6",  # 270
        curses.KEY_F7: "f7",  # 271
        curses.KEY_F8: "f8",  # 272
        curses.KEY_F9: "f9",  # 273
        curses.KEY_F10: "f10",  # 274
        curses.KEY_F11: "f11",  # 275
        curses.KEY_F12: "f12",  # 276
        "KEY_F(1)": "f1",
        "KEY_F(2)": "f2",
        "KEY_F(3)": "f3",
        "KEY_F(4)": "f4",
        "KEY_F(5)": "f5",
        "KEY_F(6)": "f6",
        "KEY_F(7)": "f7",
        "KEY_F(8)": "f8",
        "KEY_F(9)": "f9",
        "KEY_F(10)": "f10",
        "KEY_F(11)": "f11",
        "KEY_F(12)": "f12",
        curses.KEY_UP: "up",
        curses.KEY_DOWN: "down",
        curses.KEY_LEFT: "left",
        curses.KEY_RIGHT: "right",
        "KEY_UP": "up",
        "KEY_DOWN": "down",
        "KEY_LEFT": "left",
        "KEY_RIGHT": "right",
        curses.KEY_ENTER: "enter",
        "KEY_ENTER": "enter",
        "\n": "enter",
        "^J": "enter",
        "^M": "enter",
        343: "shift+enter",
        curses.KEY_BACKSPACE: "backspace",
        "KEY_BACKSPACE": "backspace",
        "^?": "backspace",
        "^H": "backspace",  # on Windows
        curses.KEY_DC: "delete",
        curses.KEY_HOME: "home",
        curses.KEY_END: "end",
        curses.KEY_PPAGE: "pageup",
        curses.KEY_NPAGE: "pagedown",
        "KEY_DC": "delete",
        "KEY_HOME": "home",
        "KEY_END": "end",
        "KEY_PPAGE": "pageup",
        "KEY_NPAGE": "pagedown",
        curses.KEY_IC: "insert",
        "KEY_IC": "insert",
        331: "insert",
        "\t": "tab",
        "^I": "tab",
        "^[": "escape",
        # Control
        "^A": "ctrl+a",
        "^B": "ctrl+b",
        "^C": "ctrl+c",
        "^D": "ctrl+d",
        "^E": "ctrl+e",
        "^F": "ctrl+f",
        "^G": "ctrl+g",
        # "^H": "ctrl+h",  # Conflicts with 'backspace' on Windows
        # "^I": "ctrl+i",  # Conflicts with 'tab'
        # "^J": "ctrl+j",  # Conflicts with 'enter'
        "^K": "ctrl+k",
        "^L": "ctrl+l",
        # "^M": "ctrl+m",  # Conflicts with 'enter'
        "^N": "ctrl+n",
        "^O": "ctrl+o",
        "^P": "ctrl+p",
        "^Q": "ctrl+q",
        "^R": "ctrl+r",
        "^S": "ctrl+s",
        "^T": "ctrl+t",
        "^U": "ctrl+u",
        "^V": "ctrl+v",
        "^W": "ctrl+w",
        "^X": "ctrl+x",
        "^Y": "ctrl+y",
        "^Z": "ctrl+z",  # Conflicts with suspend
        "CTL_LEFT": "ctrl+left",
        "CTL_RIGHT": "ctrl+right",
        544: "ctrl+left",
        559: "ctrl+right",
        565: "ctrl+up",
        524: "ctrl+down",
        "kLFT5": "ctrl+left",
        "kRIT5": "ctrl+right",
        "kUP5": "ctrl+up",
        "kDN5": "ctrl+down",
        "kIC5": "ctrl+insert",
        "kDC5": "ctrl+delete",
        "kHOM5": "ctrl+home",
        "kEND5": "ctrl+end",
        554: "ctrl+pageup",
        549: "ctrl+pagedown",
        "kNXT5": "ctrl+pageup",
        "kPRV5": "ctrl+pagedown",
        "O5P": "ctrl+f1",
        "O5Q": "ctrl+f2",
        "O5R": "ctrl+f3",
        "O5S": "ctrl+f4",
        "KEY_F(29)": "ctrl+f5",
        "KEY_F(30)": "ctrl+f6",
        "KEY_F(31)": "ctrl+f7",
        "KEY_F(32)": "ctrl+f8",
        "KEY_F(33)": "ctrl+f9",
        "KEY_F(34)": "ctrl+f10",
        "KEY_F(35)": "ctrl+f11",
        "KEY_F(36)": "ctrl+f12",
        # Alt
        563: "alt+up",
        522: "alt+down",
        542: "alt+left",
        557: "alt+right",
        "kUP3": "alt+up",
        "kDN3": "alt+down",
        "kLFT3": "alt+left",
        "kRIT3": "alt+right",
        "kIC3": "alt+insert",
        "kDC3": "alt+delete",
        "kHOM3": "alt+home",
        "kEND3": "alt+end",
        552: "alt+pageup",
        547: "alt+pagedown",
        "kPRV3": "alt+pageup",
        "kNXT3": "alt+pagedown",
        "KEY_F(53)": "alt+f5",
        "KEY_F(54)": "alt+f6",
        "KEY_F(55)": "alt+f7",
        "KEY_F(56)": "alt+f8",
        "KEY_F(57)": "alt+f9",
        "KEY_F(58)": "alt+f10",
        "KEY_F(59)": "alt+f11",
        "KEY_F(60)": "alt+f12",
        # Shift
        curses.KEY_SLEFT: "shift+left",
        curses.KEY_SRIGHT: "shift+right",
        "KEY_SLEFT": "shift+left",
        "KEY_SRIGHT": "shift+right",
        "KEY_SR": "shift+up",
        "KEY_SF": "shift+down",
        "KEY_SUP": "shift+up",
        "KEY_SDOWN": "shift+down",
        353: "shift+tab",
        "KEY_BTAB": "shift+tab",
        "KEY_SDC": "shift+delete",
        "KEY_SHOME": "shift+home",
        "KEY_SEND": "shift+end",
        "KEY_SPREVIOUS": "shift+pageup",
        "KEY_SNEXT": "shift+pagedown",
        "O2P": "shift+f1",
        "O2Q": "shift+f2",
        "O2R": "shift+f3",
        "O2S": "shift+f4",
        "KEY_F(17)": "shift+f5",
        "KEY_F(18)": "shift+f6",
        "KEY_F(19)": "shift+f7",
        "KEY_F(20)": "shift+f8",
        "KEY_F(21)": "shift+f9",
        "KEY_F(22)": "shift+f10",
        "KEY_F(23)": "shift+f11",
        "KEY_F(24)": "shift+f12",
        # Alt Gr
        "O1P": "altgr+f1",
        "O1Q": "altgr+f2",
        "O1R": "altgr+f3",
        "O1S": "altgr+f4",
        # Shift + Alt
        "kUP4": "shift+alt+up",
        "kDN4": "shift+alt+down",
        "kLFT4": "shift+alt+left",
        "kRIT4": "shift+alt+right",
        "kIC4": "shift+alt+inset",
        "kDC4": "shift+alt+delete",
        "kHOM4": "shift+alt+home",
        "kEND4": "shift+alt+end",
        # Control + Shift
        "kUP6": "ctrl+shift+up",
        "kDN6": "ctrl+shift+down",
        "kLFT6": "ctrl+shift+left",
        "kRIT6": "ctrl+shift+right",
        "kDC6": "ctrl+shift+delete",
        "kHOM6": "ctrl+shift+home",
        "kEND6": "ctrl+shift+end",
        # Control + Alt
        "kUP7": "ctrl+alt+up",
        "kDN7": "ctrl+alt+down",
        "kLFT7": "ctrl+alt+left",
        "kRIT7": "ctrl+alt+right",
        "kPRV7": "ctrl+alt+pageup",
        "kNXT7": "ctrl+alt+pagedown",
        "kIC7": "ctrl+alt+insert",
        "kDC7": "ctrl+alt+delete",
        "kHOM7": "ctrl+alt+home",
        "kEND7": "ctrl+alt+end",
        # Special events
        "KEY_RESIZE": "resize",
    }
