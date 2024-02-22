import pickle

def load_pickle():
    try:
        with open('config/meta.pickle', 'rb') as file:
            meta = pickle.load(file)
            if 'version' not in meta:
                meta['version'] = 1
            if 'version_name' not in meta:
                meta['version_name'] = '1.0.0'
            return meta
    except FileNotFoundError:
        meta = dict()
        meta['version'] = 1
        meta['version_name'] = '1.0.0'
        return meta
    
if __name__ == "__main__":
    meta = load_pickle()
    print(meta)
