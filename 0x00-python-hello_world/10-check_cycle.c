#include "lists.h"

/**
 * check_cycle - a function that checks if a singly-linked list has a cycle in
 * it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list; /* both pointers should point to the start of the list */

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next; /* move tortoise one step forward */
		hare = hare->next->next; /* move hare two steps forward */
		if (hare == tortoise) /* they meet at a point */
		{
			tortoise = list; /* reset tortoise to start of list */
			while (tortoise != hare)
			{
				/*
				 * move both pointers at the same pace, one
				 * step at a time till they meet again. meeting
				 * point is the start of the cycle.
				 */
				tortoise = tortoise->next;
				hare = hare->next;
			}
			return (1); /* cycle has been detected */
		}
	}
	return (0); /* no cycle has been detected */
}
