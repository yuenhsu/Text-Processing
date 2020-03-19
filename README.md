# Text-Processing
 Cleaning and striping line breaks, translating to Chinese using Google Cloud Platform API, and organising layout

---
`translate.command` has one job, running `translate.py`. As I hate having to launch text editor, the command script allows me to run it from terminal and avoid using Atom or VSCode.

You will need to get credentials from Google Cloud Platform to run the script. While the script itself is pretty easy, the process of setting up Google Cloud SDK was time-consuming. Nonetheless, with the script, I won't have to manually go on Google Translate to do the same task!

1. Cleaning the input file: many of the textfile contains multiple linebreaks so the script strips the breaks and organises them into a list.
2. Translating: from the list, translating each paragraph. After the translation returns, append the text in Chinese right below the English because that's how I like to read.
3. Writing file