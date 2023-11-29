#include "lists.h"

/**
 * insert_node - a function that inserts a new node at a given position/index
 * @head: double pointer to the content of the memory pointed to by the pointer
 * held by head
 * @number: value to insert at designated index
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currentNode;
	unsigned int i, idx = 5;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (idx == 0 || *head == NULL)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	currentNode = *head;
	for (i = 0; currentNode != NULL && i < idx - 1; i++)
		currentNode = currentNode->next;

	newNode->next = currentNode->next;
	currentNode->next = newNode;
	return (newNode);
}
