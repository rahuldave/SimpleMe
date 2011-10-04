import json
import markdown
import sys
import meta2
import time
import datetime

myext=meta2.makeExtension()
text=open(sys.argv[1]).read()
print text
print '------------------------------'
md = markdown.Markdown(extensions = [myext])
html = md.convert(text)

print html
print '------------------------------'
outdict={}
# View meta-data
metadict=md.Meta
blessed_keys=['title', 'metadata', 'tags', 'created-at', 'timestamp']
print metadict
for ele in metadict.keys():
    if ele in blessed_keys:
        if ele =='tags' or ele=='metadata':
            outdict[ele]=metadict[ele][0].split(',')
        else:
            outdict[ele]=metadict[ele][0]
        if ele=='timestamp' or ele=='created-at':
            outdict[ele]=datetime.datetime.strptime(outdict[ele], "%Y-%m-%d %H:%M:%S %Z").isoformat()       
print json.dumps(outdict)
