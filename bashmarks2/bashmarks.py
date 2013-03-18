#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bilal Syed Hussain

import alfred
import subprocess
#from pprint import pprint as pp


counter = 0
def create_item(name, value):
    global counter,s_args
    item = alfred.Item(
        attributes={'uid': "bashmarks", 'arg': value, 'type': 'file'},
        # title= u"  " + name,
        title=value,
        subtitle= name + u"  ",
        icon=(value, {'type': 'fileicon'})
    )
    counter += 1
    return item


def run(query):
    # Get bashmarks
    output = subprocess.check_output(
        ". ~/.local/bin/bashmarks.sh && _bookmarks_no_colour ", shell=True)
    mapping = [line.split("=") for line in output.splitlines()[1:]]

    if query:
        mapping = [(k,v) for (k,v) in mapping if k.startswith(query)]

    # Made the xml
    items = [create_item(k, v) for (k, v) in mapping]
    xml = alfred.xml(items)

    # writes the XML back to Alfred
    # alfred.write(xml)
    print str(xml)
