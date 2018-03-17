/*  Spirally traversing a matrix 4*4

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define	MATRIX_SZ	4


int main()
{
	int M, N, T, i, j, increase;
	N = T = i = increase = 0;
	int a[MATRIX_SZ][MATRIX_SZ];	// dynamic array to hold the array elements, the highest elements to the left and right
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		for(i = 0; i < MATRIX_SZ; ++i){
			for(j = 0; j < MATRIX_SZ; ++j)
	   			scanf("%d", &a[i][j]); // scanning the elements of the array one by one
		}
		
		i = 0;
		for(j = 0; j < MATRIX_SZ; ++j)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		--j;
		for(i = i + 1; i  < MATRIX_SZ; ++i)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		--i;
		for(j = j - 1; j >= 0; --j)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		++j;
		for(i = i - 1; i > 0; --i)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		++i;
		for(j = j + 1; j < MATRIX_SZ - 1; ++j)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		--j;
		for(i = i + 1; i  < MATRIX_SZ - 1; ++i)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		--i;
		for(j = j - 1; j > 0; --j)
			printf("%d ", a[i][j]);
			//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
		printf("\n");
	}
}

