# coding: utf-8

from __future__ import absolute_import

from typing import List  # noqa: F401

from biocontainers_flask.server import util
from biocontainers_flask.server.models.base_model_ import Model
from biocontainers_flask.server.models.descriptor_type import DescriptorType  # noqa: F401,E501


class ToolVersion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, url: str=None, id: str=None, image: str=None, registry_url: str=None, image_name: str=None, descriptor_type: List[DescriptorType]=None, containerfile: bool=None, meta_version: str=None, verified: bool=None, verified_source: str=None):  # noqa: E501
        """ToolVersion - a model defined in Swagger

        :param name: The name of this ToolVersion.  # noqa: E501
        :type name: str
        :param url: The url of this ToolVersion.  # noqa: E501
        :type url: str
        :param id: The id of this ToolVersion.  # noqa: E501
        :type id: str
        :param image: The image of this ToolVersion.  # noqa: E501
        :type image: str
        :param registry_url: The registry_url of this ToolVersion.  # noqa: E501
        :type registry_url: str
        :param image_name: The image_name of this ToolVersion.  # noqa: E501
        :type image_name: str
        :param descriptor_type: The descriptor_type of this ToolVersion.  # noqa: E501
        :type descriptor_type: List[DescriptorType]
        :param containerfile: The containerfile of this ToolVersion.  # noqa: E501
        :type containerfile: bool
        :param meta_version: The meta_version of this ToolVersion.  # noqa: E501
        :type meta_version: str
        :param verified: The verified of this ToolVersion.  # noqa: E501
        :type verified: bool
        :param verified_source: The verified_source of this ToolVersion.  # noqa: E501
        :type verified_source: str
        """
        self.swagger_types = {
            'name': str,
            'url': str,
            'id': str,
            'image': str,
            'registry_url': str,
            'image_name': str,
            'descriptor_type': List[DescriptorType],
            'containerfile': bool,
            'meta_version': str,
            'verified': bool,
            'verified_source': str
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url',
            'id': 'id',
            'image': 'image',
            'registry_url': 'registry_url',
            'image_name': 'image_name',
            'descriptor_type': 'descriptor_type',
            'containerfile': 'containerfile',
            'meta_version': 'meta_version',
            'verified': 'verified',
            'verified_source': 'verified_source'
        }

        self._name = name
        self._url = url
        self._id = id
        self._image = image
        self._registry_url = registry_url
        self._image_name = image_name
        self._descriptor_type = descriptor_type
        self._containerfile = containerfile
        self._meta_version = meta_version
        self._verified = verified
        self._verified_source = verified_source

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

        The URL for this tool in this registry  # noqa: E501

        :return: The url of this ToolVersion.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ToolVersion.

        The URL for this tool in this registry  # noqa: E501

        :param url: The url of this ToolVersion.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def id(self) -> str:
        """Gets the id of this ToolVersion.

        An identifier of the version of this tool for this particular tool registry  # noqa: E501

        :return: The id of this ToolVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ToolVersion.

        An identifier of the version of this tool for this particular tool registry  # noqa: E501

        :param id: The id of this ToolVersion.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image(self) -> str:
        """Gets the image of this ToolVersion.

        The docker path to the image (and version) for this tool  # noqa: E501

        :return: The image of this ToolVersion.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this ToolVersion.

        The docker path to the image (and version) for this tool  # noqa: E501

        :param image: The image of this ToolVersion.
        :type image: str
        """

        self._image = image

    @property
    def registry_url(self) -> str:
        """Gets the registry_url of this ToolVersion.

        A URL to a Singularity registry is provided when a specific type of image does not use ids in the Docker format. Used along with image_name to locate a specific image.  # noqa: E501

        :return: The registry_url of this ToolVersion.
        :rtype: str
        """
        return self._registry_url

    @registry_url.setter
    def registry_url(self, registry_url: str):
        """Sets the registry_url of this ToolVersion.

        A URL to a Singularity registry is provided when a specific type of image does not use ids in the Docker format. Used along with image_name to locate a specific image.  # noqa: E501

        :param registry_url: The registry_url of this ToolVersion.
        :type registry_url: str
        """

        self._registry_url = registry_url

    @property
    def image_name(self) -> str:
        """Gets the image_name of this ToolVersion.

        Used in conjunction with a registry_url if provided to locate images  # noqa: E501

        :return: The image_name of this ToolVersion.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name: str):
        """Sets the image_name of this ToolVersion.

        Used in conjunction with a registry_url if provided to locate images  # noqa: E501

        :param image_name: The image_name of this ToolVersion.
        :type image_name: str
        """

        self._image_name = image_name

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

        Reports if this tool has a containerfile available.  # noqa: E501

        :return: The containerfile of this ToolVersion.
        :rtype: bool
        """
        return self._containerfile

    @containerfile.setter
    def containerfile(self, containerfile: bool):
        """Sets the containerfile of this ToolVersion.

        Reports if this tool has a containerfile available.  # noqa: E501

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

        Reports whether this tool has been verified by a specific organization or individual  # noqa: E501

        :return: The verified of this ToolVersion.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified: bool):
        """Sets the verified of this ToolVersion.

        Reports whether this tool has been verified by a specific organization or individual  # noqa: E501

        :param verified: The verified of this ToolVersion.
        :type verified: bool
        """

        self._verified = verified

    @property
    def verified_source(self) -> str:
        """Gets the verified_source of this ToolVersion.

        Source of metadata that can support a verified tool, such as an email or URL  # noqa: E501

        :return: The verified_source of this ToolVersion.
        :rtype: str
        """
        return self._verified_source

    @verified_source.setter
    def verified_source(self, verified_source: str):
        """Sets the verified_source of this ToolVersion.

        Source of metadata that can support a verified tool, such as an email or URL  # noqa: E501

        :param verified_source: The verified_source of this ToolVersion.
        :type verified_source: str
        """

        self._verified_source = verified_source
