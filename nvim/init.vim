:set number
:set relativenumber
:set ic
":colorscheme elflord
":colorscheme zaibatsu
:colorscheme vim


" Center the screen after <C-D> and <C-U>
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz
nnoremap <C-f> <C-f>zz
nnoremap <C-b> <C-b>zz

" Center the screen after j and k
nnoremap j jzz
nnoremap k kzz

"Make Neovim run the command <C-d>zz right after it has been opened
autocmd VimEnter * call feedkeys("\<C-d>zz", 'n')

"highlight Normal guibg=none
"highlight NonText guibg=none
"highlight Normal ctermbg=none
"highlight NonText ctermbg=none

