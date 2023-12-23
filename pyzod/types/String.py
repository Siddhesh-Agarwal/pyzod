from typing import Dict, Union


class String:
    """
    >>> s = String().set_max(10, "Too long").min(5).allowed("1234567890")
    >>> s.validate("1234567890")
    True
    >>> s.validate("1234")
    False
    >>> s.validate("12345678901")
    ValueError: Too long
    >>> s.validate("qwerty")
    False
    """

    def __init__(self):
        self._min: Union[int, None] = None
        self._max: Union[int, None] = None
        self._error_msg: Dict[str, Union[str, None]] = {}
        self._allowed = None

    def set_min(self, min: int, *, error_msg: Union[str, None] = None):
        """Sets the minimum length of the string"""
        self._min = min
        self._error_msg["min"] = error_msg
        return self

    def set_max(self, max: int, *, error_msg: Union[str, None] = None):
        """Sets the maximum length of the string"""
        self._max = max
        self._error_msg["max"] = error_msg
        return self

    def allowed(self, allowed: str, *, error_msg: Union[str, None] = None):
        """Sets the allowed characters in the string"""
        self._allowed = allowed
        self._error_msg["allowed"] = error_msg
        return self

    def validate(self, value: str):
        """Validates the string"""

        # Check if the string is not too short
        if self._min is not None and len(value) < self._min:
            if "min" in self._error_msg and self._error_msg["min"] is not None:
                raise ValueError(self._error_msg["min"])
            return False

        # Check if the string is not too long
        if self._max is not None and len(value) > self._max:
            if "max" in self._error_msg and self._error_msg["max"] is not None:
                raise ValueError(self._error_msg["max"])
            return False

        # Check if all characters are allowed
        if self._allowed is not None and not all(x in self._allowed for x in value):
            if "allowed" in self._error_msg and self._error_msg["allowed"] is not None:
                raise ValueError(self._error_msg["allowed"])
            return False
        return True
