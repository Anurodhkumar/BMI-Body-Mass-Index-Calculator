alldata = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]
allcolumn=[]

def bmiCategory(bmi):
    if 18.4<=bmi<24.9:
        category= 'Underweight'
        risk = 'Malnutrition risk'
    elif 25<bmi<=29.9:
        category = 'Normal weight'
        risk = 'Low risk'
    elif 30<bmi<=34.9:
        category = 'Overweight'
        risk = 'Enhanced risk'        
    elif 35<bmi<=39.9:
        category = 'Moderately obese'
        risk = 'Medium risk'
    elif bmi == 40:
        category = 'Severely obese'
        risk = 'High risk'
    else:    
        category = 'Very severely obese'
        risk = 'Very high risk'
    return category,risk    

for each in alldata:
    column=[]
    Bmi = each["WeightKg"]/(each["HeightCm"]/100)
    health_category,health_risk = bmiCategory(Bmi)
    column.append(Bmi)
    column.append(health_category)
    column.append(health_risk)
    allcolumn.append(column)

count=0
for column in allcolumn:
    if column[1] == 'Overweight':
        count += 1

print(count)
        
    
