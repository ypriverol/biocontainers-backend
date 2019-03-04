import math

import pymongo
from pymodm import MongoModel, fields, EmbeddedMongoModel
from pymodm.manager import Manager
from pymodm.queryset import QuerySet
from pymongo.common import WriteConcern
from pymongo.operations import IndexModel

_CONSTANT_TOOL_CLASSES = {
    "CommandLineTool":
        {
            "description": "CommandLineTool",
            "id": "0",
            "name": "CommandLineTool"
        },
    "Workflow":
        {
            "description": "Workflow",
            "id": "1",
            "name": "Workflow"
        },
    "CommandLineMultiTool":
        {
            "description": "CommandLineMultiTool",
            "id": "3",
            "name": "CommandLineMultiTool"
        },
    "Service":
        {
            "description": "Service",
            "id": "4",
            "name": "Service"
        }
}

constants_container_type = ['SINGULARITY', 'DOCKER', 'CONDA']


class PipelineConfiguration:
    def __init__(self, docker_hub, docker_hub_container, docker_hub_tags):
        self.dockerHub = docker_hub
        self.dockerHubContainer = docker_hub_container
        self.dockerHubTags = docker_hub_tags


class ToolClass(EmbeddedMongoModel):
    description = fields.CharField()
    id = fields.CharField(required=True)
    name = fields.CharField()


class ContainerImage(EmbeddedMongoModel):
    """ This class handle how a container is build. Singularity, Docker, Conda, etc. """
    tag = fields.CharField()
    full_tag = fields.CharField(required=True)
    container_type = fields.CharField(max_length=1000, choices=constants_container_type)
    binary_urls = fields.CharField()
    description = fields.CharField()
    recipe_url = fields.CharField()
    license = fields.CharField()
    additional_metadata = fields.CharField()
    size = fields.IntegerField()
    downloads = fields.IntegerField()
    last_updated = fields.DateTimeField()


class Descriptor(EmbeddedMongoModel):
    """
    This class sotrage the information of a Tool descriptor
    """
    id = fields.CharField(max_length=100)


# Mongo Classes to persistent the data model.
class ToolQuerySet(QuerySet):

    def mongo_tool_versions_by_tool(self, tool_id):
        return self.raw({'ref_tool': tool_id})

    def mongo_all_tools(self):
        return list(self.all())

    def get_tool_by_id(self, tool_id):
        return self.raw({'id': tool_id})

    def get_tools_by_name(self, toolname, alias, name):
        query = []
        if name is not None:
            query.append({"name": {"$regex": name}})
        if alias is not None:
            query.append({"aliases": {"$regex": alias}})
        if toolname is not None:
            {"toolname": {"$regex": toolname}}

        return list(self.raw({"$or": query}))

    def exec_query(self, query):
        return self.raw(query)

    def exec_aggregate_query(self, *query):
        return self.aggregate(*query)

    def exec_update_query(self, lookup_condition, update, **kwargs):
        return self.raw(lookup_condition).update(update, **kwargs)

    def get_ids(self, query, sort_order):
        return self.raw(query).only('_id').order_by([('_id', sort_order)])


class ToolVersionQuerySet(QuerySet):

    def mongo_all_tool_versions(self):
        return list(self.all())

    def exec_update_query(self, lookup_condition, update, **kwargs):
        return self.raw(lookup_condition).update(update, **kwargs)

    def get_tool_version_by_id(self, tool_version_id):
        return self.raw({"id": tool_version_id})


class ToolsResponse:
    tools = []
    next_offset = None
    last_page_offset = None


