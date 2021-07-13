from dataclasses import dataclass


@dataclass(frozen=True)
class LabelMetrics:
    label: str
    num_actual_samples: int
    precision: float
    recall: float
    f1: float


test = LabelMetrics(
    label="tomato",
    num_actual_samples=1,
    precision=0.8,
    recall=0.34,
    f1="fds"
)

print(test)
print(test.f1)
