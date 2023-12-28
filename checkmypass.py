import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firts5_char, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(firts5_char)
    return get_pass_leak_count(response, tail)


def main(passwords):
    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f'{password} this has been used {count} times')
        else:
            print(
                f'as per my knowledge, no one has used {password} as their password before')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
