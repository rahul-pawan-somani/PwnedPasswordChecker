# Password Checker
This Python script checks the security of passwords by querying the [Pwned Passwords API](https://haveibeenpwned.com/Passwords). The API allows you to check if a password has been previously exposed in data breaches. The script uses the k-anonymity model, which means it doesn't send the entire password to the API but only the first five characters of its SHA-1 hash.

## How to Use

1. Ensure you have Python installed on your machine.
2. Clone this repository:

    ```bash
    git clone https://github.com/your-username/password-checker.git
    ```

3. Navigate to the project directory:

    ```bash
    cd password-checker
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the script with one or more passwords as arguments:

    ```bash
    python password_checker.py password1 password2 password3
    ```

    Replace `password1`, `password2`, and `password3` with the passwords you want to check.

## Example

```bash
python password_checker.py password123 securepassword mysecretpassword
```

## Notes

- Make sure not to store sensitive passwords or any critical information in plaintext within this repository.
- The script uses the `requests` library to interact with the Pwned Passwords API, so an active internet connection is required.

## Disclaimer

This script relies on a third-party service (Pwned Passwords API) and may be subject to its terms of use. Use it responsibly and avoid violating any terms or conditions set by the API provider.

## Contribution

Feel free to contribute to this project by opening issues or creating pull requests. Your feedback and suggestions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
