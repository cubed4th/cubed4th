#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

                  _            ______    ____    _____    _______   _    _
                 (_)          |  ____|  / __ \  |  __ \  |__   __| | |  | |
   __ _   _   _   _           | |__    | |  | | | |__) |    | |    | |__| |
  / _` | | | | | | |          |  __|   | |  | | |  _  /     | |    |  __  |
 | (_| | | |_| | | |          | |      | |__| | | | \ \     | |    | |  | |
  \__, |  \__,_| |_|          |_|       \____/  |_|  \_\    |_|    |_|  |_|
   __/ |              ______
  |___/              |______|

)







"""  # __banner__

__version__ = "3.0.20221212"

class IDE:  # { The p-unity IDE: Intergrated Development Environment }

    def __init__(self, run=None, **kwargs):

        from queue import Queue


        bootstrap_ring_g = """

```

    1 'window_tag !
    ({}) 'windows !


```

        """

        # the ring_k is the kernel of the os
        self.ring_g = FORTH.Engine(run=bootstrap_ring_g)

        self.ring_g.root.memory["queue"] = Queue()

        # use stdin/stdout as the debging engine
        self.debug = FORTH.Engine(run, **kwargs)

        self.debug.root.memory["queue_g"] = self.ring_g.root.memory["queue"]


    def debug_entry(self, run=None):

        e = self.debug

        def Q(e, t, c):
            global running
            running = 0

        e.add_word("Q", Q)

        def S(e, t, c):
            global running
            running = 1

        e.add_word("S", S)
        e.add_word("BYE", S)
        e.add_word("EXIT", S)
        e.add_word("EXIT()", S)

        v = ["cubed4th " + __version__]
        p, f = e.root.test["p"], e.root.test["f"]
        if p > 0:
            v.append(f"(Sanity Tests; {p} Pass, {f} Fail)")

        if __debug_run__:
            print(__debug_run__.strip())
            e.execute(__debug_run__)

        print(" ".join(v))
        print("")

        ring_g_queue = self.ring_g.root.memory["queue"]

        global running
        while running == -1:

            print(" > ", end="")
            line = input("")

            import time
            if line[0:3] == '!g ':
                ring_g_queue.put(line[3:])
                time.sleep(0.1)
            else:
                try:
                    e.execute(line)
                except Exception as ex:
                    print("!> ", end="")
                    print(repr(ex))
                    #raise ex

            print()
            print("=>", end="")
            for object in e.root.stack:
                print(f" {repr(object)}", end="")
            print()

    print()

async def janitor(ide):

    global running

    while running == -1:
        await trio.sleep(0.042)


async def async_ring_g(ide):

    import dearpygui.dearpygui as dpg

    dpg.create_context()
    dpg.configure_app(manual_callback_management=True)

    def load_gui():
        ide.ring_g.root.memory["queue"].put("'gui.md load-file")

    with dpg.window(tag="Primary Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save", callback=load_gui)
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.create_viewport(title='cubed4th IDE', width=1024, height=768, x_pos=10, y_pos=10)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    #dpg.set_primary_window("Primary Window", True)

    global running
    while running == -1 and dpg.is_dearpygui_running():

        while not ide.ring_g.root.memory["queue"].empty():
            command = ide.ring_g.root.memory["queue"].get()
            try:
                engine = FORTH.Engine(run="")
                engine.execute(command, include=True)
            except Exception as ex:
                print("!! ", end="")
                print(repr(ex))
                #raise ex

        jobs = dpg.get_callback_queue() # retrieves and clears queue

        # taken from dpg.run_callbacks
        if not jobs is None:
            for job in jobs:
                if job[0] is None:
                    continue

                if job[3] != None:
                    try:
                        job[3].execute(job[0], include=True)
                    except Exception as ex:
                        print("!! ", end="")
                        print(repr(ex))
                        #raise ex
                    continue

                sig = inspect.signature(job[0])
                args = []
                for arg in range(len(sig.parameters)):
                    args.append(job[arg+1])
                job[0](*args)

        dpg.render_dearpygui_frame()

        await trio.sleep(0)

    jobs = dpg.get_callback_queue() # retrieves and clears queue
    dpg.run_callbacks(jobs)

    if running == -1:
        running = 0

    dpg.destroy_context()


async def trio_start(ide):

    async with trio.open_nursery() as nursery:
        nursery.start_soon(async_ring_g, ide)
        nursery.start_soon(janitor, ide)

def gui_start(run=None):
    ide = IDE()

    from threading import Thread
    ide.debug_thread = Thread(target = ide.debug_entry)
    ide.debug_thread.start()

    trio.run(trio_start, ide)

    global running
    try:
        running = int(running)
    except:
        running = 3

    sys.exit(running)


import sys, trio, inspect

running = -1

from . import FORTH

__debug_run__ = """

T{ : GD2 DO I -1 +LOOP ; -> }T
T{ 1 4 GD2 -> 4 3 2 1 }T
T{ -1 2 GD2 -> 2 1 0 -1 }T

"""

__debug_run__ = None
