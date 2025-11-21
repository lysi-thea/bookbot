def get_num_words(story):
    words = story.split()
    return len(words)

def get_num_chars(story):
    story = story.lower()
    char_stats = {}

    for i in story:
        if i in char_stats:
            char_stats[i] += 1

        else:
            char_stats[i] = 1
    
    return char_stats

def sort_on(d):
    return d["num"]

def get_sorted_list(dictionary): # [ { "char": <char>, "num": <int> } ] 
    sorted_list = []

    for i in dictionary:
        entry = {
            "char": i,
            "num": dictionary[i]
        }
        sorted_list.append(entry)
    

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list