def longestCommonPrefix(strs) -> str:
    sorted_list = sorted(strs, key=lambda s: len(s))

    # iterate_list = sorted_list[1:]
    # print(iterate_list)

    pref = sorted_list[0]

    for word in strs:
        print(f"Word: {word}")
        while not word.startswith(pref):
            pref = pref[:-1]

    print(f"Prefix: {pref}")
    return pref


longestCommonPrefix(["flower", "flow", "flight", "floersgf"])
# longestCommonPrefix(["flower","flow","flight", "loersgf"])
