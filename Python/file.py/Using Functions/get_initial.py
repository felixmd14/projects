print('Input written in English')

def get_initial(name):
    initial = name[0:1].upper()
    return initial

fname = input('Please enter your first name: ')
fname_initial = get_initial(fname)
lname = input('Please enter your last name: ')
lname_initial = get_initial(lname)

print(f'Your initials are: {fname_initial}{lname_initial}')

# OR

print(' \nInput written in Swahili')

def extract_initial(from_name):
    the_initial = from_name[0:1].upper()
    return the_initial

first_name = input('Tafadhali weka jina lako la kwanza: ')
last_name = input('Tafadhali weka jina lako la mwisho: ')

print(f'Herufi za kwanza za jina lako ni: {extract_initial(first_name)}{extract_initial(last_name)}.')