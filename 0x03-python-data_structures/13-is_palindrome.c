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
	listint_t *aux = *head, *aux_2 = *head;
	int n_elements = 0;
	int i = 0, index = 0;
	int *arr;

	if (!head)
		return (0);
	
	for (n_elements = 0; aux; n_elements++)
		aux = aux->next;

	arr = malloc(sizeof(int) * (n_elements + 1));

	if (!arr)
		return (1);

	for (index = 0; aux_2; index++)
	{
		arr[index] = aux_2->n;
		aux_2 = aux_2->next;
	}

	while (i < index / 2)
	{
		if (arr[i] != arr[index - 1])
		{
			free(arr);
			return (0);
		}
		i++;
		index--;
	}
	free(arr);
	return (1);

}
