
// ci = (pi + k) % 26

#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char* argv[]) {

    // Check for valid command-line arguments
    if (argc <> 2) {
        printf("Usage: ./caesar [key]\n");
        return 1;
    }

    int k = atoi(argv[1]) % 26;
    char* p = GetString();

    for (int i = 0, n = strlen(p); i < n; i++) {

        // Cipher Alpha Only
        if ( isalpha(p[i]) ) {

            if ( (isupper(p[i]) && p[i] + k > 90) | (islower(p[i]) && p[i] + k > 122) ) {
                printf("%c", p[i] + k - 26);
            } else {
                printf("%c", p[i] + k);
            }

        } else {
            printf("%c", p[i]);   // Non-alpha
        }
    }
    printf("\n");   // End line
    return 0;
}
