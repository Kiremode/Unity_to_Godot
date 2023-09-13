import re

#regEx search function
def regEx_search(write_to_file,input):
    input = unity_class_to_godot_class(input)
    input = debug_log_to_GD_Print(input)
    input = change_public_variables(input)
    
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

def get_axis_to_godot(input):

       # Regex pattern
    pattern = r"float (?P<horizontal>\w+) = Input\.GetAxis\(\"Horizontal\"\);\s+float (?P<vertical>\w+) = Input\.GetAxis\(\"Vertical\"\);\s+Vector3 (?P<movement>\w+) = new Vector3\(\k<horizontal>, 0.0f, \k<vertical>\);"

    # Replacement pattern
    replacement = r'Vector2 inputDir = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");\n\tVector3 direction = (Transform.Basis * new Vector3(inputDir.X, 0, inputDir.Y)).Normalized();'

    # Substitute
    new_code = re.sub(pattern, replacement, input)

    print(new_code)
    return new_code