#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Desc: Time complexity O(n), Space complexity O(n)
 * Return: 0 if the  list is not a palindrome else 1
 */

int is_palindrome(listint_t **head)
{
	int *stack, size = 0;
	listint_t *current;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		size++;
	}
	stack = malloc(sizeof(int) * size);
	if (stack == NULL)
		return (-1);
	current = *head, size = 0;
	while (current != NULL)
	{
		stack[size++] = current->n;
		current = current->next;
	}
	size--;
	current = *head;
	while (current != NULL)
	{
		if (current->n != stack[size--])
		{
			free(stack);
			return (0);
		}
		current = current->next;
	}
	free(stack);
	return (1);
}
