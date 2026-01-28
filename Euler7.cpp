#include <vector>
#include <iostream>

using namespace std;

// checks if a number is prime
static bool isPrime(unsigned long long N) {
    if (N < 11) {
        static bool first_nums[11] = {
        false, false, true, true, false, true, 
        false, true, false, false, false
        };
        return first_nums[N];
    }
    if (N % 2 == 0) {return false;}
    if (N % 3 == 0) {return false;}
    unsigned long long p = 5;
    while (p*p <= N) {
        if (N % p == 0) {return false;}
        if (N % (p+2) == 0) {return false;}
        p += 6;
    }
    return true;
}

// dumb version cycling through all numbers with step 2
// keeping the primes in a vector
int main(){
    cout << "Enter an integer (10 000 000 takes ~230 sec)" << endl;
    unsigned long long n;
    cin >> n;
    clock_t c_start = clock();
    vector<unsigned long long> primes = {2};
    vector<unsigned long long>::iterator itr;
    unsigned long long test = 3;
    while (primes.size() <= n) {
        if (isPrime(test)) {primes.push_back(test);}
        test += 2;
    }
    clock_t c_end = clock();
    cout << "the " << n << " prime is " << primes[n-1] << endl;
    cout << endl;
    cout << 1000.0*(c_end - c_start) / CLOCKS_PER_SEC << " ms\n";
    cout << (c_end - c_start) / CLOCKS_PER_SEC << " sec\n";
    return 0;
}

