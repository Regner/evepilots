

from evepilots.capsuleers.services import capsuleers


def update_multiple_capsuleers(quantity=1):
    """
        Selects a number of existing capsuleers and updates them.
        
        :param quantity: the number of capsuleers to update
    """

    for capsuleer in capsuleers.get_needing_update(quantity):
        capsuleers.update_information.delay(capsuleer)


def load_capsuleers_file(file_path):
    """
        Loads capsuleers into the DB for later updating. This process just loads
        the capsuleer and their ID with all other fields being Null.
        
        :param file_path: path to a file containing one capsuleer ID per line
    """
    with open(file_path, 'r') as f:
        char_ids = f.readlines()
        for char_id in char_ids:
            char_id = int(char_id.strip('\n'))
            
            if char_id > 90000000:
                if capsuleers.get(char_id) is None:
                    print 'Unable to find {} so adding...'.format(char_id)
                    capsuleers.create(**{'id': char_id})
