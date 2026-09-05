class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        d={'(':')','{':'}','[':']'}

        for i in s:
            if i not in d.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                character=stack.pop()
                if d.get(character)!=i:
                    return False
        if stack:
            return False
        else:
            return True
