#include <string.h>
#include <stdio.h>

char line[100]; /* Line we are looking at */

int main()
{
    printf("Enter a line: ");
    fgets(line, sizeof(line), sidin);

    printf("The length of the line is: %d\n, strlen(line));
    return (0);
}
