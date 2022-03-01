# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
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
# from paddle_serving_server.pipeline import PipelineClient
import requests
import json

url = "http://127.0.0.1:9999/ppTSN/prediction"
video_url = "https://paddle-serving.bj.bcebos.com/huangjianhui04/example.avi"
for i in range(4):
    data = {"key": ["filename"], "value": [video_url]}
    r = requests.post(url=url, data=json.dumps(data))
    print(r.json())