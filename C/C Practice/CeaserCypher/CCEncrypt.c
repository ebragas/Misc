/*
  Encrypt text using Ceaser Cypher
  - Each character in the input string is shifted "down" alphabet by
    the number of characters as indicated by the key

  Todo:
  - Handle alphabet looping
  - Accepts negative key values?
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  // Check that arguments were entered correctly
  if (argc < 3 | argc > 3) {
    printf("\nUsage: CCEncrypt.exe [string_to_cipher] [cipher_key]\n");
    return 0;
  }

  char* val = argv[1];
  int key = atoi(argv[2]);

  // Pring encoded string
  for (int i = 0; i < strlen(val); i++) {
    printf("%c", argv[1][i] + key);
  }
  printf("\n");

  return 0;
}
