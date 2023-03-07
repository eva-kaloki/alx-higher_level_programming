/**
 * insert_node - inserts a node with the given number into a sorted singly linked list
 * @head: pointer to the head of the linked list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current = *head;
    listint_t *prev = NULL;

    if (!new_node) /* check if malloc fails */
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (!*head) /* if list is empty */
    {
        *head = new_node;
        return (new_node);
    }

    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (!prev) /* if number is less than first element */
    {
        new_node->next = *head;
        *head = new_node;
    }
    else /* insert new_node in between prev and current */
    {
        prev->next = new_node;
        new_node->next = current;
    }

    return (new_node);
}

