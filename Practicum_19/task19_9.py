class StrandsDNA:
    
    def __init__(self):
        self.all_strands = []
    
    def add_strands(self, strands):
        new_strands = strands.split()
        for s in new_strands:
            self.all_strands.append(s)
    
    def get_max_strands(self):
        if not self.all_strands:
            return ''
        
        max_len = max(len(s) for s in self.all_strands)
        max_strands = [s for s in self.all_strands if len(s) == max_len]
        unique_strands = sorted(set(max_strands))
        
        return ' '.join(unique_strands)
    
    def __str__(self):
        return f"StrandsDNA({self.all_strands})"