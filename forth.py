#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) https://github.com/scott91e1 ~ 2021 - 2021


__banner__ = r""" (

  _       _
 (_)     | |
  _    __| |   ___       _ __    _   _
 | |  / _` |  / _ \     | '_ \  | | | |
 | | | (_| | |  __/  _  | |_) | | |_| |
 |_|  \__,_|  \___| (_) | .__/   \__, |
                        | |       __/ |
                        |_|      |___/

)





"""  # __banner__

import sys, click

sys.path.insert(0, "depends")
import cubed4th.cli_FORTH


@click.command()
@click.option("-f", "--file", default=None)
@click.option("-d", "--docs", default=None)
def run(file, docs):

    if docs:
        import cubed4th.doc_FORTH
        doc = cubed4th.doc_FORTH.DOC()
        exec(f"doc.{docs}()")
        return

    if file:
        file = open(file, "rt").read()

    #import cubed4th.cli_FORTH
    #cubed4th.cli_FORTH.ide_stdio(run=file)

    from cubed4th.gui_FORTH import gui_start
    gui_start(run=file)


if __name__ == "__main__":
    run()
