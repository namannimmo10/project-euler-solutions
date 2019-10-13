#include <stdio.h>

bool divisibleByAllInRange(int low, int high, long int n) {
  for(int i = low; i <= high; i++) {
    if(!(n % i == 0)) {
      return false;
    }
  }
  return true;
}

int main() {
  long int i = 1;
  
  while(!divisibleByAllInRange(1, 20, i)){
    i++;
  }
  
  printf("%ld", i);
  
  return 0;
}
