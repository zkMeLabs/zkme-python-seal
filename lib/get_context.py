from seal import EncryptionParameters, scheme_type, CoeffModulus, SEALContext
from config import POLY_MODULUS_DEGREE, COEFF_MODULUS_BIT_SIZES


def get_context(
        scheme=scheme_type.ckks, poly_modulus_degree=POLY_MODULUS_DEGREE,
        coeff_modulus_bit_sizes=COEFF_MODULUS_BIT_SIZES):
    """
    Create and return a SEAL context based on the provided or default configuration parameters.

    Args:
    - scheme (scheme_type, optional): The encryption scheme type (e.g., CKKS or BFV). Default is CKKS.
    - poly_modulus_degree (int, optional): Degree of the polynomial modulus. Default is from the config.
    - coeff_modulus_bit_sizes (list of int, optional): Bit sizes of the coefficient modulus. Default is from the config.

    Returns:
    - SEALContext: The generated SEAL context.
    """
    # Initialize encryption parameters with the specified scheme.
    parms = EncryptionParameters(scheme)
    # Set the polynomial modulus degree for the encryption parameters.
    parms.set_poly_modulus_degree(poly_modulus_degree)
    # Set the coefficient modulus for the encryption parameters.
    # CoeffModulus.Create is a helper function that
    # generates a list of prime numbers that represent the coefficient modulus.
    parms.set_coeff_modulus(CoeffModulus.Create(poly_modulus_degree, coeff_modulus_bit_sizes))
    # Create and return the SEAL context using the specified encryption parameters.
    context = SEALContext(parms)

    return context
