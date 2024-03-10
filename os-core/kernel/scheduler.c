// os-core/kernel/scheduler.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define MAX_TASKS 100

typedef struct {
    int taskId;
    void (*function)(void *);
    void *args;
    time_t executeAt;
    int repeat; // 0 = no repeat, >0 = repeat interval in seconds
} Task;

Task taskQueue[MAX_TASKS];
pthread_mutex_t taskQueueMutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t taskQueueCond = PTHREAD_COND_INITIALIZER;
int schedulerRunning = 1;

void* scheduler_loop(void* arg) {
    while (schedulerRunning) {
        pthread_mutex_lock(&taskQueueMutex);
        time_t now = time(NULL);
        for (int i = 0; i < MAX_TASKS; i++) {
            if (taskQueue[i].function && taskQueue[i].executeAt <= now) {
                taskQueue[i].function(taskQueue[i].args);
                if (taskQueue[i].repeat > 0) {
                    taskQueue[i].executeAt = now + taskQueue[i].repeat;
                } else {
                    taskQueue[i].function = NULL; // Mark task as done
                }
            }
        }
        pthread_cond_wait(&taskQueueCond, &taskQueueMutex); // Wait for next task or new task
        pthread_mutex_unlock(&taskQueueMutex);
    }
    return NULL;
}

void initialize_scheduler() {
    for (int i = 0; i < MAX_TASKS; i++) {
        taskQueue[i].taskId = -1;
    }
    pthread_t schedulerThread;
    pthread_create(&schedulerThread, NULL, scheduler_loop, NULL);
    printf("Scheduler initialized and running.\n");
}

void add_task(void (*function)(void *), void *args, time_t executeAt, int repeat) {
    pthread_mutex_lock(&taskQueueMutex);
    for (int i = 0; i < MAX_TASKS; i++) {
        if (!taskQueue[i].function) {
            taskQueue[i].taskId = i;
            taskQueue[i].function = function;
            taskQueue[i].args = args;
            taskQueue[i].executeAt = executeAt;
            taskQueue[i].repeat = repeat;
            printf("Task %d added.\n", i);
            pthread_cond_signal(&taskQueueCond);
            break;
        }
    }
    pthread_mutex_unlock(&taskQueueMutex);
}

void shutdown_scheduler() {
    schedulerRunning = 0; // Stop scheduler loop
    pthread_cond_broadcast(&taskQueueCond); // Wake up scheduler to exit
    printf("Scheduler shutting down.\n");
}

// Example function to be executed by a task
void example_task_function(void *arg) {
    printf("Example task executed with argument: %s\n", (char *)arg);
}

int main() {
    initialize_scheduler();

    time_t now = time(NULL);
    add_task(example_task_function, "Task 1", now + 5, 0); // Execute once after 5 seconds
    add_task(example_task_function, "Task 2", now + 10, 5); // Execute every 5 seconds

    // Keep the main thread running for a while to see tasks being executed
    sleep(30);

    shutdown_scheduler();
    return 0;
}
