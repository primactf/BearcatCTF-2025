#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>


void store_a_charstar();
void menu();
void vuln();
void store_floats();
int key1 = 0;
int key2 = 0;
int key3 = 0;
int floatcount = 0;

void setup() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stderr, 0, _IONBF, 0);
}

int main(int argc, char **argv) {
    setup();
    menu();
    vuln();
}

void win() {
    FILE *f;
    char c;
    f = fopen("flag.txt", "rt");
    if (key1 != 27000 && key2 != 0xbadf00d && key3 != 0x1337){
        fclose(f);
        exit(1);
    }

    while ( (c = fgetc(f)) != EOF ) {
        printf("%c", c);
        fflush(stdout);
    }
    fclose(f);

}
void set_key1() {
    if (key3 != 0)
        key1 = 27000;
}

void ahhhhhhhh() {
    if (key1 == 0)
        return;
    key3 = 0;
    key2 = key2 + 0xbad0000;
}

void food() {
    key2 = key2 + 0xf00d;
}

void number3() {
    key3 = 0x1337;
}

void menu() {
    puts("Try out this new calling convention!");
    puts("Instead of calling functions directly, you just return to them instead!");
    printf(" > ");
}

void vuln() {
    fflush(stdout);
    char s[8];
	fgets(s, 0x200, stdin);
}

