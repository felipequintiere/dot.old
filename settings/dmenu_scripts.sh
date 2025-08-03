#!/bin/bash

dir="$HOME/.config/settings"
selected=$(ls "$dir" | dmenu -b -i -l 20 -p "$ " -fn "monospace-16" -nb "#000000" -nf "#a8a8a8" -sb "#de1d95" -sf "#ffffff")
[ -n "$selected" ] && "$dir/$selected"

#dmenu_run -i -p "Run" -fn "monospace-16" -nb "#000000" -nf "#a8a8a8" -sb "#9d07e0" -sf "#ffffff"


#-nb Normal Background — the background color of unselected items		"#0000ff" (blue)
#-nf Normal Foreground — the text color of unselected items			"#ffffff" (white)
#-sb Selected Background — background color of the currently highlighted item	"#800080" (purple)
#-sf Selected Foreground — text color of the highlighted item			"#ffffff" (white)
