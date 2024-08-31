def get_test_score(answer_sheet, student_answers):
    counter = 0
    name = student_answers[0]

    for i in range(0, len(answer_sheet)):
        if student_answers[i+1] == answer_sheet[i]:
            counter += 1
            
    result = (counter/len(answer_sheet))*100
    return name, result
