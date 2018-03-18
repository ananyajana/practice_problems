/*  Spirally traversing a generic matrix R*C

Author:Ananya Jana
*/

#include <stdio.h>
#include <stdlib.h>

#define	R		4
#define	C		4


int main()
{
	int M, N, T, i, j, increase, k, l, m, n;
	N = T = i = increase = 0;
	int a[R][C];
	scanf("%d", &T);

	for(int t = 1; t <= T; ++t){		
		for(i = 0; i < R; ++i){
			for(j = 0; j < C; ++j)
	   			scanf("%d", &a[i][j]); // scanning the elements of the array one by one
		}
		
		k = l = 0;
		m = R;
		n = C;
		while((k < m) && (l < n)){
			// print the first row from the remaining matrix		
			for(i = l; i < n; ++i)
				printf("%d ", a[k][i]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			++k;
			
			// print the last column from the remaining matrix
			for(i = k; i  < m; ++i)
				printf("%d ", a[i][n - 1]);
				//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
			--n;
			
			// print the last row from the remaining matrix
			if ( k < m){
				for(i = n - 1; i >= l; --i)
					printf("%d ", a[m - 1][i]);
					//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
				--m;
			}
			
			// print the first column from the remaining matrix
			if (l < n){
				for(i = m - 1; i >= k; --i)
					printf("%d ", a[i][l]);
					//printf("a[%d][%d] = %d \n", i, j, a[i][j]);
				++l;
			}
		}
		printf("\n");
	}
}

