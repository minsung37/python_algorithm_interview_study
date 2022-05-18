# 리스트를 연결리스트로
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toLinkedList(List):
    head: ListNode = ListNode()
    curr = head
    for r in List:
        print(r)
        node = ListNode(r)
        curr.next = node
        curr = curr.next
    return head.next


toLinkedList([1, 2, 3, 4, 5])