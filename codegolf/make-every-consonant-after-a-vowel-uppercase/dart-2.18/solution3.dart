// Original by @alephsquirrel https://codegolf.stackexchange.com/users/115910/alephsquirrel.
// Ported by @steffan https://codegolf.stackexchange.com/users/92689/steffan.
f(s,[d=0])=>s.split('').map((e)=>d>(d='aeiou'.contains(e)?1:0)?e.toUpperCase():e).join();