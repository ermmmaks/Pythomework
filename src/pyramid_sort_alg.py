def build_subroot(arr, ln, i_root):
    main_root = i_root

    left_root = 2 * i_root + 1
    right_root = 2 * i_root + 2

    if left_root < ln and arr[left_root] > arr[main_root]:
        main_root = left_root

    if right_root < ln and arr[right_root] > arr[main_root]:
        main_root = right_root

    if main_root != i_root:
        arr[i_root], arr[main_root] = arr[main_root], arr[i_root]
        build_subroot(arr, ln, main_root)


def build_pyramid(arr):
    ln = len(arr)

    for i in range(ln // 2 - 1, -1, -1):  # index main_root
        build_subroot(arr, ln, i)

    for d in range(ln - 1, 0, -1):  # decline lenght
        arr[d], arr[0] = arr[0], arr[d]
        build_subroot(arr, d, 0)

    return arr
