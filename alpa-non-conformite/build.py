import base64,sys
t=open(sys.argv[1]).read(); b=base64.b64encode(open(sys.argv[2],'rb').read()).decode()
open(sys.argv[3],'w').write(t.replace('__PDF_BASE64__',b))
