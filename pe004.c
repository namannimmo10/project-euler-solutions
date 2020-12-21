#include <stdio.h>

int check_palindrome(int n) {
  int t, reverse = 0;
 
  t = n;
 
  while (t != 0) {
    reverse = reverse * 10;
    reverse = reverse + t%10;
    t = t/10;
  }
 
  if (n == reverse)
    return 1;
  else
    return 0;
}

int main() {
  
  long int biggest_palindrome = 0;
  
  // Declaring here and assigning later is more efficient than redeclaring every loop
  long int product;
  
  // Starting b at a so the same cases wont be done twice
  for(int a = 1; a < 1000; a++) {
    for(int b = a; b < 1000; b++) {
      product = a * b;
      if(product > biggest_palindrome) {
        if(check_palindrome(product)) {
          biggest_palindrome = product;
        }
      }
    }
  }
  
  printf("%u", biggest_palindrome);
  
  return 0;
}
