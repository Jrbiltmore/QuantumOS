// os-core/kernel/memory_management.c

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    size_t size;
    void* base;
} MemoryBlock;

#define MAX_BLOCKS 1024
MemoryBlock memoryPool[MAX_BLOCKS];

void initialize_memory_system() {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        memoryPool[i].size = 0;
        memoryPool[i].base = NULL;
    }
    printf("Memory system initialized.\n");
}

void* allocate_memory(size_t size) {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        if (memoryPool[i].size == 0) { // Find an empty block
            memoryPool[i].base = malloc(size);
            if (memoryPool[i].base != NULL) {
                memoryPool[i].size = size;
                printf("Allocated %zu bytes.\n", size);
                return memoryPool[i].base;
            } else {
                printf("Failed to allocate memory.\n");
                return NULL;
            }
        }
    }
    printf("No memory blocks available.\n");
    return NULL;
}

void free_memory(void* ptr) {
    for (int i = 0; i < MAX_BLOCKS; i++) {
        if (memoryPool[i].base == ptr) {
            free(memoryPool[i].base);
            memoryPool[i].base = NULL;
            memoryPool[i].size = 0;
            printf("Memory freed.\n");
            return;
        }
    }
    printf("Pointer not found in memory pool.\n");
}

int main() {
    initialize_memory_system();
    void* ptr1 = allocate_memory(256);
    void* ptr2 = allocate_memory(512);
    
    // Use allocated memory
    
    free_memory(ptr1);
    free_memory(ptr2);
    return 0;
}
