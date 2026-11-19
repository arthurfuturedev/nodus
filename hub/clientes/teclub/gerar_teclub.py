"""Gera o hub da TecLub Eng. Coelho: embute as imagens de img/ no teclub.html."""
import base64, re, sys, os
H = os.path.dirname(os.path.abspath(__file__)); out = sys.argv[1]
s = open(H + '/teclub.html', encoding='utf-8').read()
def uri(m):
    f = m.group(1); return 'data:image/jpeg;base64,' + base64.b64encode(open(H + '/img/' + f, 'rb').read()).decode()
s = re.sub(r'\{\{IMG:([\w.-]+)\}\}', uri, s)
open(out, 'w', encoding='utf-8').write(s); print(out, len(s) // 1024, 'KB')
