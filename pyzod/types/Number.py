from typing import Dict, Literal, Union


class Number:
    """
    >>> Type = Number().upper_bound(10).lower_bound(5).set_type(int)
    >>> Type = Number().set_bounds(5, 10).set_type(int)
    >>> Type.validate(7)
    True
    >>> Type.validate(11)
    False
    >>> Type.validate(4)
    False
    >>> Type.validate(7.5)
    False
    """

    def __init__(self):
        self._upper_bound: Union[int | float, None] = None
        self._lower_bound: Union[int | float, None] = None
        self._error_msg: Dict[str, Union[str, None]] = {}
        self._type = None

    def upper_bound(
        self, upper_bound: int | float, *, error_msg: Union[str, None] = None
    ):
        """Sets the upper bound (included) of the number"""
        self._upper_bound = upper_bound
        self._error_msg["upper_bound"] = error_msg
        return self

    def lower_bound(
        self, lower_bound: int | float, *, error_msg: Union[str, None] = None
    ):
        """Sets the lower bound (included) of the number"""
        self._lower_bound = lower_bound
        self._error_msg["lower_bound"] = error_msg
        return self

    def set_bounds(
        self,
        lower_bound: int | float,
        upper_bound: int | float,
        *,
        error_msg: Union[str, None] = None,
    ):
        """Sets the lower (included) and upper (not included) bounds of the number"""
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._error_msg["lower_bound"] = error_msg
        self._error_msg["upper_bound"] = error_msg
        return self

    def set_type(
        self, type_: Literal["int", "float"], *, error_msg: Union[str, None] = None
    ):
        """Sets the type of the number"""
        self._type = type_
        self._error_msg["type"] = error_msg
        return self

    def validate(self, value: Union[int, float]):
        """Validates the number"""

        # Check if the number is not too small
        if self._lower_bound is not None and value < self._lower_bound:
            if (
                "lower_bound" in self._error_msg
                and self._error_msg["lower_bound"] is not None
            ):
                raise ValueError(self._error_msg["lower_bound"])
            return False

        # Check if the number is not too big
        if self._upper_bound is not None and value > self._upper_bound:
            if (
                "upper_bound" in self._error_msg
                and self._error_msg["upper_bound"] is not None
            ):
                raise ValueError(self._error_msg["upper_bound"])
            return False

        # Check if the number is the correct type
        if self._type is not None and not str(type(value)) == self._type:
            if "type" in self._error_msg and self._error_msg["type"] is not None:
                raise ValueError(self._error_msg["type"])
            return False
        return True
