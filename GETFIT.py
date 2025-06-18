class GetFit:
    def __init__(self):
        self.Bmi = 0
        self.calories = 0
        self.BMR = 0
        self.final_intake = 0
    def Bmi_Calculation(self, height, weight):
        self.Bmi = weight / (height * height)
        return self.Bmi
    def Female_Calorie_calulator(self,weight,height,age,activity_level):
        BMR = 10 * weight+ 6.25 * height - 5 * age - 161
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
        BMR = 10 * weight + 6.25 * height - 5 * age + 5
        activity_multipliers = {
            "sedentary": 1.2,
            "lightly_active": 1.375,
            "moderately_active": 1.55,
            "very_active": 1.725,
            "super_active": 1.9
        }
        multiplier = activity_multipliers.get(activity_level, 1.2)  # default to sedentary
        self.final_intake = int(BMR* multiplier)
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


