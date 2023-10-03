#include "lists.h"

/**
 * check_cycle - this checks if a linked list contains a cycle
 * @list: the linked list to check
 * Return: it returns 1 if there's a cycle found in the list, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if(slow == fast)
			return (1);
	}

	return (0);
}
