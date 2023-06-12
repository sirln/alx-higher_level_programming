#include "lists.h"

/**
  *is_palindrome - checks if a singly linked list is a palindrome.
  *
  *@head: pointer to pointer to head node
  *
  *Return: 0 or 1
  *
  */

int is_palindrome(listint_t **head)
{
	listint_t *copy;
	int l = 0, s, *num_array;

	if (!(*head))
		return (1);
	copy = *head;
	while (copy != NULL)
	{
		copy = copy->next;
		l++;
	}
	num_array = malloc(sizeof(int) * l);
	if (!num_array)
	{
		return (1);
	}
	copy = *head;
	for (s = 0; s < l; s++)
	{
		num_array[s] = copy->n;
		copy = copy->next;
	}
	for (s = 0; s < l / 2; s++)
	{
		if (num_array[l - 1 - s] != num_array[s])
		{
			free(num_array);
			return (0);
		}
	}
	free(num_array);
	return (1);
}


