f(n)=>'$n'.split('').asMap().entries.where((e)=>e.key.isOdd).map((e)=>int.parse(e.value)).reduce((v,e)=>v+e);
