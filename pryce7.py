#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#print("pryce7")

import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))
    
    

txt 	= urwid.Text("JOB SYSTEM")

fill 	= urwid.Filler(txt,"top")

loop 	= urwid.MainLoop(fill, unhandled_input=show_or_exit)

loop.run()
