def sum_numbers(*args):
    return sum([*args])



def get_multiplied_amount(multiplier, *args):
    return sum([*args]) *multiplier



def word_concatenator(*args):
    return " ".join([*args])




def inverted_word_factory(*args):
    new_str = " ".join([*args])
    return new_str[len(new_str) ::-1]



def dictionary_separator(**kwargs):
    keys = list()
    values = list()
    for key, value in kwargs.items():
        keys.append(key)
        values.append(value)
    return (keys, values)
    



def dictionary_creator(*args, **kwargs):
    new = list(kwargs.values())
    if len(args) < len(new) :
        return None
   
   

    new_dict = dict()
    for index in range(len(new)):
        print(index)
        new_dict[args[index]] = new[index]
    return new_dict




def purchase_logger(**kwargs):
    values = list(kwargs.values())
    keys = ['Product', 'costs', 'and was bought' ]
    new_str = ""
    for index in range(len(keys)):
        if index == 2 :
            new_str += (f'{keys[index]} {values[index]}')
            
        else:
            new_str += (f'{keys[index]} {values[index]} ')
    return new_str




def world_cup_logger(country, *args):
    final_str= (f'{country} -')

    for year in sorted(args):
        if year == sorted(args)[len(args) -1]:
            final_str+=(f' e {year}')
        elif year == sorted(args)[len(args) -2]:
            final_str+=(f' {year}')
        else:
            final_str +=(f' {year},')
    return final_str

