#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list a pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list = NULL, *ptr = NULL, *re = *head;
	int i = 0, j = 0;
	int new_list[BUFSIZ];

	if (*head == NULL)
	{
		return (1);
	}
	while (re != NULL)
	{
		new_list[i] = re->n;
		ptr = re->next;
		re->next = list;
		list = re;
		re = ptr;
		i++;
	}
	while (list != NULL)
	{
		if (list->n == new_list[j])
		{
			list = list->next;
			j++;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
