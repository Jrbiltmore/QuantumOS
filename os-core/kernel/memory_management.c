// os-core/kernel/memory_management.c

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct MemoryBlock {
    size_t size;
    void* base;
    bool isFree;
    struct MemoryBlock* next; // For linking free blocks
} MemoryBlock;

#define MAX_BLOCKS 1024
MemoryBlock memoryPool[MAX_BLOCKS];
MemoryBlock* freeList = NULL; // Head of the free list

void initialize_memory_system() {
    for (int i = 0; i < MAX_BLOCKS; ++i) {
        memoryPool[i].size = 0;
        memoryPool[i].base = NULL;
        memoryPool[i].isFree = true;
        memoryPool[i].next = (i < MAX_BLOCKS - 1) ? &memoryPool[i + 1] : NULL;
    }
    freeList = &memoryPool[0];
    printf("Memory system initialized with advanced features.\n");
}

// Finds the best fitting block for the requested size, returns NULL if none found
MemoryBlock* find_best_fit(size_t size) {
    MemoryBlock *bestFit = NULL, *prev = NULL, **bestPrev = NULL;
    for (MemoryBlock** curr = &freeList; *curr; curr = &((*curr)->next)) {
        if ((*curr)->isFree && (*curr)->size >= size && (!bestFit || (*curr)->size < bestFit->size)) {
            bestFit = *curr;
            bestPrev = curr;
        }
    }
    if (bestFit) {
        if (bestPrev) {
            *bestPrev = bestFit->next; // Remove from free list
        }
        bestFit->isFree = false;
        bestFit->next = NULL; // Remove next pointer for allocated block
    }
    return bestFit;
}

void* allocate_memory(size_t size) {
    MemoryBlock* block = find_best_fit(size);
    if (!block) {
        printf("Failed to find a fitting block. Attempting to allocate new block.\n");
        for (int i = 0; i < MAX_BLOCKS; ++i) {
            if (memoryPool[i].size == 0) { // Unused block found
                memoryPool[i].base = malloc(size);
                if (memoryPool[i].base) {
                    memoryPool[i].size = size;
                    memoryPool[i].isFree = false;
                    printf("Allocated %zu bytes in new block.\n", size);
                    return memoryPool[i].base;
                } else {
                    printf("System out of memory.\n");
                    return NULL;
                }
            }
        }
        printf("Memory pool is full.\n");
        return NULL;
    } else {
        printf("Allocated %zu bytes in existing block.\n", size);
        return block->base;
    }
}

void free_memory(void* ptr) {
    for (int i = 0; i < MAX_BLOCKS; ++i) {
        if (memoryPool[i].base == ptr) {
            memoryPool[i].isFree = true;
            printf("Memory block at %p freed.\n", ptr);
            // Add the block back to the free list for reuse
            memoryPool[i].next = freeList;
            freeList = &memoryPool[i];
            return;
        }
    }
    printf("Pointer %p not found in memory pool.\n", ptr);
}

int main() {
    initialize_memory_system();
    void* ptr1 = allocate_memory(100);
    void* ptr2 = allocate_memory(200);
    void* ptr3 = allocate_memory(300);

    free_memory(ptr2); // Free the second block
    void* ptr4 = allocate_memory(150); // This should ideally reuse the freed block

    // Cleanup and exit
    free_memory(ptr1);
    free_memory(ptr3);
    free_memory(ptr4);

    return 0;
}
