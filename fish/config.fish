if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""

#set -x MANPAGER='nvim -u ~/.config/nvim/init.vim +Man!'
set -x MANPAGER 'nvim +Man!'

function fish_prompt
    set_color green
    echo -n "["
    set_color green
    echo -n (whoami)
    set_color white
    echo -n "@"
    set_color cyan
    echo -n (uname -n)" "
    set_color blue
    echo -n (prompt_pwd)
    set_color green
    echo -n "]"
    set_color normal
    echo -n "\$ "
end

alias py='python3'
alias p='python3'

#alias ls='ls -1 --color=auto'
alias ls='ls -lh --color=auto'

alias sl='ls --color=auto'
alias s='ls --color=auto'
alias l='ls -l --color=auto'
alias ll='ls -l --color=auto'
alias lla='ls -la --color=auto'
alias la='ls -a --color=auto'
alias al='ls -a --color=auto'

alias sclear='clear'
alias grep='grep --color=auto'

alias v='nvim'
alias vi='nvim'
alias vim='nvim'

alias x='startx'

#alias off='shutdown -P now'
alias off='systemctl poweroff'
alias net='bash ~/.config/i3/scripts/net.sh'

#alias anime='ani-cli -v --dub --rofi'
alias anime='ani-cli -v --dub'

#update books list
alias ubook='find $HOME -name "*.pdf" > $HOME/.config/settings/.dmenu_books_log'
