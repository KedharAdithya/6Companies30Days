class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank = set(bank)
        queue = [(startGene, 0)]
        visited = set()
        
        while queue:
            gene, level = queue.pop(0)
            if gene in visited:
                continue
            visited.add(gene)
            if gene == endGene:
                return level
            
            for i in range(len(gene)):
                for c in "ACGT":
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene in bank:
                        queue.append((new_gene, level+1))
        return -1