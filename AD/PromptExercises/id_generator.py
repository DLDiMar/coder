import uuid

def id_generator(number_guids):
    guids = []
    for _ in range(number_guids):
        guid = uuid.uuid4()
        guid_str = guid.hex
        guid_str = guid_str[:8] + '-' + guid_str[8:12] + '-' + guid_str[12:16] + '-' + guid_str[16:20] + '-' + guid_str[20:]
        guids.append(guid_str)
    return guids


print(id_generator(5))