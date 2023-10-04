"""
Check hints out.
find the number of moves a player can play.
check winner
Greedy
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        def find_consecutive_char(match):
            total_moves = 0
            i = 0
            count = 0
            while i < len(colors):
                if colors[i] != match:
                    if count > 2:
                        total_moves += (count - 2)
                    count = 0
                else:
                    count += 1
                i += 1
            if count > 2:
                total_moves += (count - 2)
            return total_moves

        alice_moves = find_consecutive_char('A')
        bob_moves = find_consecutive_char('B')
        return alice_moves > bob_moves



print(Solution().winnerOfGame("AAAABBBB"))
print(Solution().winnerOfGame("AAABABB"))
print(Solution().winnerOfGame("AAAAABBB"))