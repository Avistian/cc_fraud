from kedro.pipeline import node, Pipeline
from cc_fraud.pipelines.data_normalization.nodes import (
    label_encoding,
    label_encoding_test
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=label_encoding,
                inputs="removed_col_train",
                outputs=["le_train", "encoders"],
                name="label_encoding_train",
            ),
            node(
                func=label_encoding_test,
                inputs=["removed_col_test", "encoders"],
                outputs="le_test",
                name="label_encoding_test",
            ),
        ]
    )