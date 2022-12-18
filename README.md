# ZX
ZX is a simple programming language made with Python 3.  

## Intructions

ZX has two data types: `string` and `number`[^1]

`pt|<text>` lets you print text to the console. In some cases, you can replace <text> with `pt|<var>`.   
`ct` clears the console.    
`it|<var>|<text>` asks user for input then stores it in `var`.   
`m+|<a>|<b>|<var>` adds `a` and `b` then stores it in `var`.   
`m-|<a>|<b>|<var>` subtracts `a` and `b` then stores it in `var`.   
`m*|<a>|<b>|<var>` multiplys `a` and `b` then stores it in `var`.    
`m/|<a>|<b>|<var>` divides `a` and `b` then stores it in `var`.    
`jt|<str1>|<str2>|<var>` joins `str1` and `str2` together then stores it in `var`    
`wt|<time>|<func>` waits for a certain period of time (in seconds) then executes command inside `func`. Can only run `pt` or `ct`.    
`rn|<range>|<var>` returns a random number between 0 and `range` in `var`

[^1]: In ZX, there are three variables: `a`, `b`, `c`. Each variable can store a `string` and a `number`. Use `v>` before a variable to reference it (only works on `pt`).
