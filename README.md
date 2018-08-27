[![banner](https://raw.githubusercontent.com/oceanprotocol/art/master/github/repo-banner%402x.png)](https://oceanprotocol.com)

# oceandb-bigchaindb-driver

> 🐳 Ocean DB [BigchainDB](https://www.bigchaindb.com/) driver (Python).
> [oceanprotocol.com](https://oceanprotocol.com)

[![Travis (.com)](https://img.shields.io/travis/com/oceanprotocol/oceandb-bigchaindb-driver.svg)](https://travis-ci.com/oceanprotocol/oceandb-bigchaindb-driver)
[![Codacy coverage](https://img.shields.io/codacy/coverage/be42a51b898e46c7b7c2531d49a4e1ac.svg)](https://app.codacy.com/project/ocean-protocol/oceandb-bigchaindb-driver/dashboard)
[![PyPI](https://img.shields.io/pypi/v/oceandb-bigchaindb-driver.svg)](https://pypi.org/project/oceandb-bigchaindb-driver/)
[![GitHub contributors](https://img.shields.io/github/contributors/oceanprotocol/oceandb-bigchaindb-driver.svg)](https://github.com/oceanprotocol/oceandb-bigchaindb-driver/graphs/contributors)

---

## Table of Contents

  - [Features](#features)
  - [Quick-start](#quick-start)
  - [About BigchainDB plugin implementation](#about-bigchaindb-plugin-implementation)
  - [Code style](#code-style)
  - [Testing](#testing)
  - [New Version](#new-version)
  - [License](#license)

------------|------------
 **C**reate | **C**reate   
 **R**ead   | **R**etrieve 
 **U**pdate | **A**ppend   
 **D**elete | **B**urn     


You can find [here](https://blog.bigchaindb.com/crab-create-retrieve-append-burn-b9f6d111f460) a link talking about the CRAB model.

## Code style

The information about code style in python is documented in this two links [python-developer-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-developer-guide.md)
and [python-style-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-style-guide.md).
    
## Testing

Automatic tests are setup via Travis, executing `tox`.
Our test use pytest framework.

## New Version

The `bumpversion.sh` script helps to bump the project version. You can execute the script using as first argument {major|minor|patch} to bump accordingly the version.


## License

```
Copyright 2018 Ocean Protocol Foundation Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.