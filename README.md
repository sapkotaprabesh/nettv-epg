# nettv-epg

- nettv epg link: https://sapkotaprabesh.github.io/nettv-epg/out/nettv.xml
- free nettv nepali channels stream m3u link: https://sapkotaprabesh.github.io/tv/nettv.m3u

# for self hosting

### epg.py

- fetches epg json data from https://ott-resources.geniustv.geniussystems.com.np/livetv/channels/<channel_id>/epgs
- parses it to xml format and compress into gz for iptv players to read it.

### usage
- epg.py requires channels details json file. 
- to get it, login to https://webtv.nettv.com.np/livetv while checking network tab
- save the response to the request made to this url as `in/resp.json`:
https://ott-livetv-resources.geniustv.geniussystems.com.np/subscriber/livetv/v1/namespaces/<xyz>/subscribers/<pqr>/serial/<abc>-<xyz>
- run: `python epg.py`
- get epg files in `out/` directory
