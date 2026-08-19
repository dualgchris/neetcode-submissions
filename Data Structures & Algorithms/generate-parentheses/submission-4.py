class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # result = []

        # def isValid(s):
        #     balance = 0

        #     for char in s:
        #         if char == "(":
        #             balance += 1
        #         else:
        #             balance -= 1
        #         if balance < 0:
        #             return False

        #     return balance == 0
        
        # def build(current):

        #     if len(current) == 2 * n:
        #         if isValid(current):
        #             result.append(current)
        #         return
            
        #     build(current + "(")
        #     build(current + ")")
        
        # build("")
        # return result




        result = []

        def backtrack(current, opened, closed):

            if len(current) == 2 * n:
                result.append(current)
                return

            if opened < n:
                backtrack(
                    current + "(",
                    opened + 1,
                    closed

                )

            if closed < opened:
                backtrack(
                    current + ")",
                    opened,
                    closed + 1
                )
        backtrack("", 0, 0)

        return result

