#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list we are checking
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tru = list;
	listint_t *lot = list;

	if (!list)
		return (0);

	while (tru && lot && lot->next)
	{
		tru = tru->next;
		lot = lot->next->next;
		if (tru == lot)
			return (1);
	}

	return (0);
}
