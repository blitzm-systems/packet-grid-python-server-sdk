# coding: utf-8

"""
    packetgrid-server-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TransportReport(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'backend_id': 'str',
        'successful': 'bool',
        'failures': 'list[object]'
    }

    attribute_map = {
        'backend_id': 'backend_id',
        'successful': 'successful',
        'failures': 'failures'
    }

    def __init__(self, backend_id=None, successful=None, failures=None):  # noqa: E501
        """TransportReport - a model defined in OpenAPI"""  # noqa: E501

        self._backend_id = None
        self._successful = None
        self._failures = None
        self.discriminator = None

        self.backend_id = backend_id
        self.successful = successful
        self.failures = failures

    @property
    def backend_id(self):
        """Gets the backend_id of this TransportReport.  # noqa: E501

        A string that identitifies the transport type  # noqa: E501

        :return: The backend_id of this TransportReport.  # noqa: E501
        :rtype: str
        """
        return self._backend_id

    @backend_id.setter
    def backend_id(self, backend_id):
        """Sets the backend_id of this TransportReport.

        A string that identitifies the transport type  # noqa: E501

        :param backend_id: The backend_id of this TransportReport.  # noqa: E501
        :type: str
        """
        if backend_id is None:
            raise ValueError("Invalid value for `backend_id`, must not be `None`")  # noqa: E501

        self._backend_id = backend_id

    @property
    def successful(self):
        """Gets the successful of this TransportReport.  # noqa: E501

        This will be true if the transport delievered to all recipients successfully  # noqa: E501

        :return: The successful of this TransportReport.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this TransportReport.

        This will be true if the transport delievered to all recipients successfully  # noqa: E501

        :param successful: The successful of this TransportReport.  # noqa: E501
        :type: bool
        """
        if successful is None:
            raise ValueError("Invalid value for `successful`, must not be `None`")  # noqa: E501

        self._successful = successful

    @property
    def failures(self):
        """Gets the failures of this TransportReport.  # noqa: E501


        :return: The failures of this TransportReport.  # noqa: E501
        :rtype: list[object]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this TransportReport.


        :param failures: The failures of this TransportReport.  # noqa: E501
        :type: list[object]
        """
        if failures is None:
            raise ValueError("Invalid value for `failures`, must not be `None`")  # noqa: E501

        self._failures = failures

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransportReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
