#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop to keep the program running
 *
 * Return: Always 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid > 0)
        {
            printf("Zombie process created, PID: %d\n", child_pid);
            /* The parent process gives time to child to become a zombie */
            sleep(1);
        }
        else
        {
            /* Child process */
            exit(0);
        }
    }

    /* Keep the program running */
    infinite_while();

    return (0);
}
