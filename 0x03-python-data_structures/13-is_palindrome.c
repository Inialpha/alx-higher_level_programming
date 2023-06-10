#include "lists.h"

/**
 * is_palindrome - checks if a LL is a palindrime
 * @head: pointer to the head of the list
 * Return: 0 if it not a palindrome else 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *prev, *next, *slow, *fast;

	slow = fast = *head;
	prev = next = NULL;
	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast)
		slow = slow->next;
	while (slow && prev)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}
	return (1);
}
