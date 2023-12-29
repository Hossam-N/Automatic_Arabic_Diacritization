import pickle as pkl
import re


def clean_dataset(dataset, remove_diacritics=False):
    # This function is used to clean an arabic dataset using regex
    
    # keeping diacritics
    dataset = re.sub(r'[^؀-ۿ .]', '', dataset)    # remove brackets and other symbols
    if remove_diacritics:
        dataset = re.sub(r'[\u064B-\u065F]', '', dataset)
    
    # Remove extra spaces and newlines
    dataset = re.sub(r'\s+', ' ', dataset)
    dataset = re.sub(r'\n+', '.', dataset)
    return dataset



def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
def read_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pkl.load(f)
    
def write_pickle(file_path, content):
    with open(file_path, 'wb') as f:
        pkl.dump(content, f)

    return   


        
    