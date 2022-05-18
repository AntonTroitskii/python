import sys
sys.path.extend(['_03_local', '_03_third_party'])

from serializer import json, xml, yaml

from song import Song


song = Song(song_id="1", title="The Same River", artist="Riverside")

print(song.serialize(json.JsonSerializer()))
print(song.serialize(xml.XmlSerializer()))





