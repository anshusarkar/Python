import re

re.split(r"[.?!]", "One sentence. Another one? And the last one!")                           # The split method splits sentences into two sentences by lokking for '.' , '?', '!' at the end of each sentences 

re.split(r"([.?!])", "One sentence. Another one? And the last one!")                         # To include both annotation marks and the sentences with them the rwa string must be putted in ()

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

