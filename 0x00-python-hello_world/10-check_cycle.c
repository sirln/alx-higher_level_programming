#include "lists.h"

/**
  *check_cycle - finds loop in a linked list
  *
  *@list: pointer to head of list
  *
  *Return: 0 if there is no cycle, 1 if there is a cycle
  *
  */

int check_cycle(listint_t *list)
/*listint_t *find_listint_loop(listint_t *head)*/
{
	listint_t *temp, *tmp;

	temp = list;
	tmp = list;
	while (temp && temp->next)
	{
		tmp = tmp->next;
		temp = temp->next->next;
		if (tmp == temp)
		{
			tmp = list;
			while (tmp != temp)
			{
				tmp = tmp->next;
				temp = temp->next;
			}
			return (1);
		}
	}
	return (0);
}
