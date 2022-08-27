from dataclasses import dataclass
from enum import Enum
from re import L

class Label(Enum):
    TOMATO = "tomato"
    BANANA = "banana"
    CHEESE = "cheese"


@dataclass(frozen=True)
class LabelMetrics:
    label: Label
    num_actual_samples: int
    precision: float
    recall: float
    f1: float


test = LabelMetrics(
    label=Label.TOMATO,
    num_actual_samples=1,
    precision=0.8,
    recall=0.34,
    f1="fds"
)

print(test)
print(test.f1)
print(test.label.name)
print(test.label.value)
