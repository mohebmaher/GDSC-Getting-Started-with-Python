def encrypt_msg(text):
    
    words_to_nums = {w: str(n) for n, w in enumerate(text.split())}
    
    enc_msg_list = [words_to_nums[w] for w in message.split()]
    enc_msg_str = " ".join(enc_msg_list)
    
    return enc_msg_str, words_to_nums


def encrypt_msg(enc_text, words_to_nums):
    
    nums_to_words = {n: w for w, n in words_to_nums.items()}
    
    dec_msg_list = [nums_to_words[n] for n in enc_text.split()]
    dec_msg_str = " ".join(dec_msg_list)
    
    return dec_msg_str


message = "NumPy, short for Numerical Python,\
has long been a cornerstone of numerical computing in Python.\
It provides the data structures, algorithms, and library glue\
needed for most scientific applications involving numerical data in Python."
    