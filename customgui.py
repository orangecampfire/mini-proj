import customtkinter as ctk
import math_code

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue") 

appWidth, appHeight = 600, 500

class App(ctk.CTk, math_code.Excel):
	# The layout of the window will be written
	# in the init function itself
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Sets the title of the window to "App"
		self.title("Grade Calculator") 
		# Sets the dimensions of the window to 600x700
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
          

		  
	def generateResults(self):
		self.displayBox.delete("0.0", "200.0")

        
		quiz_value = self.quizEntry.get()
		test_value = self.testEntry.get()
		attendance_value = self.attendanceEntry.get()
		recitation_value = self.recitationEntry.get()

		self.quiz_list.append(float(quiz_value))
		self.tests_list.append(float(test_value))
		self.attendance_list.append(float(attendance_value))
		self.recitation_list.append(float(recitation_value))	
		text = f"Quiz: {self.quiz_list}\nTest: {self.test_list}\nAttendance: {self.attendance_list}\nRecitation: {self.recitation_list}"
		self.displayBox.insert("0.0", text)






if __name__ == "__main__":
	app = App()
	# Used to run the application
	app.mainloop()	 

print(math_code.total_grade)

