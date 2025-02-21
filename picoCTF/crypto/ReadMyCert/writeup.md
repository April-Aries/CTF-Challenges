# ReadMyCert

| Information | Description |
| :-- | :-- |
| Category | Crypto |
| Difficulty | Medium |

# Problem Description

How about we take you on an adventure on exploring certificate signing requests?
Take a look at this CSR file [here](https://artifacts.picoctf.net/c/426/readmycert.csr).

# Solution

Use command `openssl req -in readmycert.csr -text -noout` to read the CSR (Certificate Signing Request) and the flag is in the common name (CN) of suject.

Details of the command:

| Command | Explanation |
| :-- | :-- |
| openssl req | PKCS#10 X.509 Certificate Signing Request (CSR) Management. |
| -in readmycert.csr | Specifying the input filename to read a request from |
| -text	| Prints+ing out the certificate request in text form. |
| -noout | preventing output of the encoded version of the certificate request. |

:triangular_flag_on_post:: `picoCTF{read_mycert_41d1c74c}`
