/*
  Output the ASCII values for capital and lowercase alphabet.
*/

#include <stdio.h>

// Number of characters in English alphabet
#define CHARS 26

int main(void) {
  printf("\n ASCII\tChar\n");

  // Lowercase
  for (int i = 97; i < 97 + CHARS; i++)
    printf(" %i\t%c\n", i, (char) i);

  // Uppercase
  for (int i = 65; i < 65 + CHARS; i++)
    printf(" %i\t%c\n", i, (char) i);

  return 0;
}
