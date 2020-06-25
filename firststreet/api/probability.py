# Author: Kelvin Lai <kelvin@firststreet.org>
# Copyright: This module is owned by First Street Foundation

# Standard Imports
import logging

# Internal Imports
from firststreet.api import csv_format
from firststreet.api.api import Api
from firststreet.errors import InvalidArgument
from firststreet.models.probability import ProbabilityChance, ProbabilityCount, ProbabilityCountSummary, \
    ProbabilityCumulative, ProbabilityDepth


class Probability(Api):
    """This class receives a list of fsids and handles the creation of a probability product from the request.

        Methods:
            get_depth: Retrieves a list of Probability Depth for the given list of IDs
            get_chance: Retrieves a list of Probability Depth for the given list of IDs
            get_count: Retrieves a list of Probability Depth for the given list of IDs
            get_count_summary: Retrieves a list of Probability Depth for the given list of IDs
            get_cumulative: Retrieves a list of Probability Depth for the given list of IDs
        """

    def get_chance(self, fsids, csv=False, limit=100, output_dir=None):
        """Retrieves probability chance product data from the First Street Foundation API given a list of FSIDs and
        returns a list of Probability Chance objects.

        Args:
            fsids (list/file): A First Street Foundation IDs or a file of First Street Foundation IDs
            csv (bool): To output extracted data to a csv or not
            limit (int): max number of connections to make
            output_dir (str): The output directory to save the generated csvs
        Returns:
            A list of Probability Chance
        """

        # Get data from api and create objects
        api_datas = self.call_api(fsids, "probability", "chance", "property", limit=limit)
        product = [ProbabilityChance(api_data) for api_data in api_datas]

        if csv:
            csv_format.to_csv(product, "probability", "chance", output_dir=output_dir)

        logging.info("Probability Chance Data Ready.")

        return product

    def get_count(self, fsids, location_type, csv=False, limit=100, output_dir=None):
        """Retrieves probability count product data from the First Street Foundation API given a list of FSIDs and
        returns a list of Probability Count objects.

        Args:
            fsids (list/file): A First Street Foundation IDs or a file of First Street Foundation IDs
            location_type (str): The location lookup type
            csv (bool): To output extracted data to a csv or not
            limit (int): max number of connections to make
            output_dir (str): The output directory to save the generated csvs
        Returns:
            A list of Probability Count
        Raises:
            InvalidArgument: The location provided is empty
            TypeError: The location provided is not a string
        """

        if not location_type:
            raise InvalidArgument(location_type)
        elif not isinstance(location_type, str):
            raise TypeError("location is not a string")

        # Get data from api and create objects
        api_datas = self.call_api(fsids, "probability", "count", location_type, limit=limit)
        product = [ProbabilityCount(api_data) for api_data in api_datas]

        if csv:
            csv_format.to_csv(product, "probability", "count", location_type, output_dir=output_dir)

        logging.info("Probability Count Data Ready.")

        return product

    def get_count_summary(self, fsids, csv=False, limit=100, output_dir=None):
        """Retrieves probability Count-Summary product data from the First Street Foundation API given a list of FSIDs
        and returns a list of Probability Count-Summary object.

        Args:
            fsids (list/file): A First Street Foundation IDs or a file of First Street Foundation IDs
            csv (bool): To output extracted data to a csv or not
            limit (int): max number of connections to make
            output_dir (str): The output directory to save the generated csvs
        Returns:
            A list of Probability Count-Summary
        """

        # Get data from api and create objects
        api_datas = self.call_api(fsids, "probability", "count-summary", "property", limit)
        product = [ProbabilityCountSummary(api_data) for api_data in api_datas]

        if csv:
            csv_format.to_csv(product, "probability", "count-summary", output_dir=output_dir)

        logging.info("Probability Count-Summary Data Ready.")

        return product

    def get_cumulative(self, fsids, csv=False, limit=100, output_dir=None):
        """Retrieves probability cumulative product data from the First Street Foundation API given a list of FSIDs and
        returns a list of Probability Cumulative object.

        Args:
            fsids (list/file): A First Street Foundation IDs or a file of First Street Foundation IDs
            csv (bool): To output extracted data to a csv or not
            limit (int): max number of connections to make
            output_dir (str): The output directory to save the generated csvs
        Returns:
            A list of Probability Cumulative
        """

        # Get data from api and create objects
        api_datas = self.call_api(fsids, "probability", "cumulative", "property", limit=limit)
        product = [ProbabilityCumulative(api_data) for api_data in api_datas]

        if csv:
            csv_format.to_csv(product, "probability", "cumulative", output_dir=output_dir)

        logging.info("Probability Cumulative Data Ready.")

        return product

    def get_depth(self, fsids, csv=False, limit=100, output_dir=None):
        """Retrieves probability depth product data from the First Street Foundation API given a list of FSIDs and
        returns a list of Probability Depth objects.

        Args:
            fsids (list/file): A First Street Foundation IDs or a file of First Street Foundation IDs
            csv (bool): To output extracted data to a csv or not
            limit (int): max number of connections to make
            output_dir (str): The output directory to save the generated csvs
        Returns:
            A list of Probability Depth
        """

        # Get data from api and create objects
        api_datas = self.call_api(fsids, "probability", "depth", "property", limit=limit)
        product = [ProbabilityDepth(api_data) for api_data in api_datas]

        if csv:
            csv_format.to_csv(product, "probability", "depth", output_dir=output_dir)

        logging.info("Probability Depth Data Ready.")

        return product
