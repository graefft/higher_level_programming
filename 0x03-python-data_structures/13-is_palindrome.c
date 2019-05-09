#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	int *array;
	int length = 0;
	int i = 0, j;
	listint_t *temp;

	if (!head)
		return (0);
	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		length++;
	}
	array = malloc(sizeof(int) * length);
	if (!array)
		return (0);
	temp = *head;
	while (temp)
	{
		temp = temp->next;
		i++;
		array[i] = temp->n;
	}
	for (i = 0, j = length - 1; i < j; i++, j--)
	{
		if (array[i] != array [j])
			return (0);
	}
	return (1);
}
