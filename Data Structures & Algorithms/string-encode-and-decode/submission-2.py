class Solution:

    def encode(self, strs: List[str]) -> str:
        ans_str = ''
        if strs:
            for temp_str in strs:
                ans_str += f"{len(temp_str)}#{temp_str}"
        return ans_str
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
             return []
        else:
            ans = []
            curr_len = ''
            curr_idx = 0
            while curr_idx < len(s):
                for i in s[curr_idx:]:
                    if i != '#':
                        curr_len += i
                    else:
                        break
                curr_idx += len(curr_len) + 1
                ans.append(s[curr_idx:curr_idx + int(curr_len)])
                curr_idx += int(curr_len)
                curr_len = ''
            return ans



