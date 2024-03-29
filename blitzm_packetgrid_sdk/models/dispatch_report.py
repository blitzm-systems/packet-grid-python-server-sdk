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


class DispatchReport(object):
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
        'id': 'str',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'transport_reports': 'list[TransportReport]',
        'notification': 'Notification'
    }

    attribute_map = {
        'id': 'id',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'transport_reports': 'transport_reports',
        'notification': 'notification'
    }

    def __init__(self, id=None, started_at=None, finished_at=None, transport_reports=None, notification=None):  # noqa: E501
        """DispatchReport - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._started_at = None
        self._finished_at = None
        self._transport_reports = None
        self._notification = None
        self.discriminator = None

        self.id = id
        self.started_at = started_at
        self.finished_at = finished_at
        self.transport_reports = transport_reports
        self.notification = notification

    @property
    def id(self):
        """Gets the id of this DispatchReport.  # noqa: E501


        :return: The id of this DispatchReport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DispatchReport.


        :param id: The id of this DispatchReport.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def started_at(self):
        """Gets the started_at of this DispatchReport.  # noqa: E501


        :return: The started_at of this DispatchReport.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this DispatchReport.


        :param started_at: The started_at of this DispatchReport.  # noqa: E501
        :type: datetime
        """
        if started_at is None:
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this DispatchReport.  # noqa: E501


        :return: The finished_at of this DispatchReport.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this DispatchReport.


        :param finished_at: The finished_at of this DispatchReport.  # noqa: E501
        :type: datetime
        """
        if finished_at is None:
            raise ValueError("Invalid value for `finished_at`, must not be `None`")  # noqa: E501

        self._finished_at = finished_at

    @property
    def transport_reports(self):
        """Gets the transport_reports of this DispatchReport.  # noqa: E501


        :return: The transport_reports of this DispatchReport.  # noqa: E501
        :rtype: list[TransportReport]
        """
        return self._transport_reports

    @transport_reports.setter
    def transport_reports(self, transport_reports):
        """Sets the transport_reports of this DispatchReport.


        :param transport_reports: The transport_reports of this DispatchReport.  # noqa: E501
        :type: list[TransportReport]
        """
        if transport_reports is None:
            raise ValueError("Invalid value for `transport_reports`, must not be `None`")  # noqa: E501

        self._transport_reports = transport_reports

    @property
    def notification(self):
        """Gets the notification of this DispatchReport.  # noqa: E501


        :return: The notification of this DispatchReport.  # noqa: E501
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this DispatchReport.


        :param notification: The notification of this DispatchReport.  # noqa: E501
        :type: Notification
        """
        if notification is None:
            raise ValueError("Invalid value for `notification`, must not be `None`")  # noqa: E501

        self._notification = notification

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
        if not isinstance(other, DispatchReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
