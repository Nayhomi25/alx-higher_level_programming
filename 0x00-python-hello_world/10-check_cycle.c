#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the linked list
 * Return: 0 if no cycle and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
