#include <stdio.h>

int main() 
{ 
	int b; 
	printf("Enter a value:"); 
	scanf("%d", &b); 
	if (b <= 0)
	{
		if (b == 0)
			printf("The value is zero.\n");
		else
			printf("The value is negative.\n");
	}
	else
		printf("The value is positive.\n");
	return 0; 
}