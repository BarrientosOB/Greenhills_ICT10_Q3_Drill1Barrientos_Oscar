from pyscript import document,display


subjects = ['English', 'Math', 'Science', 'Filipino']

Units = (2, 2, 3, 3)

def getting_info(e):
    document.getElementById('div1').innerHTML = ""
    first_name = document.getElementById('input1').value
    last_name = document.getElementById('input2').value
    num1 = float(document.getElementById('eng').value)
    num2 = float(document.getElementById('mth').value)
    num3 = float(document.getElementById('sci').value)
    num4 = float(document.getElementById('fil').value)

    scores = (num1, num2, num3, num4)
    total_units = sum(Units)
    total_score = sum(scores)
    average = total_score / len(subjects)
    display(f'Student Name: {first_name} {last_name}', target="div1")
    display(f'Total Units: {total_units}', target="div1")
    display(f'Average Score: {average}', target="div1")

    if average > 74:
        display(f'Status: Passed', target="div1")
    else:
        display(f'Status: Failed', target="div1")