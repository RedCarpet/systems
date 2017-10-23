#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#print("pryce3")

import urwid

#############################################################
#t0="List of Jobs:-"
#t1="\n1)landscape"
#t2="\n2)  cut grass"
#t3="\n3)    fix mower"
#total=t0+t1+t2+t3

#txt = urwid.Text(total)
#fill = urwid.Filler(txt, "top")
#loop = urwid.MainLoop(fill)
#loop.run()



######################################################################

#def exit_on_q(key):
#    if key in ('q', 'Q'):
#        raise urwid.ExitMainLoop()

#palette = [
#    ('banner', 'light green', 'black'),
#    ('streak', 'black', 'dark red'),
#    ('bg', 'black', 'dark blue'),]

#txt = urwid.Text(('banner', u" cccccccccccc Hello World "), align='left')
#map1 = urwid.AttrMap(txt, 'streak')
#fill = urwid.Filler(map1)
#map2 = urwid.AttrMap(fill, 'bg')

#loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
#loop.run()
###########################################################################


#def exit_on_q(key):
#    if key in ('q', 'Q'):
#        raise urwid.ExitMainLoop()
#
#class QuestionBox(urwid.Filler):
#    def keypress(self, size, key):
#        if key != 'enter':
#            return super(QuestionBox, self).keypress(size, key)
#        self.original_widget = urwid.Text(
#            u"Nice to meet you,\n%s.\n\nPress Q to exit." %
#            edit.edit_text)
#
#edit = urwid.Edit(u"What is your name?\n")
#fill = QuestionBox(edit)
#loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
#loop.run()


##


choices = u'Chapman Cleese Gilliam Idle Jones Palin a b c d e f g h i j k l m n o p'.split()

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
        urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 60),
    valign='middle', height=('relative', 60),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()



