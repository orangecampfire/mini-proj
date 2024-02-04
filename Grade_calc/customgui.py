import customtkinter as ctk
import math_code

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue") 

appWidth, appHeight = 600, 500

class App(ctk.CTk):
	# The layout of the window will be written
	# in the init function itself
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.excel_instance = math_code.Excel()

		self.excel_instance.quiz_list.clear()
		self.excel_instance.tests_list.clear()
		self.excel_instance.attendance_list.clear()
		self.excel_instance.recitation_list.clear()


		self.title("Grade Calculator") 
		self.geometry(f"{appWidth}x{appHeight}") 

		# Quiz Label
		self.quizLabel = ctk.CTkLabel(self,
								text="Quizzes")
		self.quizLabel.grid(row=0, column=0,
							padx=20, pady=20,
							sticky="ew")

		# Quiz Entry Field
		self.quizEntry = ctk.CTkEntry(self,
						placeholder_text="Enter quiz grades")
		self.quizEntry.grid(row = 0, column = 1,
							columnspan = 3, padx = 20,
							pady = 20, sticky = "ew")

		# Test Label
		self.testLabel = ctk.CTkLabel(self, text="Tests")
		self.testLabel.grid(row = 1, column = 0,
						padx = 20, pady = 20,
						sticky="ew")

		# Test Entry Field
		self.testEntry = ctk.CTkEntry(self,
							placeholder_text = "Enter test grades",
							width = 350)
		self.testEntry.grid(row = 1, column = 1,
						columnspan = 3, padx = 20,
						pady = 20, sticky = "ew")
		
		#attendance label
		self.attendanceLabel = ctk.CTkLabel(self, text="Attendance")
		self.attendanceLabel.grid(row = 2, column = 0,
						padx = 20, pady = 20,
						sticky = "ew")

		self.attendanceEntry = ctk.CTkEntry(self,
							placeholder_text="Enter attendance grades")
		self.attendanceEntry.grid(row = 2, column = 1,
						columnspan = 3, padx = 20,
						pady = 20, sticky = "ew")
		
		self.recitationLabel = ctk.CTkLabel(self, text="Recitation")
		self.recitationLabel.grid(row = 3, column = 0,
						padx = 20, pady = 20,
						sticky="ew")

		self.recitationEntry = ctk.CTkEntry(self,
							placeholder_text="Enter recitation grades")
		self.recitationEntry.grid(row = 3, column = 1,
						columnspan = 3, padx = 20,
						pady = 20, sticky = "ew")


		

		self.generateResultsButton = ctk.CTkButton(self,
										text="Generate Results",
										width = 350,
										command=self.generateResults)
		self.generateResultsButton.grid(row=5, column=1,
										columnspan=2, padx=20, 
										pady=20, sticky="ew")


		self.displayBox = ctk.CTkTextbox(self,
										width=350,
										height=100)
		self.displayBox.grid(row=6, column=1,
							columnspan=4, padx=20,
							pady=20, sticky="nsew")
          

	#put the total grade into the text box when clicked
	def generateResults(self):
		self.displayBox.delete("0.0", "200.0")

        
		quiz_value = self.quizEntry.get()
		test_value = self.testEntry.get()
		attendance_value = self.attendanceEntry.get()
		recitation_value = self.recitationEntry.get()

		self.excel_instance.quiz_list.append(float(quiz_value))
		self.excel_instance.tests_list.append(float(test_value))
		self.excel_instance.attendance_list.append(float(attendance_value))
		self.excel_instance.recitation_list.append(float(recitation_value))

		
		total_grade = self.excel_instance.compute_total_grade()
		text = (f"Quiz: {self.excel_instance.quiz_list}\nTest: {self.excel_instance.tests_list}\nAttendance: {self.excel_instance.attendance_list}\nRecitation: {self.excel_instance.recitation_list}\nTotal grade:{total_grade:.2f}")
		self.displayBox.insert("0.0", text)


		self.read_data()
		self.store_data()
	



	def store_data(self, filename = "grades.txt"):
		with open(filename, 'a') as file:
			file.write(f'{self.excel_instance.quiz_list}\n')
			file.write(f'{self.excel_instance.tests_list}\n')
			file.write(f'{self.excel_instance.attendance_list}\n')
			file.write(f'{self.excel_instance.recitation_list}\n')


	def read_data(self, filename = "grades.txt"):
		try:
			with open(filename, 'r') as file:
				lines = file.readlines()

				lines_str = ','.join(map(str, lines))
				data_lists = [eval(part) for part in str(lines.split(','))]

				self.excel_instance.quiz_list = data_lists[0]
				self.excel_instance.tests_list = data_lists[1]
				self.excel_instance.attendance_list = data_lists[2]
				self.excel_instance.recitation_list = data_lists[3]

				self.generateResults()

		except FileNotFoundError:
			print("File not found. Creating new lists.")


if __name__ == "__main__":
	app = App()

	app.mainloop()