#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  Inserts a number into a sorted singly linked list.
 * @head: adsress of head.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *no = *h, *w;

	w = malloc(sizeof(listint_t));
	if (w == NULL)
		return (NULL);
	w->n = number;

	if (no == NULL || no->n >= number)
	{
		w->next = no;
		*h = w;
		return (w);
	}

	while (no && no->next && no->next->n < number)
		no = no->next;

	w->next = no->next;
	no->next = w;

	return (w);
}
