import os
import shutil
path = os.path
cwd = os.getcwd()

if __name__ == '__main__':
    manifestFile = path.join(cwd, 'manifest.js')
    text = ''
    with open(manifestFile, 'r', encoding='UTF-8') as f:
        txs = f.readlines()
        for i in txs:
            idx1 = i.find('"')
            if idx1 < 0:
                continue
            idx2 = i.find('"', idx1+1)
            if idx2 < 0:
                continue
            n = i[idx1+1:idx2]
            fn = path.join(cwd, n)
            with open(fn, 'r', encoding='UTF-8') as nf:
                text += nf.read()
    with open(manifestFile, 'w', encoding='UTF-8') as f:
        f.write(text)
    os.system('uglifyjs manifest.js -m -o manifest.js')
    js_dir = path.join(cwd, 'js')
    shutil.rmtree(js_dir)
