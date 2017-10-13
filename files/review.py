# review.py
# Introduction to Web Scraping with Python
# Harvard IQSS
# October 13, 2017

# NaLette Brodnax
# nbrodnax@iq.harvard.edu
# www.nalettebrodnax.com


datasets = ['airport', 'baseball', 'calcium', 'electricbill', 'freethrows']
print(datasets[0])
print(datasets[2:4])
print(datasets[-2])

data_info = {'filename': 'airport', 'title': 'US Airport Statistics',
             'observations': 135}
print(data_info['title'])

for name in datasets:
    print(name + '.txt')

def add_extensions(names):
    """adds '.txt' to each string in a list
    list of str -> list of str"""
    filenames = []
    for name in names:
        filenames.append(name + '.txt')
    return filenames

print(add_extensions(datasets))

import requests
page = requests.get('http://ww2.amstat.org/publications/jse/jse_data_archive.htm')
print(page)


      
