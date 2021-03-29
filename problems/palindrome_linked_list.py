def is_palindrome_linked_list(self, head: ListNode) -> bool:
    val_list = []

    while head:
        val_list.append(head.val)
        head = head.next

    return val_list == val_list[::-1]
