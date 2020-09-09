#include "lists.h"

/**
 *  element_list - Calcuate the number of nodes in a linked list.
 * @head: head of the linked list.
 *
 * Return: number of nodes of the linked list.
 */
int element_list(listint_t *head)
{
	int count;

	if (!head)
		return (0);

	for (count = 0; head; count++)
		head = head->next;

	return (count);
}

/**
 * is_palindrome - check if a singly linked list of integer is palindrome
 * @head: pointer first element of the linked list.
 *
 * Return: 1 if the singly linked list is palidrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int n_elements = element_list(aux);

	int *arr, index;
	int i = 0;

	arr = malloc(sizeof(int) * n_elements);
	if (!arr)
		return (1);

	for (index = 0; aux; index++)
	{
		arr[index] = aux->n;
		aux = aux->next;
	}

	while (i < index)
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
