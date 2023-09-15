import os
from seal import KeyGenerator
from config import (
    SECRET_KEY_NAME, PUBLIC_KEY_NAME, RELIN_KEY_NAME, GAL_KEY_NAME
)
from lib.get_context import get_context


def create_keys(save_dir=None, context=None):
    """
    Create and save Homomorphic Encryption (HE) keys.

    Args:
    - save_dir (str, optional): Directory where the keys will be saved. If not provided, keys won't be saved to disk.
    - context (SEALContext, optional): The SEAL context. If not provided, it will be generated.

    Returns:
    - tuple: A tuple containing the secret key, public key, relinearization key, and Galois key.
    """
    # Check if the provided directory exists, if not, create it.
    if (save_dir is not None) and (not os.path.exists(save_dir)):
        os.makedirs(save_dir)
    # If no context is provided, generate one.
    if context is None:
        context = get_context()

    # Initialize the key generator with the given context. Generate the keys.
    keygen = KeyGenerator(context)
    public_key = keygen.create_public_key()
    secret_key = keygen.secret_key()
    relin_key = keygen.create_relin_keys()
    gal_key = keygen.create_galois_keys()

    # If a save directory is provided, save the keys to the specified directory.
    if save_dir is not None:
        secret_key.save(os.path.join(save_dir, SECRET_KEY_NAME))
        public_key.save(os.path.join(save_dir, PUBLIC_KEY_NAME))
        relin_key.save(os.path.join(save_dir, RELIN_KEY_NAME))
        gal_key.save(os.path.join(save_dir, GAL_KEY_NAME))

    # Return the generated keys.
    return secret_key, public_key, relin_key, gal_key
