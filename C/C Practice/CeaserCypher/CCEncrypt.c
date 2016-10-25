/*
  Encrypt text using Ceaser Cypher
  - Each character in the input string is shifted "down" alphabet by
    the number of characters as indicated by the key

  Todo:
  - Accepts negative key values?
*/

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

  // Check that arguments were entered correctly
  if (argc < 3 | argc > 3) {
    printf("\nUsage: CCEncrypt.exe [string_to_cipher] [cipher_key]\n");
    return 0;
  }

  // Add key value to each character
  for (int i = 0; i < strlen(argv[1]); i++) {
    printf("%c", argv[1][i]);
  }

  printf("\n");
  return 0;
}
