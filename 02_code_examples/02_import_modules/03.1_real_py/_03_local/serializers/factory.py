# local/serializers/factory.py
import sys

# благодоря это строке можно расширять пространстов имен. Если в разных пакетах содрежатся одинаковы поддиректории.
# просто добавляем их директорию PahtImport.
sys.path.extend(['_03_local', '_03_third_party'])

import importlib

def get_serializer(format):
    try:
        module = importlib.import_module(f"serializers.{format}")
        serializer = getattr(module, f"{format.title()}Serializer")
    except (ImportError, AttributeError):
        raise ValueError(f"Unknown format {format!r}") from None

    return serializer()

def serialize(serializable, format):
    serializer = get_serializer(format)
    serializable.serialize(serializer)
    return str(serializer)