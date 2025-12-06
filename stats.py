def get_word_count(book_data):
    word_list = book_data.split()
    return len(word_list)

def get_unique_string_count(book_data):
    string_count_dict = {}

    for string in book_data.lower():
        if string not in string_count_dict:
            string_count_dict[string] = 1
        else:
            string_count_dict[string] += 1
    
    return string_count_dict

# This func will receive the dict_list list and then based on the count we return determine how it will sort those keys
def sort_criteria(item):
    return item["count"]


def get_dict_list(string_count_dict):
    dict_list = []
    for key in string_count_dict:
        if key.isalpha():
            dict_list.append({
                "string": key,
                "count": string_count_dict[key]
            })

    # this will sort in desc and sorting order will be decided based on sort_criteria func
    dict_list.sort(reverse=True,key=sort_criteria)
    
    return dict_list

def print_dict(string_dict_list):
    for dict_list in string_dict_list:
        key = dict_list["string"]
        value = dict_list["count"]
        print(f"{key}: {value}")
    
    return None