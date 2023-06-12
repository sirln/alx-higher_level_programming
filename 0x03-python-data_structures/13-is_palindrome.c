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
	listint_t *slow, *fast;

	if (!(*head) || !((*head)->next))
		return (1);

	fast = slow = *head;

	while (fast &&  fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		fast = reverse_listint(&slow->next);
	else
		fast = reverse_listint(&slow);

	while (fast)
	{
		if (fast->n != (*head)->n)
			return (0);
		*head = (*head)->next;
		fast = fast->next;
	}
	return (1);
}


/**
  *reverse_listint - reverse a list
  *
  *@head: pointer to pointer of head list
  *
  *Return: value of poped element
  */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp1 = NULL, *temp2 = NULL;

	if (!(*head))
		return (*head);

	if ((*head)->next)
	{
		while ((*head)->next)
		{
			temp1 = (*head);
			(*head) = (*head)->next;
			temp1->next = temp2;
			temp2 = temp1;
		}
		(*head)->next = temp1;
	}
	return (*head);
}
