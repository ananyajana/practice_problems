/*  Spirally traversing a matrix 4*4

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define	MATRIX_SZ	16


int main()
{
	int M, N, T, i, j;
	N = T = i = 0;
	int *a;	// dynamic array to hold the array elements, the highest elements to the left and right
	a = NULL;
	
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		a = (int*)malloc(MATRIX_SZ * sizeof(int));
		
		
		for(i = 0; i < MATRIX_SZ; ++i){
	   		scanf("%d", &a[i]); // scanning the elements of the array one by one
		}
		
		
		
		//freeing up the dynamically allocated memory
		if(a1)
			free(a1);
		
	}
}

