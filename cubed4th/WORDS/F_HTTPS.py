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
        t.h_headers = {}
        t.h_method = 'post'
        t.h_status = 0
        t.h_json = {}
        t.h_result = None

    @staticmethod  ### H-METHOD  ###
    def word_H_m_METHOD__R(e, t, c, s):
        t.h_method = s.lower()

    @staticmethod  ### H-GET-STATUS  ###
    def word_H_m_GET_m_STATUS__R_x1(e, t, c):
        return (t.h_status,)

    @staticmethod  ### H-SET-HEADER  ###
    def word_H_m_SET_m_METHOD__R(e, t, c, s1, s2):
        t.h_headers[s2] = s1

    @staticmethod  ### H-DATA  ###
    def word_H_m_DATA__R(e, t, c, x):
        import json
        t.h_data = json.dumps(x)

    @staticmethod  ### H-PARAMS  ###
    def word_H_m_PARAMS__R(e, t, c, x):
        t.h_params = x

    @staticmethod  ### H-JSON  ###
    def word_H_m_INCOMING__R_x(e, t, c):
        return (t.h_result.json(),)

    @staticmethod  ### H-REQUEST  ###
    def word_H_m_REQUEST__R(e, t, c, s1):

        import requests

        kw = {"data": t.h_data}

        has_content_type = False
        for k, v in t.h_headers:
            if k.lower() == "content-type":
                has_content_type = True

        kw["headers"] = copy.copy(t.h_headers)
        if not has_content_type:
            kw["headers"]["Content-Type"] = 'application/json'

        assert t.h_method in ["post","get","put","patch","delete"]

        if t.h_method == 'post':
            response = requests.post(s1, **kw)
        elif t.h_method == 'get':
            response = requests.get(s1, **kw)
        elif t.h_method == 'put':
            response = requests.put(s1, **kw)
        elif t.h_method == 'patch':
            response = requests.patch(s1, **kw)
        elif t.h_method == 'delete':
            response = requests.delete(s1, **kw)

        t.h_status = response.status_code
        t.h_result = response

import copy
