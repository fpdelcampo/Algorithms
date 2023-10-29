class Solution:
    # Rules
    # An integer is sequence of digits optionally preceded by a +/-
    # A decimal is one of the following, optionally preceded by +/-
    # 1. a sequence of digits, followed by a '.'
    # 2. a '.' followed by a sequence of digits
    # 3. a sequence of digits followed by a '.' followed by a sequence of digits
    # Valid numbers are either decimals/integers, or decimals/integers + 'e'/'E' + an integer
    def isNumber(self, s: str) -> bool:
        return self.isInteger(s) or self.isDecimal(s) or self.other(s)

    def digitSequence(self, s):
        for char in s:
            if not char.isnumeric():
                return False
        return True
    
    def isInteger(self, s):
        if not s:
            return False
        if s[0] in ['-', '+']:
            if len(s) > 1:
                return self.digitSequence(s[1:])
            else:
                return False
        else:
            return self.digitSequence(s)
    
    def isDecimal(self, s):
        if not s:
            return False
        if s[0] in ['-', '+']:
            if len(s) > 1:
                return self.isDecimal(s[1:])
            else:
                return False
        components = []
        curr = ""
        for char in s:
            if char == '.':
                if curr != "":
                    components.append(curr)
                    curr = ""
                components.append(char)
            else:
                curr += char
        if curr != "":
            components.append(curr)
        if len(components) > 3:
            return False
        else:
            if len(components) == 2:
                first = (components[0] == '.' and self.digitSequence(components[1]))
                second = (components[1] == '.' and self.digitSequence(components[0]))
                return first or second
            elif len(components) == 3:
                return self.digitSequence(components[0]) and components[1] == '.' and self.digitSequence(components[2])
        return False
        
    def other(self, s):
        components = s.split('e')
        if len(components) == 1:
            components = s.split('E')
        if len(components) != 2:
            return False
        return (self.isDecimal(components[0]) or self.isInteger(components[0])) and self.isInteger(components[1])