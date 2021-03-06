# coding: utf-8

from __future__ import absolute_import

from biocontainers_flask.server import util
from biocontainers_flask.server.models.base_model_ import Model


class Metadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, version: str=None, api_version: str=None, country: str=None, friendly_name: str=None):  # noqa: E501
        """Metadata - a model defined in Swagger

        :param version: The version of this Metadata.  # noqa: E501
        :type version: str
        :param api_version: The api_version of this Metadata.  # noqa: E501
        :type api_version: str
        :param country: The country of this Metadata.  # noqa: E501
        :type country: str
        :param friendly_name: The friendly_name of this Metadata.  # noqa: E501
        :type friendly_name: str
        """
        self.swagger_types = {
            'version': str,
            'api_version': str,
            'country': str,
            'friendly_name': str
        }

        self.attribute_map = {
            'version': 'version',
            'api_version': 'api_version',
            'country': 'country',
            'friendly_name': 'friendly_name'
        }

        self._version = version
        self._api_version = api_version
        self._country = country
        self._friendly_name = friendly_name

    @classmethod
    def from_dict(cls, dikt) -> 'Metadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Metadata of this Metadata.  # noqa: E501
        :rtype: Metadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this Metadata.

        The version of this registry  # noqa: E501

        :return: The version of this Metadata.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this Metadata.

        The version of this registry  # noqa: E501

        :param version: The version of this Metadata.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def api_version(self) -> str:
        """Gets the api_version of this Metadata.

        The version of the GA4GH tool-registry API supported by this registry  # noqa: E501

        :return: The api_version of this Metadata.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this Metadata.

        The version of the GA4GH tool-registry API supported by this registry  # noqa: E501

        :param api_version: The api_version of this Metadata.
        :type api_version: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def country(self) -> str:
        """Gets the country of this Metadata.

        A country code for the registry (ISO 3166-1 alpha-3)  # noqa: E501

        :return: The country of this Metadata.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this Metadata.

        A country code for the registry (ISO 3166-1 alpha-3)  # noqa: E501

        :param country: The country of this Metadata.
        :type country: str
        """

        self._country = country

    @property
    def friendly_name(self) -> str:
        """Gets the friendly_name of this Metadata.

        A friendly name that can be used in addition to the hostname to describe a registry  # noqa: E501

        :return: The friendly_name of this Metadata.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name: str):
        """Sets the friendly_name of this Metadata.

        A friendly name that can be used in addition to the hostname to describe a registry  # noqa: E501

        :param friendly_name: The friendly_name of this Metadata.
        :type friendly_name: str
        """

        self._friendly_name = friendly_name
