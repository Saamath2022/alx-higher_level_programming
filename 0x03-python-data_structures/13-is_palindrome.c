#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert - Inserts a new node at the beginning of a linked list
 * @head: Pointer to a pointer pointing to the head of the list
 * @data: Integer data to be inserted into the new node
 *
 * Return: Void
 */
void insert(listNode **head, int data)
{
	listNode *newNode = (listNode *)malloc(sizeof(listNode));

	if (newNode == NULL)
	{
		fprintf(stderr, "Memory allocation failed\n");
		exit(EXIT_FAILURE);
	}
	newNode->data = data;
	newNode->next = *head;
	*head = newNode;
}

/**
 * printList - Prints the elements of a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Void
 */
void printList(listNode *head)
{
	while (head != NULL)
	{
		printf("%d\n", head->data);
		head = head->next;
	}
}

/**
 * reverseList - Reverses a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
ListNode *reverseList(ListNode *head)
{
	ListNode *prev = NULL;
	ListNode *current = head;
	ListNode *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer pointing to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(ListNode **head)
{
	ListNode *slow = *head;
	ListNode *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	ListNode *secondHalf = reverseList(slow);
	ListNode *firstHalf = *head;

	while (secondHalf != NULL)
	{
		if (firstHalf->data != secondHalf->data)
		{
			return (0);
		}
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1)
}

