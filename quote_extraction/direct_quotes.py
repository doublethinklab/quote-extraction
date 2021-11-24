import re


def replace(text: str, replacement: str = 'QUOTE') -> str:
    """Replaces direct quotes in text with a placeholder token.

    Args:
        text: String. A contiguous sequence of text from which you want to
            extract direct quotes.
        replacement: String. The placeholder to put in place of direct quotes.

    Returns:
        String: original text with direct quotes replaced by `replacement`.

    Example:
        extract('They said, "This is my quote."', 'QUOTE') -> 'They said QUOTE.'
    """
    raise NotImplementedError
