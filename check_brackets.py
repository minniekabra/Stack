# python3
'''
This code implements an editor functionality using data structure Hash: Check brackets in the code 
'''

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

class Stack:
    def __init__(self, stack):
        self.stack = stack

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            return 0

        else:
            x = self.stack.pop()
            return x


if __name__ == "__main__":
    text = sys.stdin.read()


    opening_brackets_stack = []
    opening_brackets_pos = []
    close_error = 0

    for i, next in enumerate(text):

        if next == '(' or next == '[' or next == '{':
            stack1 = Stack(opening_brackets_stack)
            stack1.push(next)

            stack2 = Stack(opening_brackets_pos)
            stack2.push(i+1)


        if next == ')' or next == ']' or next == '}':
            stack1 = Stack(opening_brackets_stack)
            open_bracket = stack1.pop()

            stack2 = Stack(opening_brackets_pos)
            open_pos = stack2.pop()


            if open_bracket == 0:
                close_error = 1
                break

            else:
                check_close_brckt = Bracket(open_bracket, i+1)
                bracket_correct = check_close_brckt.Match(next)

                if bracket_correct == True:
                    pass
                else:
                    close_error = 1
                    break
            # Process closing bracket, write your code here


    if close_error == 1:
        print(i+1)

    elif len(opening_brackets_pos) > 0:
        print(opening_brackets_pos[0])

    else:
        print('Success')
