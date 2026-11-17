import re, os
refs = set()
for f in ['index.html','js/script.js','css/style.css']:
    t = open(f, encoding='utf-8').read()
    refs.update(re.findall(r'(?:src|href)=["\']?(images/[^"\'\s]+|favicon.svg)', t))
    refs.update(re.findall(r'url\(["\']?(images/[^"\')\s]+)', t))
missing = [r for r in sorted(refs) if not os.path.exists(r)]
print('Referenced assets:', len(refs))
print('Missing:', missing if missing else 'NONE - all present')
