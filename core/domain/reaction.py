from dataclasses import dataclass

from core.domain.element import Element


@dataclass
class Reaction:
    sequence: int
    left_element: Element
    right_element: Element
    enzymes: []
