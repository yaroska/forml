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

"""
Pyfunc runner tests.
"""

import pytest

import forml
from forml import io, runtime
from forml.io import asset, layout
from forml.provider.runner import pyfunc

from . import Runner


class TestRunner(Runner):
    """Runner tests."""

    @staticmethod
    @pytest.fixture(scope='function')
    def runner(valid_instance: asset.Instance, feed_instance: io.Feed, sink_instance: io.Sink) -> pyfunc.Runner:
        """Runner fixture."""
        return pyfunc.Runner(valid_instance, feed_instance, sink_instance)

    def test_train(self, runner: runtime.Runner):
        """Overridden train test."""
        with pytest.raises(forml.InvalidError, match='Invalid runner mode'):
            super().test_train(runner)

    def test_call(self, runner: pyfunc.Runner, testset_entry: layout.Entry, generation_prediction: layout.Array):
        """Pyfunc call mode test."""
        assert tuple(runner.call(testset_entry).data) == generation_prediction
