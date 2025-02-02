#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#define MAX_LINE_LENGTH 256

uint16_t chksum(char *name)
{
    uint16_t checksum = 0;

    for (int i = 0; name[i]; i++) {
        checksum = checksum * 0x25 + name[i];
    }

    int32_t temp = checksum * 314159269;
    if (temp < 0) temp = -temp;
    temp -= ((uint64_t)((int64_t)temp * 1152921497) >> 60) * 1000000007;
    checksum = temp;

    // reverse nibble order
    checksum =
        ((checksum & 0xf000) >> 12) |
        ((checksum & 0x0f00) >> 4) |
        ((checksum & 0x00f0) << 4) |
        ((checksum & 0x000f) << 12);

    return checksum;
}

int main() {
    FILE *file = fopen("words_alpha.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, MAX_LINE_LENGTH, file) != NULL) {
        for(int i=0; i<MAX_LINE_LENGTH; i++) {
            if(line[i] == 0x0A) line[i] = 0;
            if(line[i] == 0x0D) line[i] = 0;
        }
        if(chksum(line) == 0xd20c) {
            printf("%s\n", line);
        }
    }

    fclose(file);   
    return 0;
}