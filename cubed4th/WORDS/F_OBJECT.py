#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2022, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       ____    ____         _   ______    _____   _______
  /\| |/\   / __ \  |  _ \       | | |  ____|  / ____| |__   __|
  \ ` ' /  | |  | | | |_) |      | | | |__    | |         | |
 |_     _| | |  | | |  _ <   _   | | |  __|   | |         | |
  / , . \  | |__| | | |_) | | |__| | | |____  | |____     | |
  \/|_|\/   \____/  |____/   \____/  |______|  \_____|    |_|



)







"""  # __banner__


class LIB:  # { The Object ABI : words }

    """

    -2 VALUE foo
    'ABCDE VALUE bar
    ([1,2,3]) VALUE List1

    T{ LIST1 2 -        -> ([1,3])         }T
    T{ LIST1            -> ([ 1 , 2 , 3 ]) }T
    T{ 'Hello [ foo : ] -> 'lo             }T
    T{ LIST1 [ foo ]    -> 2               }T
    T{ BAR [ 1 : 3 ]    -> 'BC             }T

    LIST1 99 !

    T{ 99 *LEN          -> 3               }T
    T{ 99 *[ -1 ]       -> 3               }T

    """

    def __init__(self, e, t, **kwargs):
        pass

    @staticmethod  ### PYTHON ###
    def word_PYTHON__R(e, t, c, s1):

        from RestrictedPython import compile_restricted
        from RestrictedPython import safe_globals

        loc = {}
        byte_code = compile_restricted(s1, "<inline>", "exec")
        exec(byte_code, safe_globals, loc)

        for name in sorted(loc):
            if name.startswith("word_"):
                e.add_word(name[5:], loc[name])
            if name.startswith("sigil_"):
                e.add_word(name[6:], loc[name])

    @staticmethod  ### LAMBDA ###
    def word_LAMBDA__R(e, t, c, s1, s2):
        s2 = repr(s2)
        parts = s1.split(":", 1)
        parts[0] = parts[0].strip()
        parts[0] = ", " + parts[0] if len(parts[0]) else parts[0]
        s1 = ":".join(parts)
        exec(f"e.add_word({s2}, lambda e, t, c{s1})")

    @staticmethod  ### INT ###
    def word_INT__R_n(e, t, c, s):
        return (int(s),)

    @staticmethod  ### LEN ###
    def word_LEN__R_n(e, t, c, x):
        "T{ 'Hello'World' len nip -> 11 }T"
        return (x, len(x),)

    @staticmethod  ### *LEN ###
    def word_times_LEN__R_n(e, t, c, a):
        """"""
        return (len(t.memory[a]),)

    @staticmethod  ### NOT ###
    def word_NOT__R_b(e, t, c, x):
        """"""
        return (not x,)

    @staticmethod  ### ~ ###
    def word_tilde__R_b(e, t, c, x):
        return (not x,)

    @staticmethod  ### *~ ###
    def word_times_tilde__R_b(e, t, c, a):
        return (not t.memory[a],)

    @staticmethod  ### [ ###
    def word_lbrack__R(e, t, c):
        struct = {"?": "[", "s": len(t.stack), "r": t.state}
        struct[" : "] = e.OBJECT.state_do_slice
        struct[" , "] = e.OBJECT.state_make_list
        c.stack.append(struct)

    @staticmethod  ### *[ ###
    def word_times_lbrack__R(e, t, c, a):
        struct = {"?": "[", "s": len(t.stack), "r": t.state, "a": a}
        struct[" : "] = e.OBJECT.state_do_slice
        struct[" , "] = e.OBJECT.state_make_list
        c.stack.append(struct)

    @staticmethod
    def state_do_slice(e, t, c):
        struct = c.stack[-1]
        assert struct["?"] == "["
        struct[2] = t.stack[struct["s"] :]
        t.stack = t.stack[: struct["s"]]

    @staticmethod
    def state_make_list(e, t, c):
        struct = c.stack[-1]
        assert struct["?"] == "["
        struct[0] = struct.get(0, [])
        struct[0].extend(t.stack[struct["s"] :])
        t.stack = t.stack[: struct["s"]]

    @staticmethod  ### ] ###
    def word_rbrack__R_x(e, t, c):
        struct = c.stack.pop()
        assert struct["?"] == "["

        if 0 in struct:
            struct[0].extend(t.stack[struct["s"] :])
            t.stack = t.stack[: struct["s"]]
            t.stack.append(struct[0])
            return

        struct_1 = t.stack[struct["s"] :]
        t.stack = t.stack[: struct["s"]]

        if "a" in struct:
            obj = t.memory[struct["a"]]
        else:
            # leave the object alone, use nip to delete if desired
            obj = t.stack[-1]

        if 2 in struct:
            struct_2 = struct[2]

            if len(struct_2):
                if len(struct_1):
                    t.stack.append(obj[struct_2[-1] : struct_1[-1]])
                else:
                    t.stack.append(obj[struct_2[-1] :])
            else:
                if len(struct_1):
                    t.stack.append(obj[: struct_1[-1]])
                else:
                    t.stack.append(obj[:])
        else:

            if len(struct_1):
                index_1 = struct_1[-1]
                # index_1 = index_1 if isinstance(index_1, str) else int(index_1)
                t.stack.append(obj[index_1])
            else:
                e.raise_SyntaxError("[ ] Is Illegal")

    @staticmethod  ### (. ###
    def sigil_lparen_dot(e, t, c, token, start=False):
        """
        T{ 'FOO DUP (.__len__) -> 'FOO 3 }T
        """
        end = token[-1] == ")"
        if end:
            obj = t.stack.pop()
            code = getattr(obj, token[2:-1])
            result = code()
            if isinstance(result, tuple):
                t.stack.extend(result)
            else:
                t.stack.append(result)

            return

        c.stack.append({"?": "()", ".": token[2:], "d":len(t.stack)})

    @staticmethod  ### ) ###
    def word_rparen__R_x(e, t, c):
        """
        T{ 'FOO (.replace 'O 'J ) -> 'FOO 'FJJ }T
        """
        LIB.impl_rparen_R_x(e, t, c, pop_obj=False)

    @staticmethod  ### )- ###
    def word_rparen_minus__R_x(e, t, c):
        """
        T{ 'FOO (.replace 'O 'J )- -> 'FJJ }T
        """
        LIB.impl_rparen_R_x(e, t, c, pop_obj=True)


    @staticmethod  ### )- ###
    def impl_rparen_R_x(e, t, c, pop_obj):

        struct = c.stack.pop()
        assert struct["?"] == "()"

        args = t.stack[struct["d"]:]
        args.extend(tuple(struct.get("*",[])))
        t.stack = t.stack[:struct["d"]]

        kwargs = struct.get("**", {})

        if pop_obj:
            obj = t.stack.pop()
        else:
            obj = t.stack[-1]

        code = getattr(obj, struct["."])
        result = code(*args, **kwargs)
        if isinstance(result, tuple):
            t.stack.extend(result)
        else:
            t.stack.append(result)








