from kedro.pipeline import node, Pipeline
from cc_fraud.pipelines.model_training.nodes import (
    train_model,
    evaluate_model
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=train_model,
                inputs="le_train",
                outputs="classifier",
                name="training",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "le_test"],
                outputs=None,
                name="evaluation",
            ),
        ]
    )