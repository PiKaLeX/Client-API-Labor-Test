# coding: utf-8

"""
    MANUFACTURING/18.100.001

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class HttpError(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'message': 'str',
        'message_detail': 'str',
        'exception_message': 'str',
        'exception_type': 'str',
        'stack_trace': 'str',
        'model_state': 'dict(str, list[str])'
    }

    attribute_map = {
        'message': 'message',
        'message_detail': 'messageDetail',
        'exception_message': 'exceptionMessage',
        'exception_type': 'exceptionType',
        'stack_trace': 'stackTrace',
        'model_state': 'modelState'
    }

    def __init__(self, message=None, message_detail=None, exception_message=None, exception_type=None, stack_trace=None, model_state=None, _configuration=None):  # noqa: E501
        """HttpError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._message_detail = None
        self._exception_message = None
        self._exception_type = None
        self._stack_trace = None
        self._model_state = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if message_detail is not None:
            self.message_detail = message_detail
        if exception_message is not None:
            self.exception_message = exception_message
        if exception_type is not None:
            self.exception_type = exception_type
        if stack_trace is not None:
            self.stack_trace = stack_trace
        if model_state is not None:
            self.model_state = model_state

    @property
    def message(self):
        """Gets the message of this HttpError.  # noqa: E501


        :return: The message of this HttpError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HttpError.


        :param message: The message of this HttpError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def message_detail(self):
        """Gets the message_detail of this HttpError.  # noqa: E501


        :return: The message_detail of this HttpError.  # noqa: E501
        :rtype: str
        """
        return self._message_detail

    @message_detail.setter
    def message_detail(self, message_detail):
        """Sets the message_detail of this HttpError.


        :param message_detail: The message_detail of this HttpError.  # noqa: E501
        :type: str
        """

        self._message_detail = message_detail

    @property
    def exception_message(self):
        """Gets the exception_message of this HttpError.  # noqa: E501


        :return: The exception_message of this HttpError.  # noqa: E501
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """Sets the exception_message of this HttpError.


        :param exception_message: The exception_message of this HttpError.  # noqa: E501
        :type: str
        """

        self._exception_message = exception_message

    @property
    def exception_type(self):
        """Gets the exception_type of this HttpError.  # noqa: E501


        :return: The exception_type of this HttpError.  # noqa: E501
        :rtype: str
        """
        return self._exception_type

    @exception_type.setter
    def exception_type(self, exception_type):
        """Sets the exception_type of this HttpError.


        :param exception_type: The exception_type of this HttpError.  # noqa: E501
        :type: str
        """

        self._exception_type = exception_type

    @property
    def stack_trace(self):
        """Gets the stack_trace of this HttpError.  # noqa: E501


        :return: The stack_trace of this HttpError.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this HttpError.


        :param stack_trace: The stack_trace of this HttpError.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

    @property
    def model_state(self):
        """Gets the model_state of this HttpError.  # noqa: E501


        :return: The model_state of this HttpError.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._model_state

    @model_state.setter
    def model_state(self, model_state):
        """Sets the model_state of this HttpError.


        :param model_state: The model_state of this HttpError.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._model_state = model_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HttpError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HttpError):
            return True

        return self.to_dict() != other.to_dict()