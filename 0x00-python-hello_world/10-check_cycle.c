#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - check for the loop in a linked list
 * @list: data type listint_t pointer of list
 * Return: 0 if no cycle || 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first_loop;
	listint_t *second_loop;

	if (list == NULL || list->next == NULL)
		return  (0);

	first_loop = list->next;
	second_loop = list->next->next;

	while (first_loop && second_loop && second_loop->next)
	{
		if (first_loop == second_loop->next)
		{
			return (1);
		}
		first_loop = first_loop->next;
		second_loop = second_loop->next->next;
	}
	return (0);
}
