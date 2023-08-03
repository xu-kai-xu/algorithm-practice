/* */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseString(char *s, int sSize)
{
    int i = 0;
    int j = sSize - 1;
    int tmp = 0;
    while (i < j) {
        tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        i++;
        j--;
    }
}

char *reverseStr(char *s, int k)
{
    int i = 0;
    while (s[i] != 0) {
        
    }
}

int main()
{
    char str1[] = "abcdefg";
    char str2[] = "abcd";
    char *s1 = malloc(sizeof(char) * (strlen(str1) + 1));
    strcpy(s1, str1);
    int k1 = 2;
    char *s2 = malloc(sizeof(char) * (strlen(str2) + 1));
    strcpy(s2, str2);
    int k2 = 2;
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    reverseString(s1, k1);
    reverseString(s2, k2);
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);

    free(s1);
    s1 = NULL;
    free(s2);
    s2 = NULL;
    system("Pause");
    return 0;
}
