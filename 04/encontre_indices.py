def encontre_indices(lista, item):
    indices = []
    for i, element in enumerate(lista):
        if element == item:
            indices.append([i])
        elif isinstance(element, list):
            sub_indices = encontre_indices(element, item)
            for sub_index in sub_indices:
                indices.append([i] + sub_index)
    return indices
