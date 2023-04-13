function controlCar(scanArray) {
  // Show me the way...
  // console.log(
  //   scanArray,
  //   "|",
  //   scanArray[4],
  //   scanArray[5],
  //   scanArray[6],
  //   "|",
  //   scanArray[7],
  //   scanArray[8],
  //   scanArray[9],
  //   "|",
  //   scanArray[10],
  //   scanArray[11],
  //   scanArray[12]
  // );

  const [g] = [...scanArray].sort((a, z) => z - a);

  const left = scanArray.slice(0, 7);
  const center = scanArray.slice(7, 10); // Why does it is even here?
  const right = scanArray.slice(10, 17);

  if (left.indexOf(g) !== -1) return -1;
  if (right.indexOf(g) !== -1) return 1;

  return 0;
}
