from kedro.pipeline import node, Pipeline
from cc_fraud.pipelines.data_cleaning.nodes import (
    remove_prefix,
    remove_columns
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=remove_prefix,
                inputs="train",
                outputs="removed_prefix_train",
                name="preprocessing_merchant_train",
            ),
            node(
                func=remove_prefix,
                inputs="test",
                outputs="removed_prefix_test",
                name="preprocessing_merchant_test",
            ),
            node(
                func=remove_columns,
                inputs="removed_prefix_train",
                outputs="removed_col_train",
                name="column_removal_train",
            ),
            node(
                func=remove_columns,
                inputs="removed_prefix_test",
                outputs="removed_col_test",
                name="column_removal_test",
            ),
        ]
    )