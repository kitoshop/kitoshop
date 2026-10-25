#!/usr/bin/env python3
"""Run before publishing: python configure-domain.py https://your-real-domain.example"""
from pathlib import Path
import sys
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
 raise SystemExit('Usage: python configure-domain.py https://YOUR-ACTUAL-DOMAIN')
origin=sys.argv[1].rstrip('/')
for p in Path(__file__).parent.glob('*/index.html'):
 text=p.read_text(encoding='utf-8')
 text=text.replace('__SITE_ORIGIN__',origin)
 p.write_text(text,encoding='utf-8')
print('Configured:',origin)
