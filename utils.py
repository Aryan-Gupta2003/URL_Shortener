import hashlib
import base64

def generate_short_url(long_url):
    # Generate a hash of the long URL
    hash_object = hashlib.sha256(long_url.encode())
    hash_digest = hash_object.digest()
    
    # Encode the hash digest in Base62
    short_url = base64.urlsafe_b64encode(hash_digest[:6]).decode('utf-8')
    return short_url
