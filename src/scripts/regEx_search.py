import re

#regEx search function
def regEx_search(write_to_file,input):
    input = unity_class_to_godot_class(input)
    input = debug_log_to_GD_Print(input)
    input = change_public_variables(input)
    input = get_axis_to_godot(input)
    return input

#debug.log to GD.Print conversion function
def debug_log_to_GD_Print(input):
    new_code = re.sub(r'Debug\.Log\((.*)\)', r'GD.Print(\1)', input)
    return new_code

#change the class to a godot class
def unity_class_to_godot_class(input):
    new_code = re.sub(r'public class (\w+) : MonoBehaviour', r'public partial class \1 : Node', input)
    return new_code

#change the public variables to the godot format
def change_public_variables(input):
    new_code = re.sub(r"(public)\s+(string|float|int|double)\s+(\w+)", r"[Export]\n\t\1 \2 \3",input)
    return new_code

def get_axis_to_godot(code):

    # Regex patterns
    pattern = r"float\s+(?P<horizontal>\w+)\s+=\s+Input\.GetAxis\(\"Horizontal\"\);"
    pattern1 = r"float\s+(?P<vertical>\w+)\s+=\s+Input\.GetAxis\(\"Vertical\"\);"

    # Replacement pattern
    replacement = r'Vector2 inputDir = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");'

    #this is jank but it is 2:30 am and I am tired
    new_code = code
    if pattern != replacement and pattern != replacement:
        new_code = re.sub(pattern, " ", code)
        new_code = re.sub(pattern1, replacement, new_code)
        
    #a for loop that goes through the new_code to check if the replacement is in the new_code abd if it is there more then once all extra instances are removed
    for match in re.finditer(pattern, new_code):
        if match.group(0) == replacement:
            pass
        else:
            new_code = new_code.replace(match.group(0), "")

    if pattern == replacement and pattern1 == replacement:
        pattern1 = ""

    return new_code
