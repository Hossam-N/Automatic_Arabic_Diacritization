import pickle as pkl
import re
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
        
def clean_dataset(dataset):
    # This function is used to clean an arabic dataset using regex
    
    # Removing diacritics
    # dataset = re.sub('[^ء-ي ]', '', dataset)
    
    # keeping diacritics
    dataset = re.sub(r'[^؀-ۿ ]', '', dataset)
    # remove brackets and other symbols
    # dataset = re.sub(r'[^\u0621-\u063A\u0641-\u064A\s]',' ', dataset)
    # Remove extra spaces
    dataset = re.sub(r'\s+', ' ', dataset)
    return dataset
    