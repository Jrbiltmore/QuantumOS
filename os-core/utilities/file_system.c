// os-core/utilities/file_system.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILES 1000

typedef struct {
    char *filename;
    char *content;
} FileEntry;

FileEntry file_table[MAX_FILES];
int num_files = 0;

void file_system_init() {
    // File system initialization code
    printf("Initializing file system...\n");
}

void file_system_read_file(char *filename) {
    // Read file contents
    for (int i = 0; i < num_files; ++i) {
        if (strcmp(file_table[i].filename, filename) == 0) {
            printf("Reading file: %s\n", filename);
            printf("Content: %s\n", file_table[i].content);
            return;
        }
    }
    printf("File not found: %s\n", filename);
}

void file_system_write_file(char *filename, char *content) {
    // Write content to file
    if (num_files >= MAX_FILES) {
        printf("File system full, cannot write file: %s\n", filename);
        return;
    }
    file_table[num_files].filename = strdup(filename);
    file_table[num_files].content = strdup(content);
    num_files++;
    printf("Writing to file: %s\n", filename);
    printf("Content: %s\n", content);
}

void file_system_cleanup() {
    // Cleanup file system resources
    for (int i = 0; i < num_files; ++i) {
        free(file_table[i].filename);
        free(file_table[i].content);
    }
    num_files = 0;
    printf("Cleaning up file system...\n");
}
