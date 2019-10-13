#include <stdio.h>

int main() {
  unsigned long int previous_fibonacci = 0;
  unsigned long int current_fibonacci = 1;
  
  // temp variable to swap variable; declaring here faster than redeclaring every time
  unsigned long int temp;
  
  unsigned long int sum;
	
	while(current_fibonacci < 4000000) {
	  if(current_fibonacci % 2) {
	    sum += current_fibonacci;
	  }
	  
	  // updating current_fibonacci
	  temp = current_fibonacci;
	  current_fibonacci += previous_fibonacci;
	  previous_fibonacci = temp;
	}
	
  printf("%u", sum);
}
