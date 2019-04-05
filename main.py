import hashlib
import random


def regenerate_smaller_string(base_string):
    char_index = random.randint(0, len(base_string) - 1)
    return base_string[:char_index] + base_string[char_index + 1:]


def main():
    base_string = "If you want to keep a secret, you must also hide it from yourself"
    new_string = regenerate_smaller_string(base_string)

    sha = hashlib.sha256()
    print('Hashing string:', base_string)
    sha.update(base_string.encode('utf8'))
    sha_base_string_digest = sha.digest()
    print('Digest: ', sha_base_string_digest)
    print('Digest size:', sha.digest_size, ' Block size:', sha.block_size, ' Digest array len:', len(sha_base_string_digest))
    print('-' * 80)

    print('Hashing string:', new_string)
    sha.update(new_string.encode('utf8'))
    sha_new_string_digest = sha.digest()
    print(sha_new_string_digest)
    print('Digest size:', sha.digest_size, ' Block size:', sha.block_size, ' Digest array len:', len(sha_new_string_digest))

    # Counts how many bits changed in each byte
    sha_diff_bit_counts = list(map(lambda x, y: bin(x ^ y).count("1"), sha_base_string_digest, sha_new_string_digest))
    print('Bits changed in each byte:', sha_diff_bit_counts)
    print('Sum:', sum(sha_diff_bit_counts))

    print('=' * 80)

    md = hashlib.md5()
    print('Hashing string:', base_string)
    md.update(base_string.encode('utf8'))
    md_base_string_digest = md.digest()
    print('Digest: ', md_base_string_digest)
    print('Digest size:', md.digest_size, ' Block size:', md.block_size, ' Digest array len:',
          len(md_base_string_digest))
    print('-' * 80)

    print('Hashing string:', new_string)
    sha.update(new_string.encode('utf8'))
    md_new_string_digest = md.digest()
    print(md_new_string_digest)
    print('Digest size:', md.digest_size, ' Block size:', md.block_size, ' Digest array len:', len(md_new_string_digest))

    # Counts how many bits changed in each byte
    md_diff_bit_counts = list(map(lambda x, y: bin(x ^ y).count("1"), md_base_string_digest, md_new_string_digest))
    print('Bits changed in each byte:', md_diff_bit_counts)
    print('Sum:', sum(md_diff_bit_counts))


if __name__ == '__main__':
    main()
