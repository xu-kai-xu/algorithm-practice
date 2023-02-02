/* 142 有效的字母异位词 */
#include <stdio.h>
#include <stdlib.h>

typedef enum
{
    false,
    true
} bool;

int isAnagram(char *s, char *t);

int main()
{
    char *s = "rat";
    char *t = "car";
    bool res = isAnagram(s, t);
    printf("%d\n", res);
    system("Pause");
    return 0;
}

int isAnagram(char *s, char *t)
{
    int word[26] = {0};
    for (int i = 0; *(s + i) != '\0'; i++)
    {
        word[*(s + i) - 97] += 1;
    }

    for (int j = 0; *(t + j) != '\0'; j++)
        word[*(t + j) - 97] -= 1;

    for (int k = 0; k < 26; k++)
        if (word[k] != 0)
            return false;
    return true;
}
