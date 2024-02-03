class Excel:    

    def __init__(self):

        self.quiz = float(.20)
        self.attendance = float(.10)
        self.recitation = float(.10)    
        self.tests = float(.60)
        self.quiz_list = []
        self.attendance_list = []
        self.recitation_list = []
        self.tests_list = []
        self.inputs = self.get_inputs()


    #def create_lists_for_each_avg(self):
     #   self.quiz_list = []
     #   self.attendance_list = []
     #   self.recitation_list = []
     #   self.tests_list = []


    #arguments to calculate the average with weights for each category

    def quiz_avg_function(self):
        self.sum_quiz = sum(self.quiz_list)
        self.length_of_quiz = len(self.quiz_list)
        self.quiz_avg = (self.sum_quiz / self.length_of_quiz) * self.quiz
       
        

    def attend_avg_function(self):
        self.sum_attend = sum(self.attendance_list)
        self.length_of_attend = len(self.attendance_list)
        self.attend_avg = (self.sum_attend / self.length_of_attend) * self.attendance
        

        
    def recitation_avg_function(self):
        self.sum_recitation = sum(self.recitation_list)
        self.length_of_recitation = len(self.recitation_list)
        self.recitation_avg = (self.sum_recitation / self.length_of_recitation) * self.recitation
        


    def test_avg_function(self):
        self.sum_tests = sum(self.tests_list)
        self.length_of_tests = len(self.tests_list)
        self.tests_avg = (self.sum_tests / self.length_of_tests) * self.tests
       

    #the previous arguments calculated the average with the weights, this one adds them together to get the final grade
    def compute_total_grade(self):
        self.total = self.quiz_avg_function() + self.attend_avg_function() + self.recitation_avg_function() + self.test_avg_function()
        print(self.total)



    def get_inputs(self):
        self.quiz_input = float(input('Enter grade of a single quiz:\n'))
        self.test_input = float(input('Enter a grade for a single test:\n'))
        self.recitation_input = float(input('Enter the grade for recitations:\n'))
        self.attendance_input = float(input('Enter the grade for attendance:\n'))

        self.quiz_list.append(self.quiz_input)
        self.tests_list.append(self.test_input)
        self.recitation_list.append(self.recitation_input)
        self.attendance_list.append(self.attendance_input)

        




inputs = Excel()
inputs.get_inputs()
inputs.compute_total_grade()
#inputs.quiz_avg_function()

        