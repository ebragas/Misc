
// ci = (pi + k) % 26

#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

void cipher(char c, int key);

int main(int argc, char* argv[]) {

    // Check for valid arguments
    if (argc != 2) {
        printf("Usage: ./caesar [key]\n");
        return 1;
    }

    int k = atoi(argv[1]) % 26;

    // Check key is non-negative
    if (k < 0) {
      printf("Key must be non-negative\n");
    }

    // Get string; Check not null
    char* p = GetString();

    if (p != NULL) {

      // Loop through string; Encrypt if alpha (preserve case); Print standard out
      for (int i = 0, n = strlen(p); i < n; i++) {

          // Cipher Alpha Only
          if ( isalpha(p[i]) ) {

              if ( (isupper(p[i]) && p[i] + k > 90) | (islower(p[i]) && p[i] + k > 122) ) {
                  cipher(p[i], k - 26);
              } else {
                  cipher(p[i], k);
              }

          } else {
              cipher(p[i], 0);   // Non-alpha
          }
      }
    }

    printf("\n");   // End line
    return 0;
}

// Function: Print character offset by key
void cipher(char c, int key) {
  printf("%c", c + key);
}
