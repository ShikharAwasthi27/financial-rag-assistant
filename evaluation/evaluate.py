from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy
)


def run_evaluation(dataset):

    result = evaluate(
        dataset,
        metrics=[
            faithfulness,
            answer_relevancy
        ]
    )

    print(result)
