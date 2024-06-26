from pyscript import display, document
from pyweb import pydom

# class BMI():
#     def __init__(self, weight: int = None, height_feet: int = None, remaining_height_inches: int = None):
#         self.weight = weight
#         self.height_feet = height_feet
#         self.remaining_height_inches = remaining_height_inches


height_feet = pydom["#height_feet"][0]
height_inches = pydom["#height_inches"][0]
weight = pydom["#weight"][0]

# print(height_inches.value)
def bmi_calculate() -> float:
    feet_inch = int(height_feet.value) * 12
    weight_kg = int(weight.value) * 0.45 #weight from lbs to kg
    height_m = ((int(height_inches.value) + feet_inch) * 0.025)**2 #height from ft/in to meters
    final_bmi = round(weight_kg / height_m, 1) #get bmi


    # display(f'{final_bmi}': {bmi_category})
    return final_bmi

    


def bmi_category( bmi: float = None) -> str:
    #can pass in an optional specific bmi
    #argument will override the default calculated bmi
    category = ['Underweight','Normal Weight', 'Overweight', 'Obese' ]
    if bmi != None:
        bmi = bmi
    else:
        bmi = bmi_calculate()
    try:
        if bmi < 18.5:
            return category[0]
        elif bmi >= 18.5 and bmi <= 24.9:
            return category[1]
        elif bmi >= 25 and bmi <= 29.9:
            return category[2]
        elif bmi >= 30:
            return category[3]
    except TypeError:
        return "ERROR: Unable to receive bmi category. Please use numbers only."

def display_bmi_info(e) -> str:
    if height_feet.value == '' or height_inches.value == '' or weight.value == '':
        return None
    bmi = bmi_calculate()
    category = bmi_category(bmi)
    display(f'BMI: {bmi} Category: {category}')
                


# def main() -> None:
    
#     print("BMI Calculator")
#     print("Do not add units to input.\nEx: If you are 5\'10\", enter 5 for height in feet and 10 for remaining height in inches input.\n")
#     try:
#         weight = int(input("Enter your weight: "))
#         height = int(input("Enter your height in feet (feet without inches as described above): "))
#         height_inch = int(input("Enter your remaining height in inches: "))
#         bmi = BMI(weight, height, height_inch).display_bmi_info()
        
#         print(bmi)
#     except ValueError:
#         print("ERROR: Please use numbers only")

    


# if __name__ == '__main__':
#     main()