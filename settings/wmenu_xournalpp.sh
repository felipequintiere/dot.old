#!/bin/bash

# run "find $HOME -name "*.pdf" > $HOME/.config/settings/.dmenu_books_log" to update the list

selected=$(cat $HOME/.config/settings/.dmenu_books_log | wmenu -b -i -l 20  -f "pango:monospace 16" -N "#000000" -n "#a8a8a8" -S "#19B5E0" -s "#ffffff")
[ -n "$selected" ] && xournalpp "$selected"

