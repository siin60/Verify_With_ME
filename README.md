# Vulnerability Scanner

This Python package performs non-intrusive vulnerability scanning and enumeration on public endpoints, infrastructure, and applications to identify vulnerabilities and exposures. 

## Features

- Validate a domain.
- Validate an email address.
- Check if an IP address is a known threat.
- Detect various threats in a text input.

## Setup

1. Clone this repository into a separate folder (e.g., `Verify_With_ME`):
    ```sh
    git clone https://github.com/siin60/Verify_With_ME.git Verify_With_ME
    cd Verify_With_ME
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    - On macOS and Linux:
      ```sh
      source .venv/bin/activate
      ```
    - On Windows:
      ```sh
      .venv\Scripts\activate
      ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Install the `cloudmersive-validate-api-client` module:
    ```sh
    pip install cloudmersive-validate-api-client
    ```

## API Key

Ensure you have set your API key in the `utils.py` file. If you do not have an API key, you can get a small business API free plan that allows up to 800 API requests per month from: [Cloudmersive Small Business API](https://cloudmersive.com/pricing-small-business).

## Examples

To see examples, type `examples` when prompted.

- Domain: google.com
- Email: samsmith@gmail.com
- IP: 81.79.7.198 (find your IP at https://www.whatismyip.com/)
- Text: "Your account has been compromised. Please visit http://phishing-site.com to reset your password."

## Usage

Run the scanner:

```sh
python scripts/run_scanner.py