class MongoTool(MongoModel):
    """
    Mongo Tool Class contains the persistence information of a Tool.
    """
    id = fields.CharField(max_length=200, blank=False, required=True)
    name = fields.CharField(max_length=1000, blank=True, required=False)
    description = fields.CharField(blank=True)
    home_url = fields.CharField()
    last_version = fields.CharField()
    organization = fields.CharField()
    has_checker = fields.BooleanField()
    checker_url = fields.CharField(max_length=400)
    is_verified = fields.BooleanField()
    verified_source = fields.CharField(max_length=400)
    registry_url = fields.CharField(max_length=500)
    license = fields.CharField(max_length=1000)
    additional_metadata = fields.CharField()
    tool_classes = fields.EmbeddedDocumentListField('ToolClass')
    authors = fields.ListField(fields.CharField(max_length=200))
    contains = fields.ListField(fields.CharField(max_length=400))
    tool_versions = fields.ListField(fields.CharField(max_length=400))
    additional_identifiers = fields.ListField(fields.CharField(max_length=400))
    registries = fields.ListField(fields.CharField(max_length=200))
    aliases = fields.ListField(fields.CharField())
    checker = fields.BooleanField()
    tool_tags = fields.ListField(fields.CharField())

    manager = Manager.from_queryset(ToolQuerySet)()

    class Meta:
        write_concern = WriteConcern(j=True)
        final = True
        indexes = [IndexModel([("id", pymongo.DESCENDING), ("name", pymongo.DESCENDING)], unique=True)]
        cascade = True

    def get_tool_versions(self):
        return list(MongoToolVersion.manager.mongo_tool_versions_by_tool(self._id))

    def add_authors(self, new_authors):
        """
        This method adds a list of authors to the current list of author of the Tool
        :param new_authors: New Authors
        :return:
        """
        if self.authors is None:
            self.authors = []

        for author in new_authors:
            if author not in self.authors:
                self.authors.append(author)

    def add_registry(self, new_registry):
        """
        This method adds a registry to the current list of registries of the Tool
        :param registry: New registry
        :return:
        """
        if self.registries is None:
            self.registries = []

        if new_registry not in self.registries:
            self.registries.append(new_registry)

    def add_alias(self, new_alias):
        """
        This method adds a registry to the current list of registries of the Tool
        :param registry: New registry
        :return:
        """
        if self.aliases is None:
            self.aliases = []

        if new_alias not in self.aliases:
            self.aliases.append(new_alias)

    def get_main_author(self):
        """
        This method returns first author of the list. The pipeline add the
        BioContainers as first author of the container.
        :return:
        """
        if len(self.authors) > 0:
            return self.authors[0]
        return None

    def get_main_tool_class(self):
        """
        This method return the specific tool
        :return:
        """
        if self.tool_classes is not None and len(self.tool_classes) > 0:
            return self.tool_classes[0]

        return _CONSTANT_TOOL_CLASSES['CommandLineTool']

    @staticmethod
    def get_main_author_dict(authors):
        """
        This method returns first author of the list. The pipeline add the
        BioContainers as first author of the container.
        :return:
        """
        if len(authors) > 0:
            return authors[0]
        return None

    @staticmethod
    def get_main_tool_class_dict(tool_classes):
        """
        This method return the specific tool
        :return:
        """
        if tool_classes is not None and len(tool_classes) > 0:
            return tool_classes[0]

        return _CONSTANT_TOOL_CLASSES['CommandLineTool']

    @staticmethod
    def get_all_tools():
        return MongoTool.manager.mongo_all_tools()

    @staticmethod
    def get_tools_by_name(toolname, alias, name):
        return MongoTool.manager.get_tools_by_name(toolname, alias, name)

    @staticmethod
    def get_tool_by_id(id):
        tools = MongoTool.manager.get_tool_by_id(id)
        tools_list = list(tools)
        if tools_list is not None and len(tools_list) > 0:
            return tools_list[0]
        return None

    @staticmethod
    def get_tools(id=None, alias=None, registry=None, organization=None, name=None, toolname=None, description=None,
                  author=None, checker=None, offset=None, limit=None, is_all_field_search=False,
                  sort_field=None, sort_order=None):

        filters = []
        if id is not None:
            filters.append({"id": id})
        if alias is not None:
            filters.append({"aliases": {"$regex": alias}})
        if registry is not None:
            filters.append({"registries": {"$regex": registry}})
        if organization is not None:
            filters.append({"organization": {"$regex": organization}})
        if toolname is not None:
            filters.append({"name": {"$regex": toolname}})  # toolname : The name of the tool
        if description is not None:
            filters.append({"description": {"$regex": description}})
        if author is not None:
            filters.append({"authors": {"$regex": author}})
        # if checker is not None:  # TODO

        versions_string = "tool_versions"
        if name is not None:  # name : The name of the image i.e., tool_version
            filters.append({("%s.name" % versions_string): {"$regex": name}})

        # Fetch tools along with the tool_versions in one query (similar to SQL join)
        lookup_condition = \
            {"$lookup":
                {
                    "from": "mongo_tool_version",
                    "localField": "name",
                    "foreignField": "name",
                    "as": ("%s" % versions_string)
                }
            }

        if is_all_field_search:
            filters_query = {"$or": filters}
        else:
            filters_query = {"$and": filters}

        match_condition = {"$match": filters_query}

        if sort_field == "toolname":
            sort_field = "name"
        elif sort_field == "description":
            sort_field = "description"
        else:
            sort_field = "id"

        if sort_order is not None and sort_order.lower().startswith("desc"):
            sort_order = pymongo.DESCENDING
        else:
            sort_order = pymongo.ASCENDING

        sort_condition = {'$sort': {sort_field: sort_order}}

        if len(filters) > 0:
            res = MongoTool.manager.exec_aggregate_query(lookup_condition, match_condition, sort_condition)
        else:
            res = MongoTool.manager.exec_aggregate_query(lookup_condition, sort_condition)

        tools = list(res)
        tools_len = len(tools)
        offset = int(offset)
        if offset >= tools_len:  # empty list
            return None

        next_offset = offset + limit
        tools_paginated = tools[offset:next_offset]

        total_pages = math.ceil(tools_len / limit)
        last_page_offset = (total_pages - 1) * limit

        resp = ToolsResponse()
        resp.tools = tools_paginated
        resp.last_page_offset = last_page_offset
        if next_offset < tools_len:
            resp.next_offset = next_offset

        return resp


