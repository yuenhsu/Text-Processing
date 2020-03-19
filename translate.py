from google.cloud import translate_v2 as translate
import sys
import subprocess
import os
from time import sleep

#setup credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'json path'
translate_client = translate.Client()

#strip link breaks
content = ""

with open('text_file') as f:
    for line in f:
        if line.strip() != '':
            content += line

#seperate paragraphs
paragraph = [line for line in content.split('\n')]

output = ""

#translate
for par in paragraph:
    results = translate_client.translate(par, target_language='zh-TW')
    sleep(1)
    trans_results = results['translatedText']
    output = output + par + '\n' + trans_results + '\n'


with open('output_file', 'w') as of:
    for line in output.split('\n'):
        # I prefer big paragraph breaks so I added 2.
        print(line, file=of, end='\n\n')

#system open the output file
subprocess.call(['open','output_file'])