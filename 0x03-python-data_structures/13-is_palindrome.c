#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: list a pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *re = *head, *aux = *head, *list = NULL, *ptr = NULL;

	if (*head == NULL)
	{
		return (1);
	}
	while (re != NULL)
	{
		ptr = re->next;
		re->next = list;
		list = re;
		re = ptr;
	}
	while (list != NULL && aux != NULL)
	{
		if (list->n == aux->n)
		{
			list = list->next;
			aux = aux->next;
		}
		else
		{
			return (0);
		}
	}
	free_listint(re);
	free_listint(aux);
	/*free_listint(list);*/
	free_listint(ptr);
	return (1);
}
