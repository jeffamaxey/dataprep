"""
Implement categorical constant imputer.
"""

# pylint: disable=unused-argument
from typing import Any, List, Optional
import dask.dataframe as dd


class ConstantImputer:
    """Constant imputer for imputing categorical values
    Attributes:
        null_values
            Specified null values which should be recognized
        fill_value
            Value used for imputing missing values, the default value is "Missing"
    """

    def __init__(self, null_values: Optional[List[Any]], fill_value: str = "") -> None:
        """
        This function initiate constant imputer.

        Parameters
        ----------
        null_values
            Specified null values which should be recognized
        fill_value
            Value used for imputing missing values.
        """

        self.null_values = null_values
        self.fill_value = "Missing" if len(fill_value) == "" else fill_value

    def fit(self, col_df: dd.Series) -> Any:
        """
        Constant imputer don't need to fit any parameter.

        Parameters
        ----------
        col_df
            Provided data column.
        """

        return self

    def transform(self, col_df: dd.Series) -> dd.Series:
        """
        Impute the provided data column with the fitted parameters.

        Parameters
        ----------
        col_df
            Provided data column.
        """

        return col_df.map(self.fillna)

    def fit_transform(self, col_df: dd.Series) -> dd.Series:
        """
        Impute the data column with constant value.

        Parameters
        ----------
        col_df
            Data column.
        """

        return self.fit(col_df).transform(col_df)

    def fillna(self, val: str) -> str:

        """
        Check if the value is in the list of null value.
        If yes, impute the data column with constant value.
        If no, just return the value.

        Parameters
        ----------
        val
            Each value in dask's Series
        """

        if self.null_values is not None and val in self.null_values:
            return self.fill_value
        return val
