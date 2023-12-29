import pickle as pkl
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
        
