import re
import ft_utils

def parse_value(liste):
    num = []
    x1 = []
    x2 = []
    x_other = []
    x1_empty = []
    x_zero = []
    final_list = []
    pattern = r"([^\^][0-9]+[\.]?[0-9]*)"
    pattern1 = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^1(?![0-9]))"
    pattern2 = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^2(?![0-9]))"
    pattern_zero = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^0(?![0-9]))"
    pattern_other = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[^0-2]|[\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[1-2][0-9])"
    pattern1_empty = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X[^\^])"
    pattern_expo = r"([0-9]*$)"
    
    liste += " "
    num = re.findall(pattern,liste)
    x1 = re.findall(pattern1,liste)
    x_zero = re.findall(pattern_zero,liste)
    x1_empty = re.findall(pattern1_empty,liste)
    x2 = re.findall(pattern2,liste)
    x_other = re.findall(pattern_other,liste)

    x1 = ft_utils.remove_x(x1, num)
    x2 = ft_utils.remove_x(x2, num)
    x1_empty = ft_utils.remove_x(x1_empty, num)
    x_zero = ft_utils.remove_x(x_zero, num)
    x_1 = x1 + x1_empty
    num = ft_utils.remove_x_in_num(num)
    num = ft_utils.clean_num(num)
    ft_utils.remove_value_from_list(num, x_zero)
    ft_utils.remove_value_from_list(num, x_1)
    ft_utils.remove_value_from_list(num, x2)
    test = ft_utils.remove_x(x_other, num)
    ft_utils.remove_value_from_list(num, ft_utils.remove_x(x_other, num))



    final_list.append(ft_utils.modif_string_to_float(num))
    final_list.append(ft_utils.modif_string_to_float(x_zero))
    final_list.append(ft_utils.modif_string_to_float(x_1))
    final_list.append(ft_utils.modif_string_to_float(x2))

    for x in x_other:
        exponential = re.findall(pattern_expo,x)
        value = re.findall(r"([\+|\-]?[0-9]*[\.]?[0-9]*[X])", x)
        value = ft_utils.remove_x(value, value)
        cmpt = len(final_list)
        while cmpt < int(exponential[0])+1:
            final_list.append(0)
            cmpt += 1 
        final_list.insert(int(exponential[0])+1, int(value[0]))


    return final_list
