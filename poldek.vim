" Vim syntax file
" Language:	Poldek configuration
" Version Info: $Revision$
" Author:       Elan Ruusamäe <glen@delfi.ee>
" Maintainer:   Elan Ruusamäe <glen@delfi.ee>
" Last Change:	$Date$ UTC
"
" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

" shut case off
syn case ignore

syn match  poldekLabel    "^.\{-}="
syn region poldekHeader   start="^\[" end="\]"
syn match  poldekComment  "^#.*$"
syn match  poldekDirective '\(%include\|%includedir\)\s.*$'
syn match  poldekMacro    '%{_\h\w*}' 

" Define the default highlighting.
" For version 5.7 and earlier: only when not done already
" For version 5.8 and later: only when an item doesn't have highlighting yet
if version >= 508 || !exists("did_inifile_syntax_inits")
  if version < 508
    let did_poldek_syntax_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  HiLink poldekHeader     Special
  HiLink poldekComment    Comment
  HiLink poldekLabel      Type
  HiLink poldekDirective  Statement
  HiLink poldekMacro      Macro

  delcommand HiLink
endif

let b:current_syntax = "poldek"

" vim:ts=2:sw=2
