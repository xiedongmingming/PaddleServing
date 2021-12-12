import pytest
# coding:utf-8
# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''
This module is used to check whether the running environment for PaddleServing is configured correctly.

Two test cases are set for verifying the smooth of environment, fit a line test case for C++ Serving environment and uci for Pipeline Serving enviroment

Usage: export PYTHON_EXECUTABLE=/usr/local/bin/python3.6
       python3.6 -m paddle_serving_server.serve check
'''


import sys
import os

cpp_test_cases = ["test_fit_a_line.py::TestFitALine::test_cpu", "test_fit_a_line.py::TestFitALine::test_gpu"]
pipeline_test_cases = ["test_uci_pipeline.py::TestUCIPipeline::test_cpu", "test_uci_pipeline.py::TestUCIPipeline::test_gpu"]

def run_test_cases(cases_list, case_type):
    old_stdout, old_stderr = sys.stdout, sys.stderr
    real_path = os.path.dirname(os.path.realpath(__file__))
    for case in cases_list:
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
        args_str = "--disable-warnings " + str(real_path) + "/" + case
        args = args_str.split(" ")
        res = pytest.main(args)
        sys.stdout, sys.stderr = old_stdout, old_stderr
        if res == 0:
            print("{} {} environment running success".format(case_type, case[-3:]))
        else:
            print("{} {} environment running failure, if you need this environment, please refer to https://github.com/PaddlePaddle/Serving/blob/v0.7.0/doc/Install_CN.md to configure environment".format(case_type, case[-3:]))
    
def unset_proxy(key):
    os.unsetenv(key)

def check_env():
    if 'https_proxy' in os.environ or 'http_proxy' in os.environ:
        unset_proxy("https_proxy") 
        unset_proxy("http_proxy")     
    run_test_cases(cpp_test_cases, "C++")
    run_test_cases(pipeline_test_cases, "Pipeline")