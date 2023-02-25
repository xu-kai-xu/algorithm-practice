/* */
#include <stdio.h>
#include <stdlib.h>

void reverseString(char *s, int sSize) {
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

int main()
{
    char s1[5] = {'h','e','l','l','o'};
    int size_s1 = 5;
    char s2[6] = {'H','a','n','n','a','h'};
    int size_s2 = 6;
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    reverseString(s1, size_s1);
    reverseString(s2, size_s2);
    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    system("Pause");
    return 0;
}
