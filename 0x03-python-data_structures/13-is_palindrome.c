#include "lists.h"
#include <stdlib.h>

/**
 * reverse - reverses a linked list
 * @head: Pointer to the head of the linked list
 * Return:  Pointer to the new head of the list
 */

listint_t *reverse(listint_t *head)
{
	listint_t *current, *next, *prev = NULL;

	current = head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Desc: Time complexity O(n), Space complexity O(n)
 * Return: 0 if the  list is not a palindrome else 1
 */

int is_palindrome(listint_t **head)
{
	int size = 0, rev_size, i;
	listint_t *current, *prev, *rev, *rev_temp;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		size++;
	}
	rev_size = size / 2;
	current = *head;
	while (i++ < size - rev_size)
	{
		prev = current;
		current = current->next;
	}
	rev = reverse(current);
	current = *head;
	rev_temp = rev;

	while (rev_temp != NULL)
	{
		if (rev_temp->n != current->n)
		{
			prev->next = reverse(rev);
			return (0);
		}
		rev_temp = rev_temp->next;
		current = current->next;
	}
	prev->next = reverse(rev);
	return (1);
}
