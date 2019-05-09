#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: double pointer to address of head of linked list
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	int length = 0;
	int i = 0, j = 0;
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
