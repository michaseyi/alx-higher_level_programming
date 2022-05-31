#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: the number to be added to the linked list
 * Desc:
 * Time complexity O(n) worstcase 0(1) bestcase
 * Space complexity 0(1)
 * Return: NULL if it fails to insert else the address of the inserted
 * node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev = NULL;

	if (head == NULL)
		return (NULL);
	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	while (current && !(current->n >= number) && current->next)
	{
		prev = current;
		current = current->next;
	}
	if (current == *head)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else if (number > current->n)
		current->next = new_node;
	else
	{
		new_node->next = current;
		prev->next = new_node;
	}
	return (new_node);
}
