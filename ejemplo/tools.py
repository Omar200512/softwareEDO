#Prof. Jorge Arroyo Hernández

## ---------------------------------- ## 
def read_file(file_path):
    text = "" 
    filepath = str(file_path)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            text +=  str("{}".format(line.strip())) + "\n" 
            line = fp.readline()
            cnt += 1
    return text

## ---------------------------------- ## 


