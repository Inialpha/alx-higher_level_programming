#include "lists.h"

/**
 * get_index - gets the index
 * @head: head of list
 * @num: number to be inserted
 * Return: index
 */

int get_index(listint_t *head, int num)
{
	listint_t *temp = head;
	int i = 0;

	while (temp != NULL && temp->n < num)
	{
		i++;
		temp = temp->next;
	}
	return (i);
}

/**
 * insert_node - insert node in a sorted LL
 * @head: the pointer to the first node in LL
 * @number: data to be inserted
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;
	int index, i;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	index = get_index(*head, number);
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		temp = *head;
		for (i = 0; i < index - 1; i++)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
