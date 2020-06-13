# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from biocontainers_flask.server.models.base_model_ import Model
from biocontainers_flask.server.models.descriptor_type import DescriptorType  # noqa: F401,E501
from biocontainers_flask.server.models.image_data import ImageData  # noqa: F401,E501
from biocontainers_flask.server import util


class ToolVersion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, author: List[str]=None, name: str=None, url: str=None, id: str=None, is_production: bool=None, images: List[ImageData]=None, descriptor_type: List[DescriptorType]=None, containerfile: bool=None, meta_version: str=None, verified: bool=None, verified_source: List[str]=None, signed: bool=None, included_apps: List[str]=None):  # noqa: E501
        """ToolVersion - a model defined in Swagger

        :param author: The author of this ToolVersion.  # noqa: E501
        :type author: List[str]
        :param name: The name of this ToolVersion.  # noqa: E501
        :type name: str
        :param url: The url of this ToolVersion.  # noqa: E501
        :type url: str
        :param id: The id of this ToolVersion.  # noqa: E501
        :type id: str
        :param is_production: The is_production of this ToolVersion.  # noqa: E501
        :type is_production: bool
        :param images: The images of this ToolVersion.  # noqa: E501
        :type images: List[ImageData]
        :param descriptor_type: The descriptor_type of this ToolVersion.  # noqa: E501
        :type descriptor_type: List[DescriptorType]
        :param containerfile: The containerfile of this ToolVersion.  # noqa: E501
        :type containerfile: bool
        :param meta_version: The meta_version of this ToolVersion.  # noqa: E501
        :type meta_version: str
        :param verified: The verified of this ToolVersion.  # noqa: E501
        :type verified: bool
        :param verified_source: The verified_source of this ToolVersion.  # noqa: E501
        :type verified_source: List[str]
        :param signed: The signed of this ToolVersion.  # noqa: E501
        :type signed: bool
        :param included_apps: The included_apps of this ToolVersion.  # noqa: E501
        :type included_apps: List[str]
        """
        self.swagger_types = {
            'author': List[str],
            'name': str,
            'url': str,
            'id': str,
            'is_production': bool,
            'images': List[ImageData],
            'descriptor_type': List[DescriptorType],
            'containerfile': bool,
            'meta_version': str,
            'verified': bool,
            'verified_source': List[str],
            'signed': bool,
            'included_apps': List[str]
        }

        self.attribute_map = {
            'author': 'author',
            'name': 'name',
            'url': 'url',
            'id': 'id',
            'is_production': 'is_production',
            'images': 'images',
            'descriptor_type': 'descriptor_type',
            'containerfile': 'containerfile',
            'meta_version': 'meta_version',
            'verified': 'verified',
            'verified_source': 'verified_source',
            'signed': 'signed',
            'included_apps': 'included_apps'
        }
        self._author = author
        self._name = name
        self._url = url
        self._id = id
        self._is_production = is_production
        self._images = images
        self._descriptor_type = descriptor_type
        self._containerfile = containerfile
        self._meta_version = meta_version
        self._verified = verified
        self._verified_source = verified_source
        self._signed = signed
        self._included_apps = included_apps

    @classmethod
    def from_dict(cls, dikt) -> 'ToolVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ToolVersion of this ToolVersion.  # noqa: E501
        :rtype: ToolVersion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def author(self) -> List[str]:
        """Gets the author of this ToolVersion.

        Contact information for the author of this version of the tool in the registry. (More complex authorship information is handled by the descriptor).  # noqa: E501

        :return: The author of this ToolVersion.
        :rtype: List[str]
        """
        return self._author

    @author.setter
    def author(self, author: List[str]):
        """Sets the author of this ToolVersion.

        Contact information for the author of this version of the tool in the registry. (More complex authorship information is handled by the descriptor).  # noqa: E501

        :param author: The author of this ToolVersion.
        :type author: List[str]
        """

        self._author = author

    @property
    def name(self) -> str:
        """Gets the name of this ToolVersion.

        The name of the version.  # noqa: E501

        :return: The name of this ToolVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ToolVersion.

        The name of the version.  # noqa: E501

        :param name: The name of this ToolVersion.
        :type name: str
        """

        self._name = name

    @property
    def url(self) -> str:
        """Gets the url of this ToolVersion.

        The URL for this tool version in this registry.  # noqa: E501

        :return: The url of this ToolVersion.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ToolVersion.

        The URL for this tool version in this registry.  # noqa: E501

        :param url: The url of this ToolVersion.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def id(self) -> str:
        """Gets the id of this ToolVersion.

        An identifier of the version of this tool for this particular tool registry.  # noqa: E501

        :return: The id of this ToolVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ToolVersion.

        An identifier of the version of this tool for this particular tool registry.  # noqa: E501

        :param id: The id of this ToolVersion.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_production(self) -> bool:
        """Gets the is_production of this ToolVersion.

        This version of a tool is guaranteed to not change over time (for example, a  tool built from a tag in git as opposed to a branch). A production quality tool  is required to have a checksum  # noqa: E501

        :return: The is_production of this ToolVersion.
        :rtype: bool
        """
        return self._is_production

    @is_production.setter
    def is_production(self, is_production: bool):
        """Sets the is_production of this ToolVersion.

        This version of a tool is guaranteed to not change over time (for example, a  tool built from a tag in git as opposed to a branch). A production quality tool  is required to have a checksum  # noqa: E501

        :param is_production: The is_production of this ToolVersion.
        :type is_production: bool
        """

        self._is_production = is_production

    @property
    def images(self) -> List[ImageData]:
        """Gets the images of this ToolVersion.

        All known docker images (and versions/hashes) used by this tool. If the tool has to evaluate any of the docker images strings at runtime, those ones cannot be reported here.  # noqa: E501

        :return: The images of this ToolVersion.
        :rtype: List[ImageData]
        """
        return self._images

    @images.setter
    def images(self, images: List[ImageData]):
        """Sets the images of this ToolVersion.

        All known docker images (and versions/hashes) used by this tool. If the tool has to evaluate any of the docker images strings at runtime, those ones cannot be reported here.  # noqa: E501

        :param images: The images of this ToolVersion.
        :type images: List[ImageData]
        """

        self._images = images

    @property
    def descriptor_type(self) -> List[DescriptorType]:
        """Gets the descriptor_type of this ToolVersion.

        The type (or types) of descriptors available.  # noqa: E501

        :return: The descriptor_type of this ToolVersion.
        :rtype: List[DescriptorType]
        """
        return self._descriptor_type

    @descriptor_type.setter
    def descriptor_type(self, descriptor_type: List[DescriptorType]):
        """Sets the descriptor_type of this ToolVersion.

        The type (or types) of descriptors available.  # noqa: E501

        :param descriptor_type: The descriptor_type of this ToolVersion.
        :type descriptor_type: List[DescriptorType]
        """

        self._descriptor_type = descriptor_type

    @property
    def containerfile(self) -> bool:
        """Gets the containerfile of this ToolVersion.

        Reports if this tool has a containerfile available. (For Docker-based tools, this would indicate the presence of a Dockerfile)  # noqa: E501

        :return: The containerfile of this ToolVersion.
        :rtype: bool
        """
        return self._containerfile

    @containerfile.setter
    def containerfile(self, containerfile: bool):
        """Sets the containerfile of this ToolVersion.

        Reports if this tool has a containerfile available. (For Docker-based tools, this would indicate the presence of a Dockerfile)  # noqa: E501

        :param containerfile: The containerfile of this ToolVersion.
        :type containerfile: bool
        """

        self._containerfile = containerfile

    @property
    def meta_version(self) -> str:
        """Gets the meta_version of this ToolVersion.

        The version of this tool version in the registry. Iterates when fields like the description, author, etc. are updated.  # noqa: E501

        :return: The meta_version of this ToolVersion.
        :rtype: str
        """
        return self._meta_version

    @meta_version.setter
    def meta_version(self, meta_version: str):
        """Sets the meta_version of this ToolVersion.

        The version of this tool version in the registry. Iterates when fields like the description, author, etc. are updated.  # noqa: E501

        :param meta_version: The meta_version of this ToolVersion.
        :type meta_version: str
        """

        self._meta_version = meta_version

    @property
    def verified(self) -> bool:
        """Gets the verified of this ToolVersion.

        Reports whether this tool has been verified by a specific organization or individual.  # noqa: E501

        :return: The verified of this ToolVersion.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified: bool):
        """Sets the verified of this ToolVersion.

        Reports whether this tool has been verified by a specific organization or individual.  # noqa: E501

        :param verified: The verified of this ToolVersion.
        :type verified: bool
        """

        self._verified = verified

    @property
    def verified_source(self) -> List[str]:
        """Gets the verified_source of this ToolVersion.

        Source of metadata that can support a verified tool, such as an email or URL.  # noqa: E501

        :return: The verified_source of this ToolVersion.
        :rtype: List[str]
        """
        return self._verified_source

    @verified_source.setter
    def verified_source(self, verified_source: List[str]):
        """Sets the verified_source of this ToolVersion.

        Source of metadata that can support a verified tool, such as an email or URL.  # noqa: E501

        :param verified_source: The verified_source of this ToolVersion.
        :type verified_source: List[str]
        """

        self._verified_source = verified_source

    @property
    def signed(self) -> bool:
        """Gets the signed of this ToolVersion.

        Reports whether this version of the tool has been signed.  # noqa: E501

        :return: The signed of this ToolVersion.
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed: bool):
        """Sets the signed of this ToolVersion.

        Reports whether this version of the tool has been signed.  # noqa: E501

        :param signed: The signed of this ToolVersion.
        :type signed: bool
        """

        self._signed = signed

    @property
    def included_apps(self) -> List[str]:
        """Gets the included_apps of this ToolVersion.

        An array of IDs for the applications that are stored inside this tool.  # noqa: E501

        :return: The included_apps of this ToolVersion.
        :rtype: List[str]
        """
        return self._included_apps

    @included_apps.setter
    def included_apps(self, included_apps: List[str]):
        """Sets the included_apps of this ToolVersion.

        An array of IDs for the applications that are stored inside this tool.  # noqa: E501

        :param included_apps: The included_apps of this ToolVersion.
        :type included_apps: List[str]
        """

        self._included_apps = included_apps
