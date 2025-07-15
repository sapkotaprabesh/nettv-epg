import json
import requests
from datetime import datetime
import gzip
import html

chans=json.load(open('in/resp.json','r'))['result']['channels']

txt='<?xml version="1.0" encoding="utf-8"?>\n<tv generator-info-name="NETTV EPG Generator : @sapkotaprabesh" generator-info-url="https://github.com/sapkotaprabesh/nettv-epg">'

for ch in chans:
    txt+=f"""\n<channel id="nettv-{ch['id']}">
    <display-name>{html.escape(ch['name'])}</display-name>
    <icon src="{html.escape(ch['logo'])}"></icon>
</channel>"""

for ch in chans:    
    url=f"https://ott-resources.geniustv.geniussystems.com.np/livetv/channels/{ch['id']}/epgs"
    try: r=requests.get(url).json()["result"]
    except: pass
    for yr in r:
        date_obj = datetime.strptime(yr, '%Y-%m-%d')
        programs=r[yr]

        start_times = []
        for pg in programs:
            start_dt = datetime.combine(date_obj, datetime.strptime(pg['time'], '%H:%M:%S').time())
            start_str = start_dt.strftime('%Y%m%d%H%M%S +0000')
            start_times.append(start_str)
            
        start_times.append(datetime.combine(date_obj, datetime.max.time()))

        for i, pg in enumerate(programs):
            if pg['programme_name']=="TBA": continue
            txt+=f"""
    <programme start="{start_times[i]}" stop="{start_times[i+1]}" channel="{ch['id']}" catchup-id="{pg['id']}">
                <title>{html.escape(pg['programme_name'])}</title>
    </programme>"""

txt+="\n</tv>"

with open('out/nettv.xml','w') as f: f.write(txt)    
with open('out/nettv.xml', 'rb') as f_in:
    with gzip.open('out/nettv.xml.gz', 'wb') as f_out:
        f_out.writelines(f_in)
