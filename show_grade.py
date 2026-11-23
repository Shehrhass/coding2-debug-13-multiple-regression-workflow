"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "f4792af852bcc3aee1085fc6180488f7"
GRADE_HASH = "b91c6a75a019de26ab6fe48c55dbb52a213817cff5eea2aec2c5866e9418fa53"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
