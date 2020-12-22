# Problem: given a dictionary, i.e., a set of strings, and a name, design an efficient algorithm that checks
#          whether the name is the concatenation of a sequence of dictionary words. If such a concatenation exists,
#          return it. A dictionary word may appear more than once in the sequence. For example, "a", "man", "plan", "a",
#          "canal" is a valid sequence for "amanaplanacanal".

# EPI Judge: is_string_decomposable_into_words.py
def decompose_into_dictionary_words(domain, dictionary):

    visited_prefixes = set()

    def build_domain_from_dict(start):
        if start == len(domain):
            return True
        if start not in visited_prefixes:
            for end in range(start + 1, len(domain) + 1):
                prefix = domain[start:end]
                if prefix in dictionary:
                    sequence.append(prefix)
                    if build_domain_from_dict(end):
                        return True
                    del sequence[-1]
            visited_prefixes.add(start)
        return False

    sequence = []
    build_domain_from_dict(0)
    return sequence


if __name__ == "__main__":
    domain = "ikkmkappkgxakkivgobqafsoiqkppoifxkipsfqmsmffofpiacsviabqsvsvoisfvccaxrogoriirsmfirxpgrpmfxxpgvbofic"
    dictionary = {'ksvbpkss', 'bssivxgvgorqgoc', 'oifxkips', 'ffmqbpik', 'gpmgiqvfiqiva', 'oriirsmfirxp', 'mm', 'marommx', 'vxrsbgxgm', 'gfbicocgfrm', 'kvraogxbcf', 'mrac', 'iqkpp', 'vgobqafso', 'cxp', 'voopfvpmfppgcav', 'p', 'kafskrgqqspxv', 'if', 'bb', 'skpscabgkcgokc', 'ikkmkappkgxakki', 'a', 'grpmfxxpgvb', 'aavbpxmvipbqp', 'sfvccaxro', 'coo', 'xivoricbbiax', 'cm', 'mfcikaqmorgbibv', 'ofic', 'mqqgaxiokqmc', 'xggikvvfvmr', 'csviabqsvsvoi', 'koqfvgpcxfibf', 'fqmsmffofpia', 'amvkkomqcp', 'kifqigm', 'ckfi', 'agfpgqmcisqxqxs', 'g', 'qbasporivms', 'sakiqoxoa', 'ab', 'pp', 'gxigsgpxoiqb', 'qoogkc', 'pxvrkk', 'xioxmax', 'gxmisxioog'}
    print(decompose_into_dictionary_words(domain, dictionary))     