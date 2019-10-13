#include <stdio.h>

int main() {
  unsigned int sum = 0;

  for(unsigned int i = 0; i < 1000; i++) {
    if (i % 5 == 0 || i % 3 == 0) {
      sum += i;
    }
  }

  printf("%u", sum);
	
  return 0;
}
