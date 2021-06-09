from datas import list_of_attitudes

def make_att_from_quest(selected_questions):
    # you can also use it to check all the attitudes which contains a word!

    global list_of_attitudes

    if type(selected_questions) == type('abc'):
        selected_questions = [selected_questions]

    selected_attitudes = list()
    for att in list_of_attitudes:
        for quest in selected_questions:
            if quest in att:
                selected_attitudes.append(att)
                break

    return selected_attitudes