class MongoToolVersion(MongoModel):
    """
    This class store the information of a Tool version (e.g. PeptideShacker 2.0 )
    """
    id = fields.CharField(max_length=200, blank=False, required=False)
    name = fields.CharField(max_length=1000, blank=True, required=False)
    version = fields.CharField(max_length=1000, blank=False, required=False)
    description = fields.CharField(blank=True)
    home_url = fields.CharField()
    doc_url = fields.CharField()
    license = fields.CharField(max_length=1000)
    additional_identifiers = fields.CharField()
    organization = fields.CharField()
    has_checker = fields.BooleanField()
    checker_url = fields.CharField(max_length=400)
    is_verified = fields.BooleanField()
    verified_source = fields.CharField(max_length=400)
    registry_url = fields.CharField(max_length=500)

    additional_metadata = fields.CharField()
    tool_classes = fields.EmbeddedDocumentListField('ToolClass')
    authors = fields.ListField(fields.CharField(max_length=200))
    contains = fields.ListField(fields.CharField(max_length=400))
    tool_versions = fields.ListField(fields.CharField(max_length=400))
    aliases = fields.ListField(fields.CharField())
    container_recipe = fields.CharField(max_length=500)

    # Specific of Tool Version
    ref_tool = fields.ReferenceField(MongoTool)
    hash_name = fields.CharField(max_length=2000)
    descriptors = fields.EmbeddedDocumentListField('Descriptor')
    image_containers = fields.EmbeddedDocumentListField('ContainerImage')
    last_update = fields.DateTimeField()

    # All queries must be executed via this_manger
    manager = Manager.from_queryset(ToolQuerySet)()
    manager_versions = Manager.from_queryset(ToolVersionQuerySet)()

    @staticmethod
    def get_all_tool_versions():
        return MongoToolVersion.manager_versions.mongo_all_tool_versions()

    @staticmethod
    def get_tool_version_by_id(tool_version_id):
        tools = MongoToolVersion.manager_versions.get_tool_version_by_id(tool_version_id)
        tools_list = list(tools)
        if tools_list is not None and len(tools_list) > 0:
            return tools_list[0]
        return None

    def add_image_container(self, image_container):
        """
        Add a new container image to the to the list of containers.
        :param image_container:
        :return:
        """
        new = True
        for index, image_container_old in enumerate(self.image_containers):
            if image_container.full_tag == image_container_old.full_tag and image_container.container_type == image_container_old.container_type:
                self.image_containers[index] = image_container
                new = False
        if new:
            self.image_containers.append(image_container)

    def __getitem__(self, key):
        if key == self.id:
            return self
        return

    def add_author(self, author):
        """
        This method add a new author to the list of authors of the Tool Version
        :param author: New author
        :return:
        """
        if self.authors is None:
            self.authors = []

        if author not in self.authors:
            self.authors.append(author)

    class Meta:
        write_concern = WriteConcern(j=True)
        final = True
        indexes = [
            IndexModel([("id", pymongo.DESCENDING), ("name", pymongo.DESCENDING), ("version", pymongo.DESCENDING)],
                       unique=True)]


class CondaRecipe:
    """
    This class storage the data of Conda Recipes. This class is use to read metadata from the conda Recipes
    """

    def __init__(self, attributes):
        self.attributes = attributes


class Tool:
    """
    This class contains the information about a tool (PeptideShacker) in Biocontainers, it can be a tool, a workflow, a service or a multi-tool container
    """
    tool_classes = []
    authors = []
    contains = []
    tool_versions = []
    additional_identifiers = []

    def __init__(self, id, name, description, home_url, last_version, organization, has_checker, checker_url,
                 is_verified, verified_source, registry_url, license, additional_metadata):
        self.id = id
        self.name = name
        self.description = description
        self.home_url = home_url
        self.last_version = last_version
        self.organization = organization
        self.has_checker = has_checker
        self.checker_url = checker_url
        self.is_verified = is_verified
        self.verified_source = verified_source
        self.registry_url = registry_url
        self.license = license
        self.additional_metadata = additional_metadata

    def add_tool_class(self, tool_class):
        self.tool_classes.append(tool_class)


class ToolVersion:
    """
    This class store the information of a Tool version (e.g. PeptideShacker 2.0 )
    """
    tool_classes = []
    descriptors = []
    image_containers = []
    contains = []
    authors = []

    def __init__(self, id, name, version, description, home_url, doc_url, license, additional_identifiers, hash_name,
                 last_update, additional_metadata):
        self.id = id
        self.name = name
        self.version = version
        self.description = description
        self.home_url = home_url
        self.doc_url = doc_url
        self.license = license
        self.additional_identifiers = additional_identifiers
        self.hash_name = hash_name
        self.last_update = last_update
        self.additional_metadata = additional_metadata

    def update_downloads(self, downloads):
        self.downloads = downloads

    def add_tool_class(self, tool_class):
        self.tool_classes.append(tool_class)

    def add_image_container(self, image_container):
        self.image_containers.append(image_container)
