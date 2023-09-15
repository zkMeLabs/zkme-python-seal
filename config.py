# Configuration for Homomorphic Encryption (HE)

# Degree of the polynomial modulus. This parameter directly affects the security,
# performance, and noise growth in the encryption scheme.
# A higher value increases security and capacity for computations
# but also increases noise growth and reduces performance.
POLY_MODULUS_DEGREE = 8192

# Bit sizes of the coefficient modulus. This is a list of primes that represent the coefficient modulus.
# The number and size of these primes determine the level of security, noise growth,
# and the maximum computation depth.
COEFF_MODULUS_BIT_SIZES = [60, 40, 40, 60]

# The scale used in encoding real numbers into plaintext polynomials.
# It's crucial for the precision of calculations.
# A common choice is a power of two for ease of use in rescaling operations.
SCALE = 2.0 ** 40

# File name for the secret key. The secret key is used for decryption.
SECRET_KEY_NAME = 'secret_key.bin'

# File name for the public key. The public key is used for encryption.
PUBLIC_KEY_NAME = 'public_key.bin'

# File name for the relinearization key.
# This key is used to change encrypted data back to its original form after multiplication operations.
RELIN_KEY_NAME = 'relin_key.bin'

# File name for the Galois key.
# This key is used for operations like rotations in encrypted vectors.
GAL_KEY_NAME = 'gal_key.bin'
