'''
간단한 pickle 파일을 만들어보자.
>> 심화 = 옵션을 받아보자. --version 1 --name 1.0.0
'''
import os
import pickle

def save_pickle():
    meta = dict()
    meta['version'] = 1
    meta['version_name'] = '1.0.0'

    os.makedirs('config', exist_ok=True)  # config 폴더가 없으면 생성
    with open('config/meta.pickle', 'wb') as file:
        pickle.dump(meta, file)
    print('save settings in config/setting.pickle')
    
if __name__ == "__main__":
    save_pickle()
    print('Finished')
