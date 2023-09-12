from typing import List
from pathlib import Path


class Stmt:
    def __init__(self):
        self.kind = None

    def __str__(self):
        return self.kind

    def __repr__(self):
        return self.__str__()

class Program:
    def __init__(self):
        self.kind: str = "program"
        self.body: List[Stmt] = []


class Extends(Stmt):
    def __init__(self, file_path: str):
        super().__init__()
        self.kind = "extends"
        self.f_path = Path(file_path)

        if not self.f_path.exists():
            raise Exception("File path not found")

    def file_content(self):
        return self.f_path.read_text('utf-8')


class Include(Extends):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.kind = "include"


class Block(Stmt):
    def __init__(self, block_name: str, data: List[Stmt]):
        super().__init__()
        self.kind = 'block'
        self.name = block_name
        self.block_data = data


class python(Stmt):
    def __init__(self, code: str):
        super().__init__()
        self.kind = 'python'
        self.code = code


class html(Stmt):
    def __init__(self, code: str):
        super().__init__()
        self.kind = 'html'
        self.code = code


class Pass(Stmt):
    def __init__(self):
        super().__init__()
        self.kind = 'pass'


class End(Stmt):
    def __init__(self):
        super().__init__()
        self.kind = 'end'