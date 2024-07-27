# SafePass Scout
This Python script checks the security of passwords by querying the [Pwned Passwords API](https://haveibeenpwned.com/Passwords). The API allows you to check if a password has been previously exposed in data breaches. The script uses the k-anonymity model, which means it doesn't send the entire password to the API but only the first five characters of its SHA-1 hash.

## How to Use

1. Ensure you have Python installed on your machine.
2. Clone this repository:

    ```bash
    git clone https://github.com/rahul-pawan-somani/password-checker.git
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
