#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _    _   _______   __  __   _
  /\| |/\  | |  | | |__   __| |  \/  | | |
  \ ` ' /  | |__| |    | |    | \  / | | |
 |_     _| |  __  |    | |    | |\/| | | |
  / , . \  | |  | |    | |    | |  | | | |____
  \/|_|\/  |_|  |_|    |_|    |_|  |_| |______|


)








""" # __banner__


class LIB:  # { JavaScript Object Notation : words }

    """

    T{ ("Hello World") -> 'Hello ''World + }T

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod
    def load(e):
        return (e.root.memory.get('<html>', []), e.root.memory.get('<html_stack>', []))

    @staticmethod
    def save(e, html, html_stack):
        e.root.memory['<html>'] = html
        e.root.memory['<html_stack>'] = html_stack


    @staticmethod  ### <!tag ###
    def sigil_langle_bang(e, t, c, token, start):
        html, html_stack = LIB.load(e)
        token = ' '.join(token.split("'"))
        html.append(token)
        LIB.save(e, html, html_stack)


    @staticmethod  ### <>tag ###
    def sigil_langle_rangle(e, t, c, token, start):
        html, html_stack = LIB.load(e)
        token = ' '.join(token[2:].split("'"))
        if token[-1] == '>': token = token[:-1]
        if not token.lower() in ['textarea']: html.append('  '*len(html_stack))
        html.append('<' + token + '>')
        token = token.split(' ')[0]
        if not token.lower() in ['td', 'textarea']: html.append("\n")
        if not token.lower() in []: html_stack.append(token)
        LIB.save(e, html, html_stack)

    @staticmethod  ### }<>tag ###
    def sigil_rbrace_langle_rangle(e, t, c, token, start):
        html, html_stack = LIB.load(e)
        token = ' '.join(token[3:].split("'"))
        if token[-1] == '>': token = token[:-1]
        values = t.stack.pop()
        for k in values.keys():
            if not token[-1] == ' ':
                token = token + ' '
            token = token + k + '="' + values[k] + '"'
        if not token.lower() in ['textarea']: html.append('  '*len(html_stack))
        html.append('<' + token + '>\n')
        token = token.split(' ')[0]
        if not token.lower() in ['td','textarea']: html.append("\n")
        html_stack.append(token)
        LIB.save(e, html, html_stack)


    @staticmethod  ### <>/tag ###
    def sigil_langle_rangle_divide(e, t, c, token, start):
        html, html_stack = LIB.load(e)
        token = ' '.join(token[3:].split("'"))
        if not token.lower() in ['td', 'br', 'textarea']: html.append('  '*len(html_stack))
        html.append('<' + token + ' />')
        token = token.split(' ')[0]
        if not token.lower() in ['td', 'br']: html.append("\n")
        LIB.save(e, html, html_stack)

    @staticmethod  ### </ ###
    def sigil_langle_divide(e, t, c, token, start):
        html, html_stack = LIB.load(e)
        token = html_stack.pop()
        if not token.lower() in ['td', 'textarea']: html.append('  '*len(html_stack))
        html.append('</' + token + '>')
        html.append('\n')
        LIB.save(e, html, html_stack)

    @staticmethod  ### <HTML> ###
    def word_langle_HTML_rangle__R(e, t, c, s):
        e.root.memory['<html>'] = []
        e.root.memory['<html_stack>'] = []

    @staticmethod  ### <TXT> ###
    def word_langle_TXT_rangle__R(e, t, c, s):
        html, html_stack = LIB.load(e)
        html.append(s)
        LIB.save(e, html, html_stack)

    @staticmethod  ### <ESC> ###
    def word_langle_ESC_rangle__R(e, t, c, s):
        html, html_stack = LIB.load(e)
        html.append(str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace('"', "&quot;").replace("'", "&#x27;").replace("`", "&#x60;"))
        LIB.save(e, html, html_stack)

    @staticmethod  ### <!-- ###
    def sigil_langle_bang_minus_minus(e, t, c, token, start=False):
        """
        """
        if isinstance(token, str) and len(token) and token[-3:] == "-->":
            t.state = e.state_INTERPRET
            return

        t.state = LIB.sigil_langle_bang_minus_minus






