""" Solution Module """
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """
        # // Input: strs = ["act","pots","tops","cat","stop","hat"]
        # // Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        anagram_dict: dict[str, list[str]] = dict()

        for i in test_input:
            sorted_list = "".join(sorted(i))
            if sorted_list in anagram_dict:
                anagram_dict[sorted_list].append(i)
            else :
                anagram_dict[sorted_list] = [i]
        return anagram_dict
