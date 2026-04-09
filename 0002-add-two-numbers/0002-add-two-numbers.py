class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        n2 = []
        
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        
        n1.reverse()
        n2.reverse()
        
        num1 = 0
        num2 = 0
        for i in n1:
            num1 = num1 * 10 + i
        for i in n2:
            num2 = num2 * 10 + i
        
        total = num1 + num2
        
        digits = [int(digit) for digit in str(total)]
        digits.reverse()
        dummy = ListNode(0)
        current = dummy
        
        for digit in digits:
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next