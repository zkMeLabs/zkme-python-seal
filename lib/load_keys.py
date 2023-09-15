import os
from seal import SecretKey, PublicKey, RelinKeys, GaloisKeys
from config import (
    SECRET_KEY_NAME, PUBLIC_KEY_NAME, RELIN_KEY_NAME, GAL_KEY_NAME
)
from lib.get_context import get_context


def load_keys(keys_dir, context=None):
    """
    Load Homomorphic Encryption (HE) keys from the specified directory on disk.

    Args:
    - keys_dir (str): The directory where the keys are stored.
    - context (SEALContext, optional): The SEAL context. If not provided, it will be generated.

    Returns:
    - tuple: A tuple containing the loaded secret key, public key, relinearization key, and Galois key.
    """
    # If no context is provided, generate one.
    if context is None:
        context = get_context()

    # Load the key from the specified file in the keys directory.
    secret_key = SecretKey()
    secret_key.load(context, os.path.join(keys_dir, SECRET_KEY_NAME))
    public_key = PublicKey()
    public_key.load(context, os.path.join(keys_dir, PUBLIC_KEY_NAME))
    relin_key = RelinKeys()
    relin_key.load(context, os.path.join(keys_dir, RELIN_KEY_NAME))
    gal_key = GaloisKeys()
    gal_key.load(context, os.path.join(keys_dir, GAL_KEY_NAME))

    # Return the loaded keys.
    return secret_key, public_key, relin_key, gal_key
