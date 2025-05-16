import re
import argparse

def pattern_finder(pat,string):
    return re.search(pat,string)

def four_car_finder(string):
    return re.findall(r"\b\w{4}\b",string)

def speed_inkms_finder(string):
    match = re.search(r"(\d+\.\d+|\d+)\s*km",string)
    if match:
        return float(match.group(1))
def redo_speed(string):
    match= re.findall(r"(\d+\.\d+|\d+)\s*km",string)
    return [float(i) for i in match]

    
parser=argparse.ArgumentParser()
parser.add_argument("--THEME")
args= parser.parse_args()

def set_theme(theme="default"):
    valid_themes = ["default", "light", "dark", "blue"]
    if theme not in valid_themes:
        raise ValueError(f"Invalid theme: {theme}")
    print(f"Theme set to {theme}")


def theme_catcher(THEME):
    try:
        set_theme(THEME)
    except ValueError as e:
        print(e)
        print("Falling back to default theme.")
        set_theme()

def process_numbers(data):
    list_floats=[]
    for item in data:
        try:
            num=float(item)
            list_floats.append(num)
        except (ValueError , TypeError):
            print("what you have cannot be converted")
    return list_floats

    
print("hello world")