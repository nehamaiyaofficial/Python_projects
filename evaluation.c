#include <stdio.h>

int main(void) {
    int branch;

    printf("Choose a BTech branch (1-4):\n");
    printf("1. AIML\n2. CSE\n3. ECE\n4. Biotechnology\n");
    printf("Enter your choice: ");

    if (scanf("%d", &branch) != 1) {
        printf("Invalid input!\n");
        return 1;
    }

    switch (branch) {
        case 1:
            printf("BTech AIML - Amity University\n");
            break;
        case 2:
            printf("BTech CSE\n");
            break;
        case 3:
            printf("BTech ECE\n");
            break;
        case 4:
            printf("BTech Biotechnology\n");
            break;
        default:
            printf("Please choose a number from 1 to 4.\n");
    }

    return 0;
}
