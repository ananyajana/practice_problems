/*  Spirally traversing a generic matrix R*C

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define	MATRIX_SZ	4


int main()
{
	int M, N, T, i, j, increase, k, l, m, n;
	N = T = i = increase = 0;
	int a[MATRIX_SZ][MATRIX_SZ];	// dynamic array to hold the array elements, the highest elements to the left and right
	
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		for(i = 0; i < MATRIX_SZ; ++i){
			for(j = 0; j < MATRIX_SZ; ++j)
	   			scanf("%d", &a[i][j]); // scanning the elements of the array one by one
		}
		
		k = l = 0;
		m = n = MATRIX_SZ;
		
		while((k < m) && (l < n)){		
			for(i = 0; i < n; ++i)
				printf("%d ", a[k][i]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			++k;
			for(i = k; i  < m; ++i)
				printf("%d ", a[i][m - 1]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			--m;
			for(i = m - 1; i >= l; --i)
				printf("%d ", a[n - 1][i]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			--n;
			for(i = n - 1; i > k; --i)
				printf("%d ", a[i][l]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			++l;
		}
		printf("\n");
	}
}

