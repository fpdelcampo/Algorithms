# This should be straight forward.  Evaluate the inner most statements first and move from there
# Each left parenthesis corresponds to 1 operator, a sequence of f/ts, and 1 close paren
# In general, each parse method will receive a statement of the format operator, open parenthesis, content, closed parenthesis

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def parse(expr, start, stop):
            if expr[start] == '!':
                return parse_not(expr, start, stop)
            elif expr[start] == '&':
                return parse_and(expr, start, stop)
            elif expr[start] == '|':
                return parse_or(expr, start, stop)
            else:
                return expr[start] == 't'
        def parse_and(expr, start, stop):
            evaluation = True
            new_expr_start = None
            open_parentheses = 0
            close_parentheses = 0
            for i in range(start + 2, stop):
                if expr[i] == '(':
                    if open_parentheses == 0:
                        new_expr_start = i - 1
                    open_parentheses += 1 
                
                if expr[i] == ')':
                    close_parentheses += 1
                
                if open_parentheses == close_parentheses and open_parentheses > 0:
                    evaluation = evaluation and parse(expr, new_expr_start, i)
                    open_parentheses = 0
                    close_parentheses = 0
                    new_expr_start = None
                
                if expr[i] == 'f' and open_parentheses == 0:
                    return False

            return evaluation

        def parse_or(expr, start, stop):
            evaluation = False
            new_expr_start = None
            open_parentheses = 0
            close_parentheses = 0
            for i in range(start + 2, stop):
                if expr[i] == '(':
                    if open_parentheses == 0:
                        new_expr_start = i - 1
                    open_parentheses += 1 
            
                if expr[i] == ')':
                    close_parentheses += 1
                
                if open_parentheses == close_parentheses and open_parentheses > 0:
                    evaluation = evaluation or parse(expr, new_expr_start, i)
                    open_parentheses = 0
                    close_parentheses = 0
                    new_expr_start = None
                
                if expr[i] == 't' and open_parentheses == 0:
                    return True

            return evaluation

        def parse_not(expr, start, stop):
            if expr[start + 2] in ['f', 't']:
                return expr[start + 2] == 'f'
            return not parse(expr, start + 2, stop - 1)    

        return parse(expression, 0, len(expression) - 1)