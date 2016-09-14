#include <stdio.h>

int main()
{
	float a, b, e, i;
	b = -1;

	printf("Enter starting degrees: ");
	scanf("%f", &a);

	printf("Enter ending degrees: ");
	scanf("%f", &e);

	printf("Enter degree increment: ");
	scanf("%f", &i);

	printf("\n\nFarenheit to Celsius Conversion:\n");
	while (a <= e)
	{
		if ((a > 98.6) && (b < 98.6))
		{
			printf("%6.2f degrees F = %6.2f degrees C\n",
				98.6, (98.6 - 32.0) * 5.0 / 9.0);
		}
		printf("%6.2f degrees F = %6.2f degrees C\n",
			a, (a - 32.0) * 5.0 / 9.0);
		b = a;
		a = a + i;
	}
	return 0;
}