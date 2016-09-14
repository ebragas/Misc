#include <stdio.h>

int main()
{
	int a, b, c;	// declaring variables
	printf("Enter the first value:\n");
	scanf("%d", &a);
	printf("Enter the second value:\n");
	scanf("%d", &b);
	c = a + b;
	printf("%d + %d = %d\n", a, b, c);
	return 0;
}