/* */
#include <stdio.h>
#include <stdlib.h>

char* replaceSpace(char* s)
{
    int count = 0;
    int space = 0;

    for (int i = 0; s[i] != 0; i++) {
        if (s[i] == ' ') {
            space++;
        }
        count++;
    }
    printf("count = %d, space = %d\n", count, space);

    int new_size = count + 2 * space;
    int k = new_size - 1;
    char *new_str = (char *)malloc(sizeof(char) * (new_size + 1));
    new_str[new_size] = 0;
    for (int j = count - 1; j >= 0; j--) {
        if (s[j] == ' ') {
            new_str[k--] = '0';
            new_str[k--] = '2';
            new_str[k--] = '%';
        } else {
            new_str[k--] = s[j];
            // printf("%c ", s[j]);
        }
    }

    return new_str;
}

int main()
{
    char s[] = "We are happy.";
    char *res = NULL;
    
    res = replaceSpace(s);
    printf("%s\n", res);
    free(res);
    res = NULL;
    system("Pause");
    return 0;
}
