from seal import CKKSEncoder, Encryptor, Evaluator, Decryptor
from lib.get_context import get_context


def get_he_tools(public_key, secret_key, context=None):
    """
    Initialize and return the necessary tools for Homomorphic Encryption (HE) operations.

    Args:
    - public_key: The public key used for encryption.
    - secret_key: The secret key used for decryption.
    - context (SEALContext, optional): The SEAL context. If not provided, it will be generated.

    Returns:
    - tuple: A tuple containing the CKKS encoder, slot count, encryptor, evaluator, and decryptor.
    """
    # If no context is provided, generate one.
    if context is None:
        context = get_context()
    # Initialize the CKKS encoder with the given context.
    # The encoder is responsible for encoding and decoding plaintexts.
    ckks_encoder = CKKSEncoder(context)
    # Get the slot count. In CKKS, a slot can hold a single real or complex number.
    # The slot count often equals the poly modulus degree / 2.
    slot_count = ckks_encoder.slot_count()
    # Initialize the encryptor with the given context and public key.
    encryptor = Encryptor(context, public_key)
    # Initialize the evaluator with the given context.
    # The evaluator is responsible for performing operations on ciphertexts.
    evaluator = Evaluator(context)
    # Initialize the decryptor with the given context and secret key.
    decryptor = Decryptor(context, secret_key)

    return ckks_encoder, slot_count, encryptor, evaluator, decryptor
