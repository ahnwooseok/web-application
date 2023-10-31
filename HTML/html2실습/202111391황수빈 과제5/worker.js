var n = 1;
while (true) {
  n += 1;
  var isPrime = true;
  for (var i = 2; i <= Math.sqrt(n); i += 1) {
    if (n % i === 0) {
      isPrime = false;
      break;
    }
  }
  if (isPrime) {
    postMessage(n);
  }
}
