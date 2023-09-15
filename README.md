# zkme-he 

This library is built upon [**SEAL-Python**](https://github.com/Huelse/SEAL-Python), showcasing the power and potential of Homomorphic Encryption (HE) in the context of the zkMe project. One of its primary objectives is to demonstrate how HE can be employed to protect sensitive facial feature information of users. Remarkably, it highlights the capability of performing computations directly on encrypted data without the need to decrypt it first. Furthermore, for those technical enthusiasts keen on understanding the intricacies of HE, the library also provides step-by-step Jupyter documentation. This documentation elucidates how HE operates under the classes of SEAL, offering a comprehensive guide for those intrigued by the world of Homomorphic Encryption.

## [zkMe](https://zk.me)

zkMe verifies user credentials without disclosing any personal information to anyone. Through the use of innovative zero-knowledge technologies, it is the only KYC solution to be fully decentralized, private-by-design and compliant with global AML requirements. No credential verified through the zkMe app is stored on any centralized storage, making it virtual impossible for any private data leak. The only thing shared (if authorized by you) are yes/no answers to basic elegibility questions such as "are you over 18 years old?". [https://zk.me/]

## Microsoft SEAL For Python

Microsoft [**SEAL**](https://github.com/microsoft/SEAL) is an easy-to-use open-source ([MIT licensed](https://github.com/microsoft/SEAL/blob/master/LICENSE)) homomorphic encryption library developed by the Cryptography Research group at Microsoft.

[**SEAL-Python**](https://github.com/Huelse/SEAL-Python) is a python binding for the Microsoft SEAL library.

This project is based on [**SEAL-Python**](https://github.com/Huelse/SEAL-Python)

## Contents

* [Environment](#Environment)
* [Prepare](#Prepare)
* [Demo](#Demo)

## Environment

* Python 3.9 or later
* Check the requirements.txt

## Prepare

* #### Install [**SEAL-Python**](https://github.com/Huelse/SEAL-Python)

    Please follow the instructions in the [git library](https://github.com/Huelse/SEAL-Python) on Build section. Make sure you have installed the SEAL library and SEAL-Python successfully. The .so file should be in the current directory or you have installed it already.

## Demo
All the examples are in the `examples` folder and build by `jupyter notebook` which is a good tool to learn and test the code.
* Basic functions

  `examples/1_basic_he_func.ipynb`

  The basic functions are the same as the C++ SEAL library.
  Here is a simple example that demonstrates the calculation of the L2 distance using both homomorphic encryption and matrix computation. By comparing the results, one can directly appreciate the use of homomorphic encryption.
