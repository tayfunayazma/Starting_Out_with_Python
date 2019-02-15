# driver's license exam

def main():
    # create a list for answer key
    answers_key = ["A", "C", "A", "A", "D",
                   "B", "C", "A", "C", "B",
                   "A", "D", "C", "A", "D",
                   "C", "B", "B", "D", "A"]
    
    stud_answer = student_answer()
    total = compare_answer(answers_key, stud_answer)
    print()
    
    # determine whether the student has 15 or more correct answers
    if total >= 15:
        print("Congratulations! You passed the exam. You have", total, "correct answers.")
    else:
        print("You failed the exam. You have", total, "correct answers.")
    
def student_answer():
    # open the file
    infile = open("student_anwers.txt", "r")
    
    # read the contents in the file
    student_answer = infile.readlines()
    
    # close the file
    infile.close()
    
    # strip all the \n from the elements
    index = 0
    while index < len(student_answer):
        student_answer[index] = student_answer[index].rstrip("\n")
        index += 1
    
    return student_answer

def compare_answer(answers_key, stud_answer):
    # create an accumulator for counting correct answers
    total = 0
    
    # compare two list
    index = 0
    
    while index < len(answers_key):
        if stud_answer[index] == answers_key[index]:
            total += 1
        else:
            print("The question #", index+1, " is wrong", sep="")
        index += 1
        
    return total
    
# call the main function
main()
            