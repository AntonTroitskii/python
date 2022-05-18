import sys

# благодоря это строке можно расширять пространстов имен. Если в разных пакетах содрежатся одинаковы поддиректории.
# просто добавляем их директорию PahtImport.
sys.path.extend(['_03_local', '_03_third_party'])

from serializers import json, xml, yaml, factory
from song import Song

song = Song(song_id="1", title="The Same River", artist="Riverside")

print(factory.serialize(song, "json"))
print(factory.serialize(song, "yaml"))
print(factory.serialize(song, "toml"))
