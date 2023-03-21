def get_all_lines(filename: str) -> list:
    """
    Grąžina nuskaityto tekstinio failo  filename  eilutes string sąraše
    """

    with open(filename, "r") as f:
        return f.readlines()
    

def convert_file_lines_to_dic(filename: str) -> list:
    """
    Grąžina faile  filename  esančių santraukų skaičių ir sakinių žodynų sąrašą.
    Sakinio žodynas papildomas eilės numeriu ir visų santraukos sakinių skaičiumi.
    """
        
    all_lines = get_all_lines(filename) #nuskaitom visas faile esančias eilutes
    abstract_count = 0
    list_of_dicts = []

    for line in all_lines:
        if line.startswith("###"):  #tikrinam ar eilutė prasideda simboliais ### (santraukos pradžia)
            abstract = ''           
            abstract_count += 1

        elif line.isspace():        #tikrinam ar eilutė yra tuščia (santraukos pabaiga)
            abstract_lines = abstract.splitlines()
            total = len(abstract_lines)

            
            for i, sentence in enumerate(abstract_lines):
                sentence_parts = sentence.split('\t')   #[0] etiketė, [1] tekstas

                sentence_dict = {}

                sentence_dict['target'] = sentence_parts[0]
                sentence_dict['text'] = sentence_parts[1]
                sentence_dict['number'] = i
                sentence_dict['total'] = total
                
                list_of_dicts.append(sentence_dict)
       
        else:                       #pridedam eilutę prie kitų santraukos eilučių
            abstract += line
    
    return abstract_count, list_of_dicts


def split_sentence_chars(text):
    """
    Grąžina sakinio tekstą su tarpu atskirtais skimboliais

    Args:
        text: skaidomo sakinio tekstas    
    """
    return " ".join(list(text))