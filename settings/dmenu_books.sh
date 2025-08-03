#!/bin/bash

# run "find $HOME -name "*.pdf" > $HOME/.config/settings/.dmenu_books_log" to update the list

selected=$(cat $HOME/.config/settings/.dmenu_books_log | dmenu -b -i -l 20 -p "> " -fn "monospace-16" -nb "#000000" -nf "#a8a8a8" -sb "#19B5E0" -sf "#ffffff")
[ -n "$selected" ] && zathura "$selected"


