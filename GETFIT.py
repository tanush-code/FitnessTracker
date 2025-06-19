class GetFit:
    def __init__(self):
        self.Bmi = 0
        self.calories = 0
        self.BMR = 0
        self.final_intake = 0
    def Bmi_Calculation(self, height, weight):
        self.Bmi = weight / (height/100 * height/100)
        return self.Bmi
    def Female_Calorie_calulator(self,weight,height,age,activity_level):
        BMR =  655.1 + (9.563 * weight) + (1.850 *height) - (4.676 * age) 
        activity_multipliers = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725,
        "super_active": 1.9
        }
        multiplier = activity_multipliers.get(activity_level, 1.2)  # default to sedentary
        self.final_intake = int(BMR * multiplier)
        return self.final_intake

    def Male_Calorie_calulator(self, weight, height, age, activity_level):
        BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 *age)
        activity_multipliers = {
            "sedentary": 1.2,
            "lightly_active": 1.375,
            "moderately_active": 1.55,
            "very_active": 1.725,
            "super_active": 1.9
        }
        multiplier = activity_multipliers.get(activity_level, 1.2)  # default to sedentary
        self.final_intake = float(BMR* multiplier)
        return self.final_intake
    def Fixed_Aim(self):
        if self.Bmi > 30:   
            return f"""
            You are Seriously overweighted person ,You should start exercising and eat less \n
            For Rapid Weight Loss Calorie intake: , {self.final_intake - 700}
            For Moderate Weight Loss Calorie intake: , {self.final_intake - 400}
            For Slow Weight Loss Calorie intake: , {self.final_intake - 250}
            """
        if self.Bmi < 16:
            return f"""
            You are Seriously Underweight person ,You should start exercising and eat less \n
            For Rapid Weight Gain Calorie intake: , {self.final_intake + 700}
            For Moderate Weight Gain Calorie intake: , {self.final_intake + 400}
            For Slow Weight Gain Calorie intake: , {self.final_intake + 250}
            """


