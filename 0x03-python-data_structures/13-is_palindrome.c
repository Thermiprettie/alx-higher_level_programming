#include "lists.h"

/**
 * is_palindrome - checks palindrome
 * @head: code head
 * Return: 0, or 1, if otherwise
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL|| *head == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (0);
}
