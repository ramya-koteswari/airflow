#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import time  # noqa
import uuid  # noqa
from datetime import datetime, timedelta
from random import random  # noqa
from typing import Any, Optional, Union

import dateutil  # noqa
import lazy_object_proxy

from airflow.macros import hive  # noqa


def ds_add(ds: Union[str, lazy_object_proxy.Proxy], days: int) -> str:
    """
    Add or subtract days from a YYYY-MM-DD

    :param ds: anchor date in ``YYYY-MM-DD`` format to add to
    :type ds: str
    :param days: number of days to add to the ds, you can use negative values
    :type days: int

    >>> ds_add('2015-01-01', 5)
    '2015-01-06'
    >>> ds_add('2015-01-06', -5)
    '2015-01-01'
    """
    if not days:
        return str(ds)
    dt = datetime.strptime(str(ds), "%Y-%m-%d") + timedelta(days=days)
    return dt.strftime("%Y-%m-%d")


def ds_format(ds: Union[str, lazy_object_proxy.Proxy], input_format: str, output_format: str) -> str:
    """
    Takes an input string and outputs another string
    as specified in the output format

    :param ds: input string which contains a date
    :type ds: str
    :param input_format: input string format. E.g. %Y-%m-%d
    :type input_format: str
    :param output_format: output string format  E.g. %Y-%m-%d
    :type output_format: str

    >>> ds_format('2015-01-01', "%Y-%m-%d", "%m-%d-%y")
    '01-01-15'
    >>> ds_format('1/5/2015', "%m/%d/%Y",  "%Y-%m-%d")
    '2015-01-05'
    """
    return datetime.strptime(str(ds), input_format).strftime(output_format)


def datetime_diff_for_humans(dt: Any, since: Optional[datetime] = None) -> str:
    """
    Return a human-readable/approximate difference between two datetimes, or
    one and now.

    :param dt: The datetime to display the diff for
    :type dt: datetime.datetime
    :param since: When to display the date from. If ``None`` then the diff is
        between ``dt`` and now.
    :type since: None or datetime.datetime
    :rtype: str
    """
    import pendulum

    return pendulum.instance(dt).diff_for_humans(since)
