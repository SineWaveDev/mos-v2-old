import hashlib
import base64
import os
import hmac

# Json path to validate
JSON_PATH = r"C:\Users\Sinewave#2022\Downloads"
JSON_FILE_NAME = "ITR 3_2024-2025_ITR3 sample 1.json"
JSON_FILE_PATH = os.path.join(JSON_PATH, JSON_FILE_NAME)

ALGORITHM = "sha256"

values = {"SW20000297": ["HeRWGR9kDHyLAOZT", "1790"]}


def main():
    with open(JSON_FILE_PATH, "rb") as f:
        data = f.read().decode("utf-8")
        print("data:",data)

    dig_index = data.index("Digest")

    if (
        data[dig_index + 6] != '"'
        or data[dig_index + 7] != ":"
        or data[dig_index + 8] != '"'
    ):
        print("Invalid Digest key detected")
        return

    swc_index = data.index("SWCreatedBy")
    sw_created_by = data[swc_index + 14 : swc_index + 24]
    print("SwCreatedBy -", sw_created_by)
    if not sw_created_by.startswith("SW") or len(sw_created_by) != 10:
        print("Invalid SWCreatedBy")
        return

    digest_bef = data[: dig_index + 9]
    dig_value_colon_end_index = data.index('"', dig_index + 9)
    digest_aft = data[dig_value_colon_end_index :]

    hash_to_gen_for = digest_bef + "-" + digest_aft

    key_itrtns = get_key_iteration(sw_created_by)
    if not key_itrtns:
        print(f"No key and iteration found for SWCreatedBy: {sw_created_by}")
        return

    key = key_itrtns[0]
    iteration = int(key_itrtns[1])

    generated_digest = generate_hash_for_string(hash_to_gen_for, iteration, key)
    print("Digest -", generated_digest)


def get_key_iteration(sw_created_by):
    return values.get(sw_created_by, [])


def validate_hash(f, iteration, key, hash_in_xml):
    start_time = os.times()[0]

    hmac_instance = hmac.new(key.encode("utf-8"), digestmod=ALGORITHM)

    hash_updated = False

    while True:
        bytes_buffer = f.read(2048)
        if not bytes_buffer:
            break

        read_byte_str = bytes_buffer.decode("utf-8")

        start_index = read_byte_str.find(hash_in_xml)

        if not hash_updated and start_index != -1:
            end_index = start_index + len(hash_in_xml)

            read_byte_str = (
                read_byte_str[:start_index] + "-" + read_byte_str[end_index:]
            )

            hmac_instance.update(read_byte_str.encode("utf-8"))

            hash_updated = True
        else:
            hmac_instance.update(bytes_buffer)

    digest_value = hmac_instance.digest()

    for _ in range(iteration):
        hmac_instance = hmac.new(key.encode("utf-8"), digestmod=ALGORITHM)
        hmac_instance.update(digest_value)
        digest_value = hmac_instance.digest()

    generated_hash = base64.b64encode(digest_value).decode("utf-8")

    end_time = os.times()[0]

    return generated_hash == hash_in_xml


def generate_hash_for_string(content, iteration, key):
    hmac_instance = hmac.new(key.encode("utf-8"), content.encode("utf-8"), digestmod=ALGORITHM)

    digest_value = hmac_instance.digest()

    for _ in range(iteration):
        hmac_instance = hmac.new(key.encode("utf-8"), digestmod=ALGORITHM)
        hmac_instance.update(digest_value)
        digest_value = hmac_instance.digest()

    generated_hash = base64.b64encode(digest_value).decode("utf-8")

    return generated_hash


if __name__ == "__main__":
    main()
