#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

      _                           ______    ____    _____    _______   _    _
     | |                         |  ____|  / __ \  |  __ \  |__   __| | |  | |
   __| |   ___     ___           | |__    | |  | | | |__) |    | |    | |__| |
  / _` |  / _ \   / __|          |  __|   | |  | | |  _  /     | |    |  __  |
 | (_| | | (_) | | (__           | |      | |__| | | | \ \     | |    | |  | |
  \__,_|  \___/   \___|          |_|       \____/  |_|  \_\    |_|    |_|  |_|
                         ______
                        |______|

)

As this module is not available in production



"""  # __banner__

class DOC:

    def __init__(self):
        pass

    def magic(self):

        std = self.standard_2012()

        vis = MagicVistor(std)

        from .FORTH import Engine
        e = Engine(vis=vis)





        #e.execute("SEE /")





    def standard_2012(self):

        import simplejson as json

        with open("books\\2012.json", "r") as f:
            std = json.loads(f.read())['wordSets']

        all_help = {}

        for k, v in std.items():
            for k1, v1 in v['words'].items():
                help = []
                stack_plain = v1['stackEffect']['plain']
                help.append(stack_plain.get('NBSP', ''))
                text = v1['sections'].get('NBSP', {})
                html = text.get('html', '').replace('\n', ' ')
                html = html.replace("&lt;", "<")
                html = html.replace("&gt;", ">")
                for tag in ['em', 'strong', 'sub', 'p']:
                    html = html.replace(f'<{tag}>', '')
                    html = html.replace(f'</{tag}>', '')

                for loop in range(0, 3):
                    html = html.replace('  ', ' ')

                html = html.strip()

                temp = stack_plain.get('NBSP', '')
                if html[:len(temp)] == temp:
                    html = html[len(temp):]

                html = html.strip()

                help.append(html)

                help.append(f"https://forth-standard.org/standard/{k}/{k1}")

                all_help[v1['name'].lower()] = help

        return all_help




class MagicVistor:

    def __init__(self, std):
        self.std = std

        self.in_order = []

        self.is_word = {}
        self.to_code = {}
        self.to_fname = {}
        self.to_sname = {}
        self.to_lname = {}  # the mapping to library name

    def before_imports(self, engine):
        pass

    def before_import(self, lname, lcode):
        self.lname = lname
        self.lcode = lcode

    def visit_sigil(self, code, fname, sname, tname):  # full, short, true
        assert tname not in self.to_fname

        self.in_order.append(tname)

        self.is_word[tname] = False
        self.to_code[tname] = code
        self.to_fname[tname] = fname
        self.to_sname[tname] = sname
        self.to_lname[tname] = self.lname

    def visit_word(self, code, fname, sname, tname):
        assert tname not in self.to_fname

        self.in_order.append(tname)

        self.is_word[tname] = True
        self.to_code[tname] = code
        self.to_fname[tname] = fname
        self.to_sname[tname] = sname
        self.to_lname[tname] = self.lname

    def after_import(self, name, lib):
        pass

    def after_imports(self, engine):

        sorted = copy.copy(self.in_order)
        sorted.sort()

        for i in range(0, len(sorted)):
            tname = sorted[i]

            url = self.std[tname][2] if tname in self.std else ''

            code = self.to_code[tname]
            lname = self.to_lname[tname]

            print("%03i %10s %10s %30s %s"%(i, lname, tname, self.to_sname[tname], url))

            if self.is_word[tname]:

                parts = self.to_fname[tname].split("_")
                name = []
                meta = None
                for part in parts:
                    if meta is None:
                        if part == "":
                            meta = []
                            continue
                    else:
                        meta.append(part)
                        continue
                    name.append(engine.symbol_map.get(part, part))

                name = "".join(name)
                where = engine.root

                #  if name in where:
                #      raise ForthException(f"{name}: error(-4): Word Already Defined")

                if name in where.word_immediate:
                    del where.word_immediate[name]

                if not meta is None:
                    if "i" in meta[0]:
                        where.word_immediate[name] = True

                where.words[name] = code
                argc = code.__code__.co_argcount - 3

                doc = code.__doc__

                #fname = self.to_fname[name]

                #parts = fname.split("_")

            if i == 20: break




__openapi_header__ = """

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from quart import Quart, websocket
from quart_schema import QuartSchema, validate_request, validate_response

app = Quart(__name__)
QuartSchema(app)

@dataclass
class Todo:
    task: str
    due: Optional[datetime]

"""

__openapi_body__ = """

@app.post("/")
@validate_request(Todo)
@validate_response(Todo, 201)
async def create_todo(data: Todo) -> Todo:
    ... # Do something with data, e.g. save to the DB
    return data, 201

"""

__openapi_footer__ = """




"""

import hashlib, copy
