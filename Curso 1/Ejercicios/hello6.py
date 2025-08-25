
#EJERCICO 1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """

    return len(zip_code) == 5 and zip_code.isdigit()
    
print(is_valid_zip("12345"))


#EJERCICIO 2
def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


#EJERCICIO 3

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

