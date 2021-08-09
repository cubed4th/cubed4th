#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _                _______   _______   _____        __   _____
  /\| |/\  | |              |__   __| |__   __| |  __ \      / /  / ____|
  \ ` ' /  | |__               | |       | |    | |__) |    / /  | (___
 |_     _| | '_ \              | |       | |    |  ___/    / /    \___ \
  / , . \  | | | |             | |       | |    | |       / /     ____) |
  \/|_|\/  |_| |_|             |_|       |_|    |_|      /_/     |_____/
                    ______
                   |______|

)







"""  # __banner__


class LIB:  #

    """


    """

    def __init__(self, e, t, **kwargs):
        t.h_data = {}
        t.h_params = {}
        t.h_method = 'POST'
        t.h_status = 0
        t.h_json = {}
        t.h_result = None

    @staticmethod  ### H-STATUS  ###
    def word_H_minus_STATUS__R_x1(e, t, c):
        return (t.h_status,)

    @staticmethod  ### H-METHOD  ###
    def word_H_minus_METHOD__R(e, t, c, s):
        t.h_method = s.upper()

    @staticmethod  ### H-DATA  ###
    def word_H_minus_DATA__R(e, t, c, x):
        import json
        t.h_data = json.dumps(x)

    @staticmethod  ### H-PARAMS  ###
    def word_H_minus_PARAMS__R(e, t, c, x):
        t.h_params = x

    @staticmethod  ### H-JSON  ###
    def word_H_minus_INCOMING__R_x(e, t, c):
        return (t.h_result.json(),)

    @staticmethod  ### H-REQUEST  ###
    def word_H_minus_REQUEST__R(e, t, c, s1):

        kw = {"data": t.h_data}

        headers = {'Content-Type': 'application/json'}
        proxies = {
              # "http"  : "http://127.0.0.1:8888"
            }

        import requests
        if t.h_method == "POST":
            r = requests.post(s1, **kw, proxies=proxies, headers=headers)
        elif t.h_method == "GET":
            kw["params"] = t.h_params
            r = requests.get(s1, **kw, proxies=proxies, headers=headers)
        elif t.h_method == "PUT":
            r = requests.put(s1, **kw, proxies=proxies, headers=headers)
        elif t.h_method == "PATCH":
            r = requests.patch(s1, **kw, proxies=proxies, headers=headers)
        elif t.h_method == "DELETE":
            r = requests.delete(s1, **kw, proxies=proxies, headers=headers)
        else:
            raise RuntimeError("H-TTP(S) not supported: %s" % (h.method))

        t.h_status = r.status_code
        t.h_result = r


