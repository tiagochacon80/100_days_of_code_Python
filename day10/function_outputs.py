#Functions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title() #returne la premiere lettre du nom en majuscule
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("TiAgO", "CHACON"))


