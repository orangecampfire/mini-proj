class Excel():

    def __init__(self):
        self.quiz_weight = 0.20
        self.attendance_weight = 0.10
        self.recitation_weight = 0.10
        self.tests_weight = 0.60
        self.quiz_list = [1]
        self.attendance_list = [1]
        self.recitation_list = [1]
        self.tests_list = [1]

    def quiz_avg_function(self):
        sum_quiz = sum(self.quiz_list)
        length_of_quiz = len(self.quiz_list)
        return (sum_quiz / length_of_quiz) * self.quiz_weight

    def attend_avg_function(self):
        sum_attend = sum(self.attendance_list)
        length_of_attend = len(self.attendance_list)
        return (sum_attend / length_of_attend) * self.attendance_weight

    def recitation_avg_function(self):
        sum_recitation = sum(self.recitation_list)
        length_of_recitation = len(self.recitation_list)
        return (sum_recitation / length_of_recitation) * self.recitation_weight

    def test_avg_function(self):
        sum_tests = sum(self.tests_list)
        length_of_tests = len(self.tests_list)
        return (sum_tests / length_of_tests) * self.tests_weight

    def compute_total_grade(self):
        total = self.quiz_avg_function() + self.attend_avg_function() + self.recitation_avg_function() + self.test_avg_function()
        return total


inputs = Excel()
total_grade = inputs.compute_total_grade()