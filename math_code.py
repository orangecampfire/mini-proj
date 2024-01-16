import tkinter as tk


class Excel:    

    def __init__(self, root):
        self.root = root
        self.root.title("Totally an Excel Sheet")
    
        self.grid_width = 50
        self.grid_height = 50

        self.quiz = float(.20)
        self.attendance = float(.10)
        self.recitation = float(.10)
        self.tests = float(.60)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, width=self.grid_width, height=self.grid_height)
        self.canvas.pack()


    def create_lists_for_each_avg(self):
        self.quiz_list = [90, 87, 100, 76]
        self.attendance_list = []
        self.recitation_list = []
        self.tests_list = []

    def quiz_avg_function(self):
        sum_quiz = sum(self.quiz_list)
        print(sum_quiz)




if __name__ == "__main__":
    root = tk.Tk()
    excel = Excel(root)
    root.mainloop()
    instance = Excel()
    Excel.quiz_avg_function(root)