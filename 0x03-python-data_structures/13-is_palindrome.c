#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - check if a singly linked list of integer is palindrome
 * @head: pointer first element of the linked list.
 *
 * Return: 1 if the singly linked list is palidrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int i = 0, index = 0;
	int arr[4096];

	if (!head)
		return (0);

	for (index = 0; aux; index++)
	{
		arr[index] = aux->n;
		aux = aux->next;
	}

	while (i < index)
	{
		if (arr[i] != arr[index - 1])
		{
			return (0);
		}
		i++;
		index--;
	}
	return (1);
}
