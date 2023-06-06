#include "lists.h"

/**
  *insert_node - inserts a new node in a sorted list
  *
  *@head: pointer to pointer to head node in list
  *@number: number/node to be added
  *
  *Return: adderess of new node or  NULL
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	tmp = *head;
	if (tmp)
	{
		if (number <= tmp->n)
		{
			new_node->next = tmp;
			*head = new_node;
		}
		else
		{
			while (tmp->next && number > tmp->next->n)
			{
				tmp = tmp->next;
			}
			new_node->next = tmp->next;
			tmp->next = new_node;
		}
	}
	else
		*head = new_node;

	return (new_node);
}
