#include "lists.h"

/**
 * check_cycle - Checks if a linked lsit has a cycle in it
 * @list: Pointer to the head of the linked list
 * Desc:
 *                  ---- ALGORITHM ----
 * - Traverse the list with two pointers, a slow and a fast one.
 * - The slow one should move one node at a time
 * - The fast one should move two nodes at a time
 * - If at any point during the iteration any of the the pointers
 *  have a NULL value then there is no cycle in the list
 * - Else if at any point during the iteration they both have the same value
 *   then there is a cycle in the list
 * ---------------------------------------------------------------------
 * Return: 1 if there is a cycle in it else 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	do {
		if (slow == NULL || fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != fast);
	return (1);
}
