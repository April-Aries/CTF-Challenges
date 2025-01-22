#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

char *find_little_endian(const char *word)
{
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;)
    {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word)
{
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++)
    {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}

int main()
{
    char *challenge_word = calloc(100, sizeof(char));
    fgets(challenge_word, 100, stdin);
    if(challenge_word[strlen(challenge_word)-1]=='\n')	challenge_word[strlen(challenge_word)-1] = 0;

    char *little_endian = find_little_endian(challenge_word);
    char *big_endian = find_big_endian(challenge_word);

    printf("Little Endian: %s\n", little_endian);
    printf("Big Endian: %s\n", big_endian);

    return 0;
}
