class RenderBlock:
    def __init__(self, *, body=None, block_type: str ="html"):
        self.block_type = block_type
        # body is a list because it can have 
        if isinstance(self.body, list):
            self.body = list(body)
        else:
            self.body = body or []
    
    def __eq__(self, other: str):
        return self.block_type == other   
    
    def __add__(self, other):
        return self.body + other.body