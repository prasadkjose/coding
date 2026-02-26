""" Solution Module """


class Solution:
    """ Solution Class """

    def run_solution(self, test_input):
        """ Solution Method """
        # Take an input encode it and then decode it.

        def encode(to_encode: list[str]) -> str:
            len_arr = [str(len(mess))+'##' for mess in to_encode]
            prefix = ''.join(len_arr)
            stringified_message = "".join(to_encode)
            encoded = prefix+stringified_message
            return encoded

        def decode(encoded: str) -> list[str]:
            split_arr = encoded.split("##")
            encoded_message = split_arr[-1]
            len_arr = split_arr[0:len(split_arr) -1]
            print(len_arr, encoded_message)
            decoded = []
            prev_l = 0
            for l in len_arr:
                decoded.append(encoded_message[prev_l:prev_l+int(l)])
                prev_l += int(l)
            return decoded

        encoded = encode(test_input)
        decoded = decode(encoded)
        return test_input == decoded
