import math
from typing import List
import seal
from seal import Ciphertext

from config import SCALE
from lib.get_context import get_context
from lib.create_keys import create_keys
from lib.load_keys import load_keys
from lib.get_he_tools import get_he_tools


class HECryptor(object):
    """
    HECryptor class provides methods for encrypting, decrypting, and performing
    operations on encrypted data using Homomorphic Encryption (HE).
    """
    def __init__(self, keys_dir: str = None):
        """
        Initialize the HECryptor with necessary tools and keys.

        Args:
        - keys_dir (str, optional): Directory where the keys are stored. If not provided, new keys will be generated.
        """
        self.context = get_context()
        if keys_dir is not None:
            self.secret_key, self.public_key, self.relin_key, self.gal_key = load_keys(keys_dir, self.context)
        else:
            self.secret_key, self.public_key, self.relin_key, self.gal_key = create_keys(context=self.context)
        self.scale = SCALE
        self.ckks_encoder, self.slot_count, self.encryptor, self.evaluator, self.decryptor = get_he_tools(
            self.public_key, self.secret_key, self.context)

    def encrypt_data(self, data: List[float]) -> seal.Ciphertext:
        """
        Encrypt a list of floating-point numbers into a ciphertext.

        Args:
        - data (List[float]): List of floating-point numbers to be encrypted.

        Returns:
        - seal.Ciphertext: Encrypted data.
        """
        plain = self.ckks_encoder.encode(data, self.scale)
        cipher = self.encryptor.encrypt(plain)

        return cipher

    def decrypt_data(self, cipher: seal.Ciphertext) -> List[float]:
        """
        Decrypt a ciphertext back into a list of floating-point numbers.

        Args:
        - cipher (seal.Ciphertext): The encrypted data.

        Returns:
        - List[float]: Decrypted list of floating-point numbers.
        """
        plain = self.decryptor.decrypt(cipher)
        data = self.ckks_encoder.decode(plain)

        return data

    def cal_cipher_l2(self, cipher1, cipher2):
        """
        Calculate the L2 (Euclidean) distance between two ciphertexts.

        The process involves the following steps:
        1. Compute the difference between the two ciphertexts.
        2. Square the result.
        3. Sum the squared result.
        4. Compute the square root of the sum.

        Args:
        - cipher1, cipher2: The two ciphertexts for which the L2 distance is to be calculated.

        Returns:
        - seal.Ciphertext: Encrypted L2 distance.
        """
        # a = x - y
        temp = Ciphertext(cipher1)
        self.evaluator.sub_inplace(temp, cipher2)
        # b = a * a
        self.evaluator.multiply_inplace(temp, temp)
        self.evaluator.relinearize_inplace(temp, self.relin_key)
        # c = sum(b)
        encrypted_result = Ciphertext(temp)
        k = 0
        while k < math.log(self.slot_count, 2):
            temp = self.evaluator.rotate_vector(encrypted_result, pow(2, k), self.gal_key)
            self.evaluator.add_inplace(encrypted_result, temp)
            k += 1
        self.evaluator.relinearize_inplace(encrypted_result, self.relin_key)

        # Lower the cipher scale.
        self.evaluator.rescale_to_next_inplace(encrypted_result)

        return encrypted_result

