/*  Sort an array of 0s, 1s and 2s.
We can use bucket sort for this.
Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX	4

int main()
{
	int N, T, cur;
	N = T = cur = 0;
	int arr[3] = {0};	

	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){
		
		scanf("%d", &N); // scanning the number of elements in the array
		
		for(int n = 0; n < N; ++n){
	   		scanf("%d", &cur);	// scanning the elements of the array one by one and 
	   		++arr[cur];	// using the currently number as index to increment the count of the respective value 
		}

		for(int i = 0; i < 3; ++i){
			while(0 != arr[i]){
				printf("%d ", i);
				--arr[i];
			}
		}
		printf("\n");
	}
}
