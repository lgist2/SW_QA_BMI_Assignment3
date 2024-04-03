from bmi import BMI
import pytest


#Tests form bmi_calculate()
@pytest.mark.parametrize(
        "weight, height, height_inch, output",
        [
            (125, 5, 3, 22.7), #TC Calculate 01.1
            (125, "a", 3, "ERROR: Please use numbers only."), #TC Calculate 01.2
            (125.4, 5.2, 3, 21.1) #TC Calculate 01.3
        ]
)
def test_bmi_calculate(weight, height, height_inch, output):
    bmi = BMI(weight, height, height_inch)
    bmi_calc = bmi.bmi_calculate()
    assert bmi_calc == output



@pytest.mark.parametrize(
        "bmi, category",
        [
            (18.4, "Underweight"), #TC Category 01.1
            (18.5, "Normal Weight"), #TC Category 01.2
            (24.9, "Normal Weight"), #TC Category 01.3
            (25, "Overweight"), #TC Category 01.4
            (29.9, "Overweight"), #TC Category 01.5
            (30, "Obese"), #TC Category 01.6
            (30.1, "Obese") #TC Category 01.7
        ]
)
def test_bmi_category(bmi, category):
    bmi_category = BMI().bmi_category(bmi) 
    assert bmi_category == category


@pytest.mark.parametrize(
        "bmi, output",
        [
            (17.9, "BMI: 17.9 Category: Underweight"), #TC Display 01.1
            (22.5, "BMI: 22.5 Category: Normal Weight"),#TC Display 01.2
            (27.6, "BMI: 27.6 Category: Overweight"),#TC Display 01.3
            (32.7, "BMI: 32.7 Category: Obese")#TC Display 01.4
        ]
)
def test_display_bmi_info(bmi, output):
    bmi_display = BMI().display_bmi_info(bmi)
    assert bmi_display == output


