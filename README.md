# Email Accounts Dictionary Program

## Overview
This Python program generates a dictionary containing email account details, including account names, passwords, and other attributes. It simulates the creation of multiple Google accounts with randomly generated information.

---

## Features
- **Account Generation:** Randomly generates account names and passwords.
- **Birthdate Generator:** Creates a random date of birth based on the provided age.
- **Gender Assignment:** Assigns a random gender (male/female) to each account.

---

## Code Description

### Main Functions
1. **`date_o_birth_gen(age)`**
   - **Input:** `age` (integer representing the person's age).
   - **Output:** A dictionary with `day`, `month`, `month_number`, and `year` fields representing the person's date of birth.
   - **Logic:** Randomly selects a day (1–28), a month from a predefined list, and calculates the birth year by subtracting the age from the current year.

2. **`acc_generator()`**
   - **Output:** Generates random attributes for Google accounts such as:
     - Account name
     - Password
     - Gender
     - Email address numbers
   - **Randomization:** Uses predefined character arrays for letters (uppercase and lowercase), vowels, consonants, and numbers to create unique values.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
