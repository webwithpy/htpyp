from .data.token import Token, Methods
from .helpers.str_helper import remove_quotes
from pathlib import Path
from typing import List


class Lexer:
    def __init__(self):
        ...

    def lex_file(self, file_path: Path | str) -> List[Token]:
        tokens = []
        if isinstance(file_path, str):
            file_path = Path(file_path)

        file_data: List[str] = file_path.read_text().split("\n")

        for line in file_data:
            if "{{" in line:
                l_bracket = line.find("{{")
                r_bracket = line.find("}}")
                # make it so that everything outside the brackets is also parsed
                tokens.append(Token(data=line[0:l_bracket], method=Methods.HTML))
                tokens.append(
                    Token(data=line[r_bracket + 2 : len(line)], method=Methods.HTML)
                )
                line = self.__filter_pyht(line=line[l_bracket + 2 : r_bracket])

                if line.startswith("include"):
                    line = line[len("include"): len(line)]
                    line = remove_quotes(line.replace(' ', ''))
                    tokens.append(Token(data=line, method=Methods.INCLUDE))
                elif line.startswith("extends"):
                    line = line[len("extends"): len(line)]
                    line = remove_quotes(line.replace(' ', ''))
                    tokens.append(Token(data=line, method=Methods.EXTENDS))
                elif line.startswith("block"):
                    line = line[len("block"): len(line)]
                    line = line.replace(' ', '')
                    tokens.append(Token(data=line, method=Methods.BLOCK))
                elif line == "pass":
                    line = line[len("pass"): len(line)]
                    tokens.append(Token(data=line, method=Methods.PASS))
                elif line == "end":
                    line = line[len("end"): len(line)]
                    tokens.append(Token(data=line, method=Methods.PASS))
                else:
                    tokens.append(Token(data=line, method=Methods.PYTHON))
            else:
                tokens.append(Token(data=line, method=Methods.HTML))

        tokens.append(Token(data="EOF", method=Methods.EOF))

        return self.filter_tokens(tokens)

    def filter_tokens(self, tokens: List[Token]) -> List[Token]:
        index = 0
        while index < len(tokens):
            token = tokens[index]

            if token.method != Methods.HTML and token.method != Methods.PYTHON:
                index += 1
                continue

            filtered_data = token.data.replace(' ', '').replace('\n', '')
            if filtered_data == '' and len(filtered_data) == 0:
                tokens.pop(index)
                index -= 1
            index += 1

        return tokens


    def __filter_pyht(self, line: str):
        """
        filters all unnecessary data from line
        :param line: line given in html file
        :return:
        """
        line = line.replace("{{", "").replace("}}", "")
        line = line.lower()
        return line.strip(" ")
