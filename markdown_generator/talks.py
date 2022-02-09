import pandas as pd
import os

talks = pd.read_csv("talks.tsv", sep="\t", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

loc_dict = {}

for row, item in talks.iterrows():
    
    md_filename = str(item.date) + "-" + item.url_slug + ".md"
    html_filename = str(item.date) + "-" + item.url_slug 
    year = str(item.date)[:4]
    
    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: talks" + "\n"
    
    if len(str(item.type)) > 3:
        md += 'type: "' + item.type + '"\n'
    else:
        md += 'type: "Talk"\n'
    
    md += "permalink: /talks/" + html_filename + "\n"
    
    if len(str(item.venue)) > 3:
        md += 'venue: "' + item.venue + '"\n'
        
    if len(str(item.location)) > 3:
        md += "date: " + str(item.date) + "\n"
    
    if len(str(item.location)) > 3:
        md += 'location: "' + str(item.location) + '"\n'
           
    md += "---\n"
    
    
    if len(str(item.talk_url)) > 3:
        md += "\n[More information here](" + item.talk_url + ")\n" 
        
    
    if len(str(item.description)) > 3:
        md += "\n" + html_escape(item.description) + "\n"
        
        
    md_filename = os.path.basename(md_filename)
    
    with open("../_talks/" + md_filename, 'w') as f:
        f.write(md)

