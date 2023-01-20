class Solution:
    def removeZeroSumSublists(self, head):
        # A: nodes found
        # S: Running Sum values (always unique, since duplicates triger cleanup)
        # d: Companion dictionary for "S" (allows quick O(1) access).
        #    Entries are d[cumulative_sum] = index 
        # t: Current Running sum
        nodes, running_sums, sum_dict, current_sum = [], [], {0: -1}, 0
        
        # Iterate over linked list
        current_node = head
        while current_node:
            current_sum += current_node.val
            if current_sum in sum_dict:
                # Running sum seen before, trigger cleanup
                for _ in range(sum_dict[current_sum]+1, len(nodes)):
                    nodes.pop()
                    sum_dict.pop(running_sums.pop())
                current_sum = running_sums[-1] if running_sums else 0
            else:
                # Append new cumulative sum (unseen before)
                nodes.append(current_node)
                running_sums.append(current_sum)
                sum_dict[current_sum] = len(nodes) - 1
            current_node = current_node.next
        
        # Fix linked list pointers
        nodes.append(None)
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i+1]
        return nodes[0]