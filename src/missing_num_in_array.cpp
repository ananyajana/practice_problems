/*  Missing number in array problem.

We can do this in the following way. We calculate the sum of all
numbers till N i.e. (N * (N  + 1)) /2 and then keep on subtracting
each input. We don't even  need to store the elements.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, T, sum,cur;
	N = T = 0;
	int * arr = NULL;	// dynamic array to hold the array elements
	
	
    
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		
		sum = cur = 0;
		
		scanf("%d", &N); // scanning the number of elements in the array
		
		sum = ( N * ( N + 1)) / 2;	// calculating the sum from 1 to N
		
		
		for(int n = 0; n < (N - 1); ++n){
	   		scanf("%d", &cur);	// scanning the elements of the array one by one and 
	   		sum = sum - cur;	// subtracting them from the sum
		}

		printf("%d\n", sum);	//this prints the missing number
	}
}
