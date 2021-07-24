#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneInter.net

__banner__ = r""" ( This string is also the module initilizer program.

     _      _____    ______   _____    _
  /\| |/\  |  __ \  |  ____| |  __ \  | |
  \ ` ' /  | |__) | | |__    | |__) | | |
 |_     _| |  _  /  |  __|   |  ___/  | |
  / , . \  | | \ \  | |____  | |      | |____
  \/|_|\/  |_|  \_\ |______| |_|      |______|



)





"""  # __banner__


class LIB:  # { By the Power of Introspection : words }
    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### . ###
    def word_dot__R(e, t, c, x):
        print(f"{x} ", end="")

    @staticmethod  ### IC ###
    def word_IC__R(e, t, c, x):
        ic(x)

    @staticmethod  ### .S ###
    def word_dot_S__R_x(e, t, c, x):
        print(f" {x}")
        return (x,)

    @staticmethod  ### WORDS ###
    def word_WORDS(e, t, c):
        words = {}
        for name in e.root.words.keys():
            words[name] = True
        for name in t.words.keys():
            words[name] = True
        for name in e.root.sigils.keys():
            words[name] = True
        for name in t.sigils.keys():
            words[name] = True
        words = sorted(words)
        print(" ".join(words))

    @staticmethod  ### SEE ###
    def word_SEE(e, t, c):
        t.state = e.REPL.state_SEE

    @staticmethod
    def state_SEE(e, t, c, token):
        import dis

        word = t.words.get(token.lower(), None)
        if not word:
            e.root.words.get(token.lower(), None)
        if callable(word):
            dis.show_code(word)
            dis.dis(word)
        else:
            print(word)
        t.state = e.state_INTERPRET

    @staticmethod  ### DIR ###
    def word_DIR__R_x(e, t, c, x):
        d = []
        for k in dir(x):
            if not k[0] == "_":
                d.append(k)
        print(str(d))
        return (x,)

    @staticmethod  ### DIR:ALL ###
    def word_DIR_colon_ALL__R_x(e, t, c, x):
        print(str(dir(x)))
        return (x,)

    @staticmethod  ### MEM ###
    def word_MEM(e, t, c):
        print(str(e.root.memory))
        if not t.is_root:
            print(str(t.memory))

    @staticmethod  ### SEE:ALL ###
    def word_SEE_colon_ALL(e, t, c):
        show = {}
        for name in e.root.words:
            if not callable(e.root.words[name]):
                show[name] = e.root.words[name]
        for name in t.words:
            if not callable(t.words[name]):
                show[name] = t.words[name]
        print(str(show))

    @staticmethod  ### SEE:ALL+ ###
    def word_SEE_colon_ALL_plus(e, t, c):
        show = {}
        for name in e.root.words:
            if not callable(e.root.words[name]):
                show[name] = e.root.words[name]
            else:
                show[name] = e.root.word_argc.get(name, 0)
        for name in t.words:
            if not callable(t.words[name]):
                show[name] = t.words[name]
            else:
                show[name] = t.word_argc.get(name, 0)
        print(str(show))

        show = {}
        for name in e.root.sigils:
            show[name] = "SIGIL"
        for name in t.sigils:
            show[name] = "SIGIL"
        print(str(show))

    @staticmethod  ### SEE:ALL++ ###
    def word_SEE_colon_ALL_plus_plus(e, t, c):
        print(str(e.root.words))
        print(str(t.words))
        print(str(e.root.sigils))
        print(str(t.sigils))
