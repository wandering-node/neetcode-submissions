class Solution:
    from typing import List
    def encode(self, strs: List[str]) -> str:
        ans_str = ""
        for temp_str in strs:
            # Format: <length>#<string>
            ans_str += f"{len(temp_str)}#{temp_str}"
        return ans_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            # Find where the length integer ends
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Extract the exact string based on the parsed length
            start = j + 1
            end = start + length
            ans.append(s[start:end])
            
            # Move index past the current string to the next length integer
            i = end
            
        return ans