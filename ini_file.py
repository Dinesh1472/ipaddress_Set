import configparser
try:
    config = configparser.ConfigParser()

    #parser existing file
    config.read('fileread.ini')

    #read values from a section
    string_val =config.get('section_a','string_val')
    print(string_val)

    bool_val =config.getboolean('section_a','bool_val')
    print(bool_val)

    int_val =config.get('section_a','int_val')
    print(int_val)

    float_val =config.getfloat('section_a','pi_val')
    print(float_val)

except Exception as e:
    print(e)
