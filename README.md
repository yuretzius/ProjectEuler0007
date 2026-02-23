# ProjectEuler0007
My work on

[problem #7 of projecteuler.net](https://projecteuler.net/problem=7):

### 10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number ?

*Completed on Sat, 20 Feb 2021, 22:39*

> [!NOTE]
> Project Euler's policy allows publication of solutions for the first 100 problems, that's why I am sharing my work here for reference and educational purposes.

For a simple test of primeness we can use the following facts:

1. All numbers divisible by 2 and 3 (except for 2 and 3 themselves) are composite.

2. This means that above 3 all primes must be in the form 6k+1 or 6k-1, with k = 1,2,3...

3. For any number N the divisibility only needs to be checked for p such that p * p <= N.
Because apart from N itself a number can only have one divisor above sqrt(N), and if it does, then it also has a divisor below sqrt(N),
so checking for it is not necessary. E.g. for 55 = 5 * 11 floor(sqrt(55)) = 7, and it is enough to check for a divisor below 7 to find 5,
looking for 11 is excessive.

I've slightly improved Erat(N) from [problem 5](https://github.com/yuretzius/ProjectEuler0005) and created EratM(N) which immediately eliminates doubles and triples,
and then only checks pairs p and p+2 with step 6. The inconvenience of this function is that it lists all primes below or equal to N,
so it is excessive for the task of this problem and also we need to know up to which number to populate the array to reach the required nth prime.
But I see no point to write a special version just to look for the nth prime.

For a test I use N = 2*10**8 and look for 10 000 001th prime. The result is 11 078 937 primes below 200 000 000,
and 10 000 001th prime is 179 424 691. EratM performes only slightly better: Erat: 13.94s EratM: 13.87s.

In C++ code I create a more or less efficient function isPrime(N) to test for primeness using the rules above,
but then use it in a rather inefficient manner, just cycling through numbers with step 2 and checking for primeness,
keeping the resulting primes in a vector. I tried just counting primes and keeping only the last one, but that did
not change much. Same 10 000 001th prime is found in about ~230s.
