function isPrime(){
    number = document.getElementById("input").value;
    if(checkPrime(number)){
        document.getElementById("output1").value = number + " is a prime number";
    }
    else{
        nprime = nearestPrime(number);
        document.getElementById("output1").value = number + " is not prime " + nprime + " is diffrence between next prime number";
    }
    
}
function checkPrime(n){
    if (n <= 1) // 1 is nor prime nor composite
        return false;
    if (n == 2 || n == 3) // 2 and 3 are prime
        return true;
    if (n % 2 == 0 || n % 3 == 0) // Number divisible by 2 and 3 are not prime
        return false;
    for (var i = 5; i <= Math.sqrt(n); i = i + 6) // check from 5v to square root of n 
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

function nearestPrime(n){
    if (n <= 1)
        return (2-n);
    let prime = n;
    let found = false;
    while (!found) {
        prime++;
        if (checkPrime(prime))
            found = true;
        }
    console.log(prime)
    return (prime-n);
}