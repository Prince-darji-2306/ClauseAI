import re
import unicodedata

def clean_legal_text(text):
    text = unicodedata.normalize("NFKC", text)

    # 2️⃣ Replace non-breaking spaces and other weird whitespace
    text = text.replace("\xa0", " ").replace("\u200b", "")

    # 3️⃣ Remove multiple consecutive spaces within a line
    text = re.sub(r" {2,}", " ", text)

    # 4️⃣ Remove trailing spaces at line ends
    text = "\n".join([line.rstrip() for line in text.splitlines()])

    # 5️⃣ Remove empty lines at the start and end
    text = text.strip()

    return text