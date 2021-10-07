The binary uses exceptions to call WinAPIs. Trace AddVectoredExceptionsHandler to find the function that is responsible for resolving the APIs and calling them. The API calls are made via patching, and modifications of EIP.

Thread 4 is the main function to reverse. Within thread 4, there is 4 hex strings loaded into memory, and will be decrypted after passing checks in thread3. However, manual decryption of the strings can be done to reveal L0ve,s3cret,5Ex & g0d. These 4 strings are then passed into a crc32 function to form a key, to decrypt the ciphertext via ARC4.

`n0_mOr3_eXcEpti0n$_p1ea$e@flare-on.com`
