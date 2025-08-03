#!/bin/bash

dir="$HOME/.config/alacritty"
theme=$(wc -l < $dir/.selected_themes)
custom=$(cat $dir/custom/*)

if [ $(cat $dir/.current_theme.log) == 1 ];then
	xx=$theme
	echo "$theme" > $dir/.current_theme.log
else
	x=$(cat $dir/.current_theme.log)
	xx=$(($x-1))
	echo "$(($x - 1))" > $dir/.current_theme.log
fi

y=$(sed -n "${xx}p" $dir/.selected_themes)

echo "
[general]
import = [$y]

$custom

" > $dir/alacritty.toml
