#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _                _     _              __       __
  /\| |/\  | |              | |   | |            / /       \ \
  \ ` ' /  | |__    ______  | |_  | |_   _ __   | |   ___   | |
 |_     _| | '_ \  |______| | __| | __| | '_ \  | |  / __|  | |
  / , . \  | | | |          | |_  | |_  | |_) | | |  \__ \  | |
  \/|_|\/  |_| |_|           \__|  \__| | .__/  | |  |___/  | |
                                        | |      \_\       /_/
                                        |_|

)







"""  # __banner__


class LIB:  #

    """


    """

    def __init__(self, e, t, **kwargs):
        t.h_data = {}
        t.h_params = {}
        t.h_outgoing = {} # headers
        t.h_method = 'post'
        t.h_status = 0
        t.h_json = {}
        t.h_result = None
        t.h_incoming = {} # headers

    @staticmethod  ### H-METHOD  ###
    def word_H_m_METHOD__R(e, t, c, s):
        t.h_method = s.lower()

    @staticmethod  ### H-STATUS  ###
    def word_H_m_STATUS__R_x1(e, t, c):
        return (t.h_status,)

    @staticmethod  ### H-HEADER  ###
    def word_H_m_HEAD__R(e, t, c, s1, s2):
        t.h_outgoing[s2] = s1

    @staticmethod  ### H-DATA  ###
    def word_H_m_DATA__R(e, t, c, x):

        def encode(_):
            if isinstance(_, complex):
                return {"__complex__": True, "real": _.real, "imag": _.imag}
            raise TypeError(repr(_) + " is not JSON serializable")

        import simplejson
        t.h_data = simplejson.dumps(x, default=encode)

    @staticmethod  ### H-PARAMS  ###
    def word_H_m_PARAMS__R(e, t, c, x):
        t.h_params = x

    @staticmethod  ### H-JSON  ###
    def word_H_m_JSON__R_x(e, t, c):

        def h(values):
            if "__complex__" in values:
                return complex(values["real"], values["imag"])
            return values

        import simplejson
        return (simplejson.loads(t.h_result.text, use_decimal=True, object_hook=h),)

    @staticmethod  ### H-HEADERS  ###
    def word_H_m_HEADERS__R_x(e, t, c):
        return (t.h_incoming,)

    @staticmethod  ### H-REQUEST<300  ###
    def word_H_m_REQUEST_langle_300__R(e, t, c, s1):
        LIB.word_H_m_REQUEST__R(e, t, c, s1)
        h_status = t.h_status
        assert h_status < 300

    @staticmethod  ### H-REQUEST  ###
    def word_H_m_REQUEST__R(e, t, c, s1):

        import requests, copy

        kw = {"data": t.h_data}

        has_content_type = False
        for k, v in t.h_outgoing:
            if k.lower() == "content-type":
                has_content_type = True

        kw["headers"] = copy.copy(t.h_outgoing)
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
        t.h_headers = response.headers
        t.h_result = response


