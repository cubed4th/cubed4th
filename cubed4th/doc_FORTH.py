#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2022, Scott.McCallum@HQ.UrbaneINTER.NET

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

        from .FORTH import Engine

        std = self.standard_2012()
        v = MagicVistor(std)
        e = Engine(vis=v)

        import dis

        files = {}

        for name in v.in_order:
            print()
            print()
            data = std.get(name, {})
            if 'en' in data:
                print(name, " == ", data["en"])
            else:
                print(name)

            print()

            print(v.to_code[name].__doc__)

            print()
            print(data.get("text", ""))
            print()

            fname = v.to_code[name].__code__.co_filename
            if not fname in files:
                files[fname] = ['']
                for line in open(fname, 'r').readlines():
                    files[fname].append(line.rstrip())

            print(fname)

            fline = v.to_code[name].__code__.co_firstlineno
            for i in range(fline, fline + 2):
                line = files[fname][i]
                print(f'Line: {i} == ', line)




            print()
            #print(dir(v.to_code[name].__code__))

        #e.execute("SEE /")


    def standard_2012(self):

        import simplejson as json
        from bs4 import BeautifulSoup

        with open("books\\2012.json", "r") as f:
            std = json.loads(f.read())['wordSets']

        all_help = {}

        for k, v in std.items():
            for k1, v1 in v['words'].items():
                help = {}
                stack_plain = v1['stackEffect']['plain']
                help["effects"] = stack_plain.get('NBSP', '')
                data = v1['sections'].get('NBSP', {})

                html = data.get('html', '')
                html = html.replace('<em>', '  ')
                html = html.replace('</em>', '  ')

                soup = BeautifulSoup(html, 'html.parser')

                text = ''
                for t in soup.find_all(text=True):
                    print("t = ", t)
                    text += '{} '.format(t)

                #print("----")
                #print(text)
                #print("----")

                text = text.strip()
                for x in range(0, 10):
                    text = text.replace("  ", " ")

                text = text.replace("\n\n", " ")
                text = text.replace("\n", " ")


                for o in ['n', 'x', 'u']:
                    for i in ['1', '2', '3', '4']:
                        text = text.replace(f"{o} {i}", f"{o}{i}")

                lines = text.split('\n')
                lines = lines[4:]
                text = '\n'.join(lines)

                help["text"] = text

                help["url"] = f"https://forth-standard.org/standard/{k}/{k1}"

                help["en"] = v1.get('english', None)
                if help["en"] == "NBSP":
                    help["en"] = v1.get('name', None)

                all_help[v1['name'].lower()] = help

        return all_help




class MagicVistor:

    def __init__(self, std):
        self.std = std

        self.in_order = []

        self.to_code = {}
        self.to_fname = {}
        self.to_sname = {}
        self.to_lname = {}  # the mapping to library name
        self.is_sigil = {}
        self.is_word = {}

    def before_imports(self, engine):
        pass

    def before_import(self, lname, lcode):
        self.lname = lname
        self.lcode = lcode

    def visit_sigil(self, code, fname, sname, tname):  # full, short, true
        assert tname not in self.is_sigil
        self.is_sigil[tname] = True

        self.in_order.append(tname)

        self.to_code[tname] = code
        self.to_fname[tname] = fname
        self.to_sname[tname] = sname
        self.to_lname[tname] = self.lname



    def visit_word(self, code, fname, sname, tname):
        assert tname not in self.is_word
        self.is_word[tname] = True

        self.in_order.append(tname)

        self.to_code[tname] = code
        self.to_fname[tname] = fname
        self.to_sname[tname] = sname
        self.to_lname[tname] = self.lname

    def after_import(self, name, lib):
        pass

    def after_imports(self, engine):

        return

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
