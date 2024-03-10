// os-core/kernel/scheduler.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define MAX_TASKS 10

typedef struct Task {
    int taskID;
    void (*taskFunction)(void*);
    void* taskArgs;
    time_t scheduledTime;
} Task;

Task taskQueue[MAX_TASKS];
pthread_mutex_t queueMutex;

void initialize_scheduler() {
    pthread_mutex_init(&queueMutex, NULL);
    for (int i = 0; i < MAX_TASKS; i++) {
        taskQueue[i].taskID = -1; // Indicates that the task slot is empty
    }
    printf("Scheduler initialized.\n");
}

int schedule_task(void (*taskFunction)(void*), void* args, time_t runAt) {
    pthread_mutex_lock(&queueMutex);
    for (int i = 0; i < MAX_TASKS; i++) {
        if (taskQueue[i].taskID == -1) {
            taskQueue[i].taskID = i;
            taskQueue[i].taskFunction = taskFunction;
            taskQueue[i].taskArgs = args;
            taskQueue[i].scheduledTime = runAt;
            pthread_mutex_unlock(&queueMutex);
            printf("Task %d scheduled.\n", i);
            return i;
        }
    }
    pthread_mutex_unlock(&queueMutex);
    printf("Failed to schedule task. Task queue is full.\n");
    return -1;
}

void execute_tasks() {
    while (1) {
        pthread_mutex_lock(&queueMutex);
        time_t now = time(NULL);
        for (int i = 0; i < MAX_TASKS; i++) {
            if (taskQueue[i].taskID != -1 && taskQueue[i].scheduledTime <= now) {
                taskQueue[i].taskFunction(taskQueue[i].taskArgs);
                taskQueue[i].taskID = -1; // Mark as executed
                printf("Task %d executed.\n", i);
            }
        }
        pthread_mutex_unlock(&queueMutex);
        sleep(1); // Polling interval
    }
}

void cleanup_scheduler() {
    pthread_mutex_destroy(&queueMutex);
    printf("Scheduler cleanup complete.\n");
}

// Example task function
void exampleTask(void* arg) {
    printf("Executing example task with arg: %s\n", (char*)arg);
}

int main() {
    initialize_scheduler();
    time_t now = time(NULL);
    schedule_task(exampleTask, "Task argument", now + 5); // Schedule to run 5 seconds from now

    // Start a thread to execute tasks
    pthread_t execThread;
    pthread_create(&execThread, NULL, (void*)execute_tasks, NULL);
    
    // Simulate running for some time
    sleep(10);
    
    cleanup_scheduler();
    pthread_cancel(execThread);
    pthread_join(execThread, NULL);
    return 0;
}
