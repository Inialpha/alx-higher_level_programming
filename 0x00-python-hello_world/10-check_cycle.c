#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: pointer to the begining of linked list
 * Return: 0 if no cycle 1 if cycle exits
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	if (fast != NULL)
	{
		if (fast->next == NULL)
			return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			break;
	}
	if (fast == NULL)
		return (0);

	return (1);
}
