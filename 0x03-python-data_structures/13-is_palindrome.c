#include "lists.h"

/**
 * listint_len - a function that counts and returns the number
 * of elements in a linked list
 * @h: pointer to the head node
 * Return: number of nodes
*/

size_t listint_len(const listint_t *h)
{
    size_t numDigits = 0;

    while (h)
    {
        numDigits++;
        h = h->next;
    }

    return (numDigits);
}

/**
 * is_palindrome_recursion - a function that recursively checks the
 * candidacy of a string to be a palindrome
 * @left: pointer to head of list
 * @right: first character to check
 * @length: last character to check
 * Return: 1 if palindrome, 0 if not palindrome
*/

size_t is_palindrome_recursion(listint_t **left, listint_t *right, size_t length)
{
    size_t palindrome;

    if (right == NULL || length == 0)
        return (1);
    
    if (length == 1)
    {
        *left = (*left)->next;
        return (1);
    }

    palindrome = is_palindrome_recursion(left, right->next, length - 1);
    if (!palindrome)
        return (0);

    palindrome = ((*left)->n == right->n);
    *left = (*left)->next;

    return (palindrome);
}

/**
 * is_palindrome - a function that checks if a linked list is a palindrome
 * using recursion
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not palindrome
*/

int is_palindrome(listint_t **head)
{
    size_t length = listint_len(*head);

    return (is_palindrome_recursion(head, *head, length));
}
