#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert number into a sortedf singly linked list
 * @head: pointer to head node of the list
 * @number: number to be inserted into the singly linked list
 * Return: pointer to new node or NULL if process fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (list == NULL || list->n >= number)
	{
		new->next = list;
		*head = new;
		return (new);
	}

	while (list && list->next && list->next->n < number)
		list = list->next;

	new->next = list->next;
	list->next = new;

	return (new);
}
