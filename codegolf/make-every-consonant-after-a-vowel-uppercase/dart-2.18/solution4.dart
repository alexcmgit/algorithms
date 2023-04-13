// Original by @arnauld https://codegolf.stackexchange.com/users/58563/arnauld.
// Ported by @steffan https://codegolf.stackexchange.com/users/92689/steffan.
f(s,[d=0])=>String.fromCharCodes([for(s in s.runes)s^d&~(d=68174912>>s%32)&32]);