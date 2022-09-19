#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *sloth, *flash;

	if (list == NULL || list->next == NULL)
		return (0);

	sloth = list->next;
	flash = list->next->next;

	while (sloth && flash && flash->next)
	{
		if (sloth == flash)
			return (1);

		sloth = sloth->next;
		flash = flash->next->next;
	}
	return (0);
}
