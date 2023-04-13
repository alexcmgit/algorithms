// By @steffan https://codegolf.stackexchange.com/users/92689/steffan.
f(s,[v,i=0])=>s.split('').map((e)=>i++<1||!(v='aeiou'.contains)(s[i-2])||v(e)?e:e.toUpperCase()).